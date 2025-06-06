# posixUID

**Framework**: Collaboration  
**Kind**: property

Returns the POSIX UID of the identity.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var posixUID: uid_t { get }
```

#### Return Value

The POSIX UID of the identity.

#### Discussion

The POSIX UID is a integer that can identify a user within an identity authority. UIDs are not guaranteed to be unique within an identity authority.

## See Also

- [init?(posixUID: uid_t, authority: CBIdentityAuthority)](cbuseridentity/init(posixuid:authority:).md)
  Returns the user identity with the given POSIX UID in the specified identity authority.


---

*[View on Apple Developer](https://developer.apple.com/documentation/collaboration/cbuseridentity/posixuid)*