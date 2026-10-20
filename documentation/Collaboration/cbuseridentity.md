# CBUserIdentity

**Framework**: Collaboration  
**Kind**: class  
**Role**: Class

An object of the `CBUserIdentity` class represents a user identity and is used for accessing the attributes of a user identity from an identity authority. The principal attributes of `CBUserIdentity` are a POSIX user identifier (UID), password, and certificate.

**Availability**:
- macOS 10.5+

## Declaration

```swift
class CBUserIdentity
```

```objc
@interface CBUserIdentity : CBIdentity
```

## Topics

### Password Authentication
- [func authenticate(withPassword: String) -> Bool](./cbuseridentity/authenticate%28withpassword%29.md)
  Returns a Boolean value indicating whether the given password is correct for the identity.
- [var certificate: SecCertificate?](./cbuseridentity/certificate.md)
  Returns the public authentication certificate associated with a user identity.
- [var isEnabled: Bool](./cbuseridentity/isenabled.md)
  Returns a Boolean value indicating whether the identity is allowed to authenticate.
### Using UIDs
- [var posixUID: uid_t](./cbuseridentity/posixuid.md)
  Returns the POSIX UID of the identity.
- [init?(posixUID: uid_t, authority: CBIdentityAuthority)](./cbuseridentity/init%28posixuid,authority%29.md)
  Returns the user identity with the given POSIX UID in the specified identity authority.

## Relationships

### Inherits From
- [CBIdentity](./cbidentity.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/collaboration/cbuseridentity)*