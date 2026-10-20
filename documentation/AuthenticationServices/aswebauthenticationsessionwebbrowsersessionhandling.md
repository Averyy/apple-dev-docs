# ASWebAuthenticationSessionWebBrowserSessionHandling

**Framework**: Authentication Services  
**Kind**: protocol  
**Role**: Protocol

An interface that a session handler implements to handle login requests from an app.

**Availability**:
- macOS 10.15+

## Declaration

```swift
protocol ASWebAuthenticationSessionWebBrowserSessionHandling
```

```objc
@protocol ASWebAuthenticationSessionWebBrowserSessionHandling
```

## Mentions

- [Supporting Single Sign-On in a Web Browser App](./supporting-single-sign-on-in-a-web-browser-app.md)

## Topics

### Starting and Stopping a Session Request
- [func begin(ASWebAuthenticationSessionRequest!)](./aswebauthenticationsessionwebbrowsersessionhandling/begin%28_%29.md)
  Handles the given session request from an app.
- [func cancel(ASWebAuthenticationSessionRequest!)](./aswebauthenticationsessionwebbrowsersessionhandling/cancel%28_%29.md)
  Cancels the process of handling the given request.
- [class ASWebAuthenticationSessionRequest](./aswebauthenticationsessionrequest.md)
  A login session request that a web browser receives from an app.

## See Also

### Handling a Session Request
- [var sessionHandler: any ASWebAuthenticationSessionWebBrowserSessionHandling](./aswebauthenticationsessionwebbrowsersessionmanager/sessionhandler.md)
  A handler that a web browser provides to handle session requests from an app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aswebauthenticationsessionwebbrowsersessionhandling)*