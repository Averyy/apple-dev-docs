# ASWebAuthenticationSessionWebBrowserSessionHandling

**Framework**: Authentication Services  
**Kind**: protocol

An interface that a session handler implements to handle login requests from an app.

**Availability**:
- macOS 10.15+

## Declaration

```swift
protocol ASWebAuthenticationSessionWebBrowserSessionHandling
```

## Mentions

- [Supporting Single Sign-On in a Web Browser App](supporting-single-sign-on-in-a-web-browser-app.md)

## Topics

### Starting and Stopping a Session Request
- [func begin(ASWebAuthenticationSessionRequest!)](aswebauthenticationsessionwebbrowsersessionhandling/begin(_:).md)
  Handles the given session request from an app.
- [func cancel(ASWebAuthenticationSessionRequest!)](aswebauthenticationsessionwebbrowsersessionhandling/cancel(_:).md)
  Cancels the process of handling the given request.
- [class ASWebAuthenticationSessionRequest](aswebauthenticationsessionrequest.md)
  A login session request that a web browser receives from an app.

## See Also

- [var sessionHandler: any ASWebAuthenticationSessionWebBrowserSessionHandling](aswebauthenticationsessionwebbrowsersessionmanager/sessionhandler.md)
  A handler that a web browser provides to handle session requests from an app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aswebauthenticationsessionwebbrowsersessionhandling)*