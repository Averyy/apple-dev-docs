# ASAuthorizationControllerDelegate

**Framework**: Authentication Services  
**Kind**: protocol

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

## Mentions

- [Supporting Security Key Authentication Using Physical Keys](supporting-security-key-authentication-using-physical-keys.md)
- [Supporting passkeys](supporting-passkeys.md)
- [Authenticating people by using passkeys in browser apps](authenticating-people-by-using-passkeys-in-browser-apps.md)

## Topics

### Handling Successful Authorization
- [func authorizationController(ASAuthorizationController, didCompleteWithCustomMethod: ASAuthorizationCustomMethod)](asauthorizationcontrollerdelegate/authorizationcontroller(_:didcompletewithcustommethod:).md)
  Informs the delegate when authorization completes, and specifies the custom method the user selected.
- [func authorizationController(controller: ASAuthorizationController, didCompleteWithAuthorization: ASAuthorization)](asauthorizationcontrollerdelegate/authorizationcontroller(controller:didcompletewithauthorization:).md)
  Tells the delegate when authorization completes successfully.
- [class ASAuthorization](asauthorization.md)
  The encapsulation of a successful authorization by a controller.
### Handling Authorization Errors
- [func authorizationController(controller: ASAuthorizationController, didCompleteWithError: any Error)](asauthorizationcontrollerdelegate/authorizationcontroller(controller:didcompletewitherror:).md)
  Tells the delegate when authorization fails, and provides an error explaining why.
- [let ASAuthorizationErrorDomain: String](asauthorizationerrordomain.md)
  The domain of authorization errors.
- [struct ASAuthorizationError](asauthorizationerror-swift.struct.md)
  Errors that can occur during authorization.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var delegate: (any ASAuthorizationControllerDelegate)?](asauthorizationcontroller/delegate.md)
  A delegate that the authorization controller informs about the success or failure of an authorization attempt.
- [func authorizationController(ASAuthorizationController, didCompleteWithCustomMethod: ASAuthorizationCustomMethod)](asauthorizationcontrollerdelegate/authorizationcontroller(_:didcompletewithcustommethod:).md)
  Informs the delegate when authorization completes, and specifies the custom method the user selected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationcontrollerdelegate)*