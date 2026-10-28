# identityAuthorityWithCSIdentityAuthority:

**Framework**: Collaboration  
**Kind**: method  
**Role**: Type Method

Returns an identity authority specified by a given Core Services Identity authority object.

**Availability**:
- macOS 10.5+

## Declaration

```objc
+ (CBIdentityAuthority *) identityAuthorityWithCSIdentityAuthority:(CSIdentityAuthorityRef) CSIdentityAuthority;
```

## Return Value

The identity authority object for use with the Collaboration framework.

## Discussion

This method, along with [`CSIdentityAuthority`](./csidentityauthority.md), is used for interoperability with the Core Services Identity API.

## Parameters

- `CSIdentityAuthority`: The Core Services Identity opaque object.

## See Also

### Interacting with the Core Services Identity API
- [CSIdentityAuthority](./csidentityauthority.md)
  Returns an identity authority for use with the Core Services Identity API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/collaboration/cbidentityauthority/identityauthoritywithcsidentityauthority:)*