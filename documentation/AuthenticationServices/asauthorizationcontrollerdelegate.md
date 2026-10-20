# ASAuthorizationControllerDelegate

**Framework**: Authentication Services  
**Kind**: protocol  
**Role**: Protocol

An interface for providing information about the outcome of an authorization request.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
@MainActor
protocol ASAuthorizationControllerDelegate : NSObjectProtocol
```

```objc
@protocol ASAuthorizationControllerDelegate <NSObject>
```

## Mentions

- [Supporting passkeys](./supporting-passkeys.md)
- [Supporting Security Key Authentication Using Physical Keys](./supporting-security-key-authentication-using-physical-keys.md)
- [Authenticating people by using passkeys in browser apps](./authenticating-people-by-using-passkeys-in-browser-apps.md)

## Topics

### Handling Successful Authorization
- [func authorizationController(ASAuthorizationController, didCompleteWithCustomMethod: ASAuthorizationCustomMethod)](./asauthorizationcontrollerdelegate/authorizationcontroller%28_,didcompletewithcustommethod%29.md)
  Informs the delegate when authorization completes, and specifies the custom method the user selected.
- [func authorizationController(controller: ASAuthorizationController, didCompleteWithAuthorization: ASAuthorization)](./asauthorizationcontrollerdelegate/authorizationcontroller%28controller,didcompletewithauthorization%29.md)
  Tells the delegate when authorization completes successfully.
- [class ASAuthorization](./asauthorization.md)
  The encapsulation of a successful authorization by a controller.
### Handling Authorization Errors
- [func authorizationController(controller: ASAuthorizationController, didCompleteWithError: any Error)](./asauthorizationcontrollerdelegate/authorizationcontroller%28controller,didcompletewitherror%29.md)
  Tells the delegate when authorization fails, and provides an error explaining why.
- [let ASAuthorizationErrorDomain: String](./asauthorizationerrordomain.md)
  The domain of authorization errors.
- [struct ASAuthorizationError](./asauthorizationerror-swift.struct.md)
  Errors that can occur during authorization.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Responding to request completion
- [var delegate: (any ASAuthorizationControllerDelegate)?](./asauthorizationcontroller/delegate.md)
  A delegate that the authorization controller informs about the success or failure of an authorization attempt.
- [func authorizationController(ASAuthorizationController, didCompleteWithCustomMethod: ASAuthorizationCustomMethod)](./asauthorizationcontrollerdelegate/authorizationcontroller%28_,didcompletewithcustommethod%29.md)
  Informs the delegate when authorization completes, and specifies the custom method the user selected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationcontrollerdelegate)*