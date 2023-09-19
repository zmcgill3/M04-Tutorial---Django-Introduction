from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Greeting(request):
    page = "<html><body><h1>Hello World</h1></body></html>"
    return HttpResponse(page)

def otherGreeting(request):
    return render(request, "greet.html", {"title": "greetings", "message": "hello world"})