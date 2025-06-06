# ASAuthorization

**Framework**: Authentication Services  
**Kind**: class

The encapsulation of a successful authorization by a controller.

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
class ASAuthorization
```

## Topics

### Getting the Provider
- [var provider: any ASAuthorizationProvider](asauthorization/provider.md)
  The provider that created the request that resulted in the successful authorization.
### Getting the Credential
- [var credential: any ASAuthorizationCredential](asauthorization/credential.md)
  Information provided about a user after successful authentication.
- [protocol ASAuthorizationCredential](asauthorizationcredential.md)
  An interface that all credentials share.
### Characterizing an Authorization
- [ASAuthorization.Scope](asauthorization/scope.md)
  The kinds of contact information that can be requested from the user.
- [ASAuthorization.OpenIDOperation](asauthorization/openidoperation.md)
  The kinds of operations that you can perform with OpenID authentication.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func authorizationController(ASAuthorizationController, didCompleteWithCustomMethod: ASAuthorizationCustomMethod)](asauthorizationcontrollerdelegate/authorizationcontroller(_:didcompletewithcustommethod:).md)
  Informs the delegate when authorization completes, and specifies the custom method the user selected.
- [func authorizationController(controller: ASAuthorizationController, didCompleteWithAuthorization: ASAuthorization)](asauthorizationcontrollerdelegate/authorizationcontroller(controller:didcompletewithauthorization:).md)
  Tells the delegate when authorization completes successfully.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorization)*