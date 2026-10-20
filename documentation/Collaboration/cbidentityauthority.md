# CBIdentityAuthority

**Framework**: Collaboration  
**Kind**: class  
**Role**: Class

An identity authority is a database that stores information about identities. The `CBIdentityAuthority` class defines one or more identity authorities. You can search this database for identities in conjunction with the `CBIdentity` class factory methods.

**Availability**:
- macOS 10.5+

## Declaration

```swift
class CBIdentityAuthority
```

```objc
@interface CBIdentityAuthority : NSObject
```

## Topics

### Accessing Identity Authorities
- [var localizedName: String](./cbidentityauthority/localizedname.md)
  Returns the localized name of the identity authority.
- [class func local() -> CBIdentityAuthority](./cbidentityauthority/local%28%29.md)
  Returns the identity authority on the local system.
- [class func managed() -> CBIdentityAuthority](./cbidentityauthority/managed%28%29.md)
  Returns the identity authority that contains all the identities in bound network directory servers.
- [class func `default`() -> CBIdentityAuthority](./cbidentityauthority/default%28%29.md)
  Returns an identity authority that contains the identities in both the local and the network-bound authorities.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/collaboration/cbidentityauthority)*