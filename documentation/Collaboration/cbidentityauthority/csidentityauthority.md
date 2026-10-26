# CSIdentityAuthority

**Framework**: Collaboration  
**Kind**: property  
**Role**: Instance Property

Returns an identity authority for use with the Core Services Identity API.

**Availability**:
- macOS 10.5+

## Declaration

```objc
@property (readonly) CSIdentityAuthorityRef CSIdentityAuthority;
```

#### Return Value

The opaque authority object for use with the Core Services Identity API.

#### Discussion

This method, along with [`identityAuthorityWithCSIdentityAuthority:`](./identityauthoritywithcsidentityauthority_.md), is used for interoperability with the Core Services Identity API.

## See Also

### Related Documentation
- [Identity Services Programming Guide](https://developer.apple.com/library/archive/documentation/Networking/Conceptual/IdentityServices_ProgGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004490)
### Interacting with the Core Services Identity API
- [+ identityAuthorityWithCSIdentityAuthority:](./identityauthoritywithcsidentityauthority_.md)
  Returns an identity authority specified by a given Core Services Identity authority object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/collaboration/cbidentityauthority/csidentityauthority)*