# sessionHandler

**Framework**: Authentication Services  
**Kind**: property

A handler that a web browser provides to handle session requests from an app.

**Availability**:
- macOS 10.15+

## Declaration

```swift
var sessionHandler: any ASWebAuthenticationSessionWebBrowserSessionHandling { get set }
```

## Mentions

- [Supporting Single Sign-On in a Web Browser App](supporting-single-sign-on-in-a-web-browser-app.md)

#### Discussion

To enable a web browser that you write to participate in single sign-on (SSO), adopt the [`ASWebAuthenticationSessionWebBrowserSessionHandling`](aswebauthenticationsessionwebbrowsersessionhandling.md) protocol, and then set your browser app as the [`shared`](aswebauthenticationsessionwebbrowsersessionmanager/shared.md) manager’s [`sessionHandler`](aswebauthenticationsessionwebbrowsersessionmanager/sessionhandler.md).

## See Also

- [protocol ASWebAuthenticationSessionWebBrowserSessionHandling](aswebauthenticationsessionwebbrowsersessionhandling.md)
  An interface that a session handler implements to handle login requests from an app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aswebauthenticationsessionwebbrowsersessionmanager/sessionhandler)*