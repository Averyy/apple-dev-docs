# Apple News API Tutorial

**Framework**: Apple News

Request channel data and publish an article using the Apple News API.

#### Overview

In this tutorial, you’ll use Python to request channel data and publish an article to your channel. The tutorial assumes you’re familiar with basic Python programming constructs and techniques. Beginning programmers should be able to follow along and run this tutorial.

##### Alternative Tutorial Code Languages

In addition to Python, the tutorial code is also available in Java, C#, and PHP. To get the code for all four, download the [`Apple-News-API-Tutorial-Example-Code.zip`](https://developer.apple.comhttps://developer.apple.com/apple-news/download/Apple-News-API-Tutorial-Example-Code.zip) file.

##### Requirements

Before beginning the tutorial, make sure you have the following information and installed software:

- Channel ID, Key ID, and Key Secret.  See [`Use your CMS with News Publisher`](https://developer.apple.comhttps://support.apple.com/guide/news-publisher/apd88c8447e6) in News Publisher User Guide.
- [`Python`](https://developer.apple.comhttps://www.python.org). Ensure that you have `PIP` installed. `PIP` is automatically installed if you have Python 3.4+. See [`Installing Python Modules`](https://developer.apple.comhttps://docs.python.org/3/installing/index.html#installing-index).
- Python’s [`Requests`](https://developer.apple.comhttps://pypi.org/project/requests/) library.

If you are not familiar with Apple News API endpoints, see  doc:apple-news-api before you get started.

## Topics

### Apple News API Python Tutorial
- [Making an HTTP Request to the Apple News API](making-an-http-request-to-the-apple-news-api.md)
  Create the URL, set the method, and send the request.
- [Signing the HTTP Request](signing-the-http-request.md)
  Sign the canonical request and send the custom authorization header to the Apple News API.
- [Publishing an Article](publishing-an-article.md)
  Build a URL and article body for the publish-article request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenews/apple-news-api-tutorial)*