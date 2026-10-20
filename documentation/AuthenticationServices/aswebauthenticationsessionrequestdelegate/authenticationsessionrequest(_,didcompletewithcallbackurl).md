# authenticationSessionRequest(_:didCompleteWithCallbackURL:)

**Framework**: Authentication Services  
**Kind**: method  
**Role**: Instance Method

Tells the delegate, typically a browser, that the authentication completed successfully.

**Availability**:
- macOS 10.15+

## Declaration

```swift
optional func authenticationSessionRequest(_ authenticationSessionRequest: ASWebAuthenticationSessionRequest, didCompleteWithCallbackURL callbackURL: URL)
```

```objc
- (void) authenticationSessionRequest:(ASWebAuthenticationSessionRequest *) authenticationSessionRequest didCompleteWithCallbackURL:(NSURL *) callbackURL;
```

## Parameters

- `authenticationSessionRequest`: The request sending the message.
- `callbackURL`: A URL using the scheme indicated by the request’s [`callbackURLScheme`](../aswebauthenticationsessionrequest/callbackurlscheme.md) property that indicates the outcome of the authentication attempt.

## See Also

### Responding to Completion Events
- [func authenticationSessionRequest(ASWebAuthenticationSessionRequest, didCancelWithError: any Error)](./authenticationsessionrequest%28_,didcancelwitherror%29.md)
  Tells the delegate, typically a browser, that the authentication was canceled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aswebauthenticationsessionrequestdelegate/authenticationsessionrequest(_:didcompletewithcallbackurl:))*