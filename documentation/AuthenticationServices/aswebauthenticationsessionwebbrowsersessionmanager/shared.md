# shared

**Framework**: Authentication Services  
**Kind**: property

The shared manager for which a web browser acts as the session handler.

**Availability**:
- macOS 10.15+

## Declaration

```swift
class var shared: ASWebAuthenticationSessionWebBrowserSessionManager { get }
```

#### Discussion

Use this singleton when supporting single sign-on (SSO) in a web browser app. Make the web browser adopt the [`ASWebAuthenticationSessionWebBrowserSessionHandling`](aswebauthenticationsessionwebbrowsersessionhandling.md) protocol, and set it as the shared manager’s [`sessionHandler`](aswebauthenticationsessionwebbrowsersessionmanager/sessionhandler.md). This allows your browser app to receive and process [`ASWebAuthenticationSessionRequest`](aswebauthenticationsessionrequest.md) instances from other apps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aswebauthenticationsessionwebbrowsersessionmanager/shared)*