# ASWebAuthenticationSessionRequestDelegate

**Framework**: Authentication Services  
**Kind**: protocol  
**Role**: Protocol

An interface through which the session request can inform its delegate, which is typically a browser, about the outcome of the authentication attempt.

**Availability**:
- macOS 10.15+

## Declaration

```swift
protocol ASWebAuthenticationSessionRequestDelegate : NSObjectProtocol
```

```objc
@protocol ASWebAuthenticationSessionRequestDelegate <NSObject>
```

## Topics

### Responding to Completion Events
- [func authenticationSessionRequest(ASWebAuthenticationSessionRequest, didCompleteWithCallbackURL: URL)](./aswebauthenticationsessionrequestdelegate/authenticationsessionrequest%28_,didcompletewithcallbackurl%29.md)
  Tells the delegate, typically a browser, that the authentication completed successfully.
- [func authenticationSessionRequest(ASWebAuthenticationSessionRequest, didCancelWithError: any Error)](./aswebauthenticationsessionrequestdelegate/authenticationsessionrequest%28_,didcancelwitherror%29.md)
  Tells the delegate, typically a browser, that the authentication was canceled.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Indicating completion
- [var delegate: (any ASWebAuthenticationSessionRequestDelegate)?](./aswebauthenticationsessionrequest/delegate.md)
  A delegate that the session request instance informs about authentication completion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aswebauthenticationsessionrequestdelegate)*