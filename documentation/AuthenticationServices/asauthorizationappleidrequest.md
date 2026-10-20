# ASAuthorizationAppleIDRequest

**Framework**: Authentication Services  
**Kind**: class  
**Role**: Class

An OpenID authorization request that relies on the user’s Apple ID.

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
class ASAuthorizationAppleIDRequest
```

```objc
@interface ASAuthorizationAppleIDRequest : ASAuthorizationOpenIDRequest
```

## Topics

### Setting the User
- [var user: String?](./asauthorizationappleidrequest/user.md)
  An identifier associated with the user’s Apple ID.

## Relationships

### Inherits From
- [ASAuthorizationOpenIDRequest](./asauthorizationopenidrequest.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Creating Requests
- [func createRequest() -> ASAuthorizationAppleIDRequest](./asauthorizationappleidprovider/createrequest%28%29.md)
  Creates a new Apple ID authorization request.
- [class ASAuthorizationOpenIDRequest](./asauthorizationopenidrequest.md)
  An OpenID authorization request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationappleidrequest)*