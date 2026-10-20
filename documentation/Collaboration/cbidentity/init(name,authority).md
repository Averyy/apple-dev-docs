# init(name:authority:)

**Framework**: Collaboration  
**Kind**: init  
**Role**: Initializer

Returns the identity object with the given name from the specified identity authority.

**Availability**:
- macOS 10.5+

## Declaration

```swift
init?(name: String, authority: CBIdentityAuthority)
```

```objc
+ (CBIdentity *) identityWithName:(NSString *) name authority:(CBIdentityAuthority *) authority;
```

#### Return Value

The identity object, or `nil` if no identity is found with the specified name.

#### Discussion

The name is compared against all valid identity names, including full names, short names, email addresses, and aliases.

## Parameters

- `name`: The name of the identity.
- `authority`: The identity authority to search.

## See Also

### Finding Identities
- [init?(persistentReference: Data)](./init%28persistentreference%29.md)
  Returns the identity object matching the persistent reference data.
- [init?(uuidString: String, authority: CBIdentityAuthority)](./init%28uuidstring,authority%29-13vns.md)
  Returns the identity object with the given UUID from the specified identity authority.


---

*[View on Apple Developer](https://developer.apple.com/documentation/collaboration/cbidentity/init(name:authority:))*