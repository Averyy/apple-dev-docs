# ASWebAuthenticationSessionRequestDelegate

**Framework**: Authentication Services  
**Kind**: protocol

An interface through which the session request can inform its delegate, which is typically a browser, about the outcome of the authentication attempt.

**Availability**:
- macOS 10.15+

## Declaration

```swift
protocol ASWebAuthenticationSessionRequestDelegate : NSObjectProtocol
```

## Topics

### Responding to Completion Events
- [func authenticationSessionRequest(ASWebAuthenticationSessionRequest, didCompleteWithCallbackURL: URL)](aswebauthenticationsessionrequestdelegate/authenticationsessionrequest(_:didcompletewithcallbackurl:).md)
  Tells the delegate, typically a browser, that the authentication completed successfully.
- [func authenticationSessionRequest(ASWebAuthenticationSessionRequest, didCancelWithError: any Error)](aswebauthenticationsessionrequestdelegate/authenticationsessionrequest(_:didcancelwitherror:).md)
  Tells the delegate, typically a browser, that the authentication was canceled.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var delegate: (any ASWebAuthenticationSessionRequestDelegate)?](aswebauthenticationsessionrequest/delegate.md)
  A delegate that the session request instance informs about authentication completion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aswebauthenticationsessionrequestdelegate)*