# local()

**Framework**: Collaboration  
**Kind**: method

Returns the identity authority on the local system.

**Availability**:
- macOS 10.5+

## Declaration

```swift
class func local() -> CBIdentityAuthority
```

#### Return Value

The identity authority on the local system.

#### Discussion

Any identities stored on the local system are contained within this identity authority.

## See Also

- [var localizedName: String](cbidentityauthority/localizedname.md)
  Returns the localized name of the identity authority.
- [class func managed() -> CBIdentityAuthority](cbidentityauthority/managed.md)
  Returns the identity authority that contains all the identities in bound network directory servers.
- [class func `default`() -> CBIdentityAuthority](cbidentityauthority/default.md)
  Returns an identity authority that contains the identities in both the local and the network-bound authorities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/collaboration/cbidentityauthority/local())*