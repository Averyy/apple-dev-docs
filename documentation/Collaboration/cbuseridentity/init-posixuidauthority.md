# init(posixUID:authority:)

**Framework**: Collaboration  
**Kind**: init

Returns the user identity with the given POSIX UID in the specified identity authority.

**Availability**:
- macOS 10.5+

## Declaration

```swift
init?(posixUID uid: uid_t, authority: CBIdentityAuthority)
```

#### Return Value

The user identity with the given UID in the specified identity authority, or `nil` if no identity exists with the specified UID.

## Parameters

- `uid`: The UID of the identity you are searching for.
- `authority`: The identity authority to search.

## See Also

- [var posixUID: uid_t](cbuseridentity/posixuid.md)
  Returns the POSIX UID of the identity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/collaboration/cbuseridentity/init(posixuid:authority:))*