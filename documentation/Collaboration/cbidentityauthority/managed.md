# managed()

**Framework**: Collaboration  
**Kind**: method

Returns the identity authority that contains all the identities in bound network directory servers.

**Availability**:
- macOS 10.5+

## Declaration

```swift
class func managed() -> CBIdentityAuthority
```

#### Return Value

The identity authorities in bound network directory servers.

#### Discussion

If you are bound to a network directory server (such as an LDAP server) that has an identity authority, use this method to search those authorities.

## See Also

- [var localizedName: String](cbidentityauthority/localizedname.md)
  Returns the localized name of the identity authority.
- [class func local() -> CBIdentityAuthority](cbidentityauthority/local.md)
  Returns the identity authority on the local system.
- [class func `default`() -> CBIdentityAuthority](cbidentityauthority/default.md)
  Returns an identity authority that contains the identities in both the local and the network-bound authorities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/collaboration/cbidentityauthority/managed())*