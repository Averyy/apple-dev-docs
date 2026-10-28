# cancelWithError(_:)

**Framework**: Authentication Services  
**Kind**: method  
**Role**: Instance Method

Indicates that the browser canceled the authentication attempt.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func cancelWithError(_ error: any Error)
```

```objc
- (void) cancelWithError:(NSError *) error;
```

## Mentions

- [Supporting Single Sign-On in a Web Browser App](../supporting-single-sign-on-in-a-web-browser-app.md)

## Discussion

Call this method from your browser app when the authentication attempt fails to complete, for example because the user cancels it.

## Parameters

- `error`: An error with domain [`ASWebAuthenticationSessionErrorDomain`](../aswebauthenticationsessionerrordomain.md) and a suitable code from [`ASWebAuthenticationSessionError.Code`](../aswebauthenticationsessionerror/code.md) that indicates the reason for the cancelation.

## See Also

### Finishing a request
- [var callback: ASWebAuthenticationSession.Callback?](./callback.md)
  The callback to listen for, which completes the request.
- [ASWebAuthenticationSession.Callback](../aswebauthenticationsession/callback.md)
  An object for evaluating navigation events in an authentication session.
- [func complete(withCallbackURL: URL)](./complete%28withcallbackurl%29.md)
  Indicates that the browser successfully completed the authentication attempt.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aswebauthenticationsessionrequest/cancelwitherror(_:))*