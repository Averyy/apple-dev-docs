# localizedName

**Framework**: Collaboration  
**Kind**: property

Returns the localized name of the identity authority.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var localizedName: String { get }
```

#### Return Value

The computer’s name if the authority is local, or Managed Network Directory if the authority is managed.

## See Also

- [class func local() -> CBIdentityAuthority](cbidentityauthority/local.md)
  Returns the identity authority on the local system.
- [class func managed() -> CBIdentityAuthority](cbidentityauthority/managed.md)
  Returns the identity authority that contains all the identities in bound network directory servers.
- [class func `default`() -> CBIdentityAuthority](cbidentityauthority/default.md)
  Returns an identity authority that contains the identities in both the local and the network-bound authorities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/collaboration/cbidentityauthority/localizedname)*