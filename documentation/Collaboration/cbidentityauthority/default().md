# default()

**Framework**: Collaboration  
**Kind**: method  
**Role**: Type Method

Returns an identity authority that contains the identities in both the local and the network-bound authorities.

**Availability**:
- macOS 10.5+

## Declaration

```swift
class func `default`() -> CBIdentityAuthority
```

```objc
+ (CBIdentityAuthority *) defaultIdentityAuthority;
```

## Return Value

The local and network-bound identity authorities.

## Discussion

The default identity authority is the logical union of the identities in the local and managed authorities.

## See Also

### Accessing Identity Authorities
- [var localizedName: String](./localizedname.md)
  Returns the localized name of the identity authority.
- [class func local() -> CBIdentityAuthority](./local%28%29.md)
  Returns the identity authority on the local system.
- [class func managed() -> CBIdentityAuthority](./managed%28%29.md)
  Returns the identity authority that contains all the identities in bound network directory servers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/collaboration/cbidentityauthority/default())*