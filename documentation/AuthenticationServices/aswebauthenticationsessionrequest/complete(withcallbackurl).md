# complete(withCallbackURL:)

**Framework**: Authentication Services  
**Kind**: method  
**Role**: Instance Method

Indicates that the browser successfully completed the authentication attempt.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func complete(withCallbackURL url: URL)
```

```objc
- (void) completeWithCallbackURL:(NSURL *) url;
```

## Mentions

- [Supporting Single Sign-On in a Web Browser App](../supporting-single-sign-on-in-a-web-browser-app.md)

## Discussion

Call this method from your browser app when the authentication attempt completes to report the result of the attempt using the callback URL.

## Parameters

- `url`: A URL using the scheme indicated by the request’s [`callbackURLScheme`](./callbackurlscheme.md) property that indicates the outcome of the authentication attempt.

## See Also

### Finishing a request
- [var callback: ASWebAuthenticationSession.Callback?](./callback.md)
  The callback to listen for, which completes the request.
- [ASWebAuthenticationSession.Callback](../aswebauthenticationsession/callback.md)
  An object for evaluating navigation events in an authentication session.
- [func cancelWithError(any Error)](./cancelwitherror%28_%29.md)
  Indicates that the browser canceled the authentication attempt.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aswebauthenticationsessionrequest/complete(withcallbackurl:))*