# init(posixGID:authority:)

**Framework**: Collaboration  
**Kind**: init

Returns the group identity with the given POSIX GID in the specified identity authority.

**Availability**:
- macOS 10.5+

## Declaration

```swift
init?(posixGID gid: gid_t, authority: CBIdentityAuthority)
```

#### Return Value

The group identity object with the given GID in the specified identity authority, or `nil` if no identity exists with the specified GID.

## Parameters

- `gid`: The GID of the group identity you are searching for.
- `authority`: An identity authority in which to search for the group identity.

## See Also

- [Identity Services Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Networking/Conceptual/IdentityServices_ProgGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004490)


---

*[View on Apple Developer](https://developer.apple.com/documentation/collaboration/cbgroupidentity/init(posixgid:authority:))*