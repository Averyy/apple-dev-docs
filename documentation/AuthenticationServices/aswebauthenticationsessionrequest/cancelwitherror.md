# cancelWithError(_:)

**Framework**: Authentication Services  
**Kind**: method

Indicates that the browser canceled the authentication attempt.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func cancelWithError(_ error: any Error)
```

## Mentions

- [Supporting Single Sign-On in a Web Browser App](supporting-single-sign-on-in-a-web-browser-app.md)

#### Discussion

Call this method from your browser app when the authentication attempt fails to complete, for example because the user cancels it.

## Parameters

- `error`: An error with domain   and a suitable code from   that indicates the reason for the cancelation.

## See Also

- [var callback: ASWebAuthenticationSession.Callback?](aswebauthenticationsessionrequest/callback.md)
  The callback to listen for, which completes the request.
- [ASWebAuthenticationSession.Callback](aswebauthenticationsession/callback.md)
  An object for evaluating navigation events in an authentication session.
- [func complete(withCallbackURL: URL)](aswebauthenticationsessionrequest/complete(withcallbackurl:).md)
  Indicates that the browser successfully completed the authentication attempt.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aswebauthenticationsessionrequest/cancelwitherror(_:))*