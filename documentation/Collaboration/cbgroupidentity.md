# CBGroupIdentity

**Framework**: Collaboration  
**Kind**: class

An object of the `CBGroupIdentity` class represents a group identity and is used for viewing the attributes of group identities from an identity authority. The principal attributes of a `CBGroupIdentity` object are a POSIX group identifier (GID) and a list of members.

**Availability**:
- macOS 10.5+

## Declaration

```swift
class CBGroupIdentity
```

## Topics

### Finding Group Identities
- [init?(posixGID: gid_t, authority: CBIdentityAuthority)](cbgroupidentity/init(posixgid:authority:).md)
  Returns the group identity with the given POSIX GID in the specified identity authority.
### Group Identity Attributes
- [var posixGID: gid_t](cbgroupidentity/posixgid.md)
  Returns the POSIX GID of the identity.
### Instance Properties
- [var memberIdentities: [CBIdentity]](cbgroupidentity/memberidentities.md)

## Relationships

### Inherits From
- [CBIdentity](cbidentity.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/collaboration/cbgroupidentity)*