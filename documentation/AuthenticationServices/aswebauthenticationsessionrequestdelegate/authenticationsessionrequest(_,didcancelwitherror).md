# authenticationSessionRequest(_:didCancelWithError:)

**Framework**: Authentication Services  
**Kind**: method  
**Role**: Instance Method

Tells the delegate, typically a browser, that the authentication was canceled.

**Availability**:
- macOS 10.15+

## Declaration

```swift
optional func authenticationSessionRequest(_ authenticationSessionRequest: ASWebAuthenticationSessionRequest, didCancelWithError error: any Error)
```

```objc
- (void) authenticationSessionRequest:(ASWebAuthenticationSessionRequest *) authenticationSessionRequest didCancelWithError:(NSError *) error;
```

## Parameters

- `authenticationSessionRequest`: The request sending the message.
- `error`: An error that indicates the reason for the cancelation.

## See Also

### Responding to Completion Events
- [func authenticationSessionRequest(ASWebAuthenticationSessionRequest, didCompleteWithCallbackURL: URL)](./authenticationsessionrequest%28_,didcompletewithcallbackurl%29.md)
  Tells the delegate, typically a browser, that the authentication completed successfully.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aswebauthenticationsessionrequestdelegate/authenticationsessionrequest(_:didcancelwitherror:))*