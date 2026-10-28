# identityWithCSIdentity:

**Framework**: Collaboration  
**Kind**: method  
**Role**: Type Method

Returns an identity object created from the specified Core Services Identity opaque object.

**Availability**:
- macOS 10.5+

## Declaration

```objc
+ (CBIdentity *) identityWithCSIdentity:(CSIdentityRef) csIdentity;
```

## Return Value

The identity object for use with the Collaboration framework.

## Discussion

This method is used for interoperability with the Core Services Identity API.

## Parameters

- `csIdentity`: The Core Services Identity opaque object.

## See Also

### Related Documentation
- [Identity Services Programming Guide](https://developer.apple.com/library/archive/documentation/Networking/Conceptual/IdentityServices_ProgGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004490)
### Finding Identities
- [init?(name: String, authority: CBIdentityAuthority)](./init%28name,authority%29.md)
  Returns the identity object with the given name from the specified identity authority.
- [init?(persistentReference: Data)](./init%28persistentreference%29.md)
  Returns the identity object matching the persistent reference data.
- [init?(uuidString: String, authority: CBIdentityAuthority)](./init%28uuidstring,authority%29-13vns.md)
  Returns the identity object with the given UUID from the specified identity authority.


---

*[View on Apple Developer](https://developer.apple.com/documentation/collaboration/cbidentity/identitywithcsidentity:)*