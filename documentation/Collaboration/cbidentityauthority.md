# CBIdentityAuthority

**Framework**: Collaboration  
**Kind**: class

An identity authority is a database that stores information about identities. The `CBIdentityAuthority` class defines one or more identity authorities. You can search this database for identities in conjunction with the `CBIdentity` class factory methods.

**Availability**:
- macOS 10.5+

## Declaration

```swift
class CBIdentityAuthority
```

## Topics

### Accessing Identity Authorities
- [var localizedName: String](cbidentityauthority/localizedname.md)
  Returns the localized name of the identity authority.
- [class func local() -> CBIdentityAuthority](cbidentityauthority/local.md)
  Returns the identity authority on the local system.
- [class func managed() -> CBIdentityAuthority](cbidentityauthority/managed.md)
  Returns the identity authority that contains all the identities in bound network directory servers.
- [class func `default`() -> CBIdentityAuthority](cbidentityauthority/default.md)
  Returns an identity authority that contains the identities in both the local and the network-bound authorities.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/collaboration/cbidentityauthority)*