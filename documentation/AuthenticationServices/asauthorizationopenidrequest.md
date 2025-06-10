# ASAuthorizationOpenIDRequest

**Framework**: Authentication Services  
**Kind**: class

An OpenID authorization request.

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
class ASAuthorizationOpenIDRequest
```

## Topics

### Setting the Operation
- [var requestedOperation: ASAuthorization.OpenIDOperation](asauthorizationopenidrequest/requestedoperation.md)
  The OpenID authentication operation you want this request to perform.
- [ASAuthorization.OpenIDOperation](asauthorization/openidoperation.md)
  The kinds of operations that you can perform with OpenID authentication.
### Setting the Scope
- [var requestedScopes: [ASAuthorization.Scope]?](asauthorizationopenidrequest/requestedscopes.md)
  The contact information to be requested from the user during authentication.
- [ASAuthorization.Scope](asauthorization/scope.md)
  The kinds of contact information that can be requested from the user.
### Setting the State
- [var state: String?](asauthorizationopenidrequest/state.md)
  Data that’s returned to you unmodified in the corresponding credential after a successful authentication.
### Setting the Nonce
- [var nonce: String?](asauthorizationopenidrequest/nonce.md)
  A string value to pass to the identity provider.

## Relationships

### Inherits From
- [ASAuthorizationRequest](asauthorizationrequest.md)
### Inherited By
- [ASAuthorizationAppleIDRequest](asauthorizationappleidrequest.md)
- [ASAuthorizationSingleSignOnRequest](asauthorizationsinglesignonrequest.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func createRequest() -> ASAuthorizationAppleIDRequest](asauthorizationappleidprovider/createrequest.md)
  Creates a new Apple ID authorization request.
- [class ASAuthorizationAppleIDRequest](asauthorizationappleidrequest.md)
  An OpenID authorization request that relies on the user’s Apple ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationopenidrequest)*