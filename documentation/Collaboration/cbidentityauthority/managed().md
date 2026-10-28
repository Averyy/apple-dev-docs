# managed()

**Framework**: Collaboration  
**Kind**: method  
**Role**: Type Method

Returns the identity authority that contains all the identities in bound network directory servers.

**Availability**:
- macOS 10.5+

## Declaration

```swift
class func managed() -> CBIdentityAuthority
```

```objc
+ (CBIdentityAuthority *) managedIdentityAuthority;
```

## Return Value

The identity authorities in bound network directory servers.

## Discussion

If you are bound to a network directory server (such as an LDAP server) that has an identity authority, use this method to search those authorities.

## See Also

### Accessing Identity Authorities
- [var localizedName: String](./localizedname.md)
  Returns the localized name of the identity authority.
- [class func local() -> CBIdentityAuthority](./local%28%29.md)
  Returns the identity authority on the local system.
- [class func `default`() -> CBIdentityAuthority](./default%28%29.md)
  Returns an identity authority that contains the identities in both the local and the network-bound authorities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/collaboration/cbidentityauthority/managed())*