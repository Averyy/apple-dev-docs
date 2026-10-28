# init(uuidString:authority:)

**Framework**: Collaboration  
**Kind**: init  
**Role**: Initializer

Returns the identity object with the given UUID from the specified identity authority.

**Availability**:
- macOS 10.5+ - Deprecated in 10.11

> **Deprecated**: Use +identityWithUniqueIdentifier:authority: instead.

## Declaration

```swift
init?(uuidString uuid: String, authority: CBIdentityAuthority)
```

```objc
+ (CBIdentity *) identityWithUUIDString:(NSString *) uuid authority:(CBIdentityAuthority *) authority;
```

## Return Value

The identity object, or `nil` if no identity is found with the matching criteria.

## Parameters

- `uuid`: The UUID of the identity you are searching for.
- `authority`: The identity authority to search.

## See Also

### Finding Identities
- [init?(name: String, authority: CBIdentityAuthority)](./init%28name,authority%29.md)
  Returns the identity object with the given name from the specified identity authority.
- [init?(persistentReference: Data)](./init%28persistentreference%29.md)
  Returns the identity object matching the persistent reference data.
- [+ identityWithCSIdentity:](./identitywithcsidentity_.md)
  Returns an identity object created from the specified Core Services Identity opaque object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/collaboration/cbidentity/init(uuidstring:authority:)-13vns)*