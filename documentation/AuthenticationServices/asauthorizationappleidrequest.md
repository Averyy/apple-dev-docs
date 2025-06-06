# ASAuthorizationAppleIDRequest

**Framework**: Authentication Services  
**Kind**: class

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

## Topics

### Setting the User
- [var user: String?](asauthorizationappleidrequest/user.md)
  An identifier associated with the user’s Apple ID.

## Relationships

### Inherits From
- [ASAuthorizationOpenIDRequest](asauthorizationopenidrequest.md)
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

## See Also

- [func createRequest() -> ASAuthorizationAppleIDRequest](asauthorizationappleidprovider/createrequest.md)
  Creates a new Apple ID authorization request.
- [class ASAuthorizationOpenIDRequest](asauthorizationopenidrequest.md)
  An OpenID authorization request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationappleidrequest)*