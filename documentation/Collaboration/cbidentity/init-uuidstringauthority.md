# init(uuidString:authority:)

**Framework**: Collaboration  
**Kind**: init

Returns the identity object with the given UUID from the specified identity authority.

**Availability**:
- macOS 10.5+

## Declaration

```swift
init?(uuidString uuid: String, authority: CBIdentityAuthority)
```

#### Return Value

The identity object, or `nil` if no identity is found with the matching criteria.

## Parameters

- `uuid`: The UUID of the identity you are searching for.
- `authority`: The identity authority to search.

## See Also

- [init?(name: String, authority: CBIdentityAuthority)](cbidentity/init(name:authority:).md)
  Returns the identity object with the given name from the specified identity authority.
- [init?(persistentReference: Data)](cbidentity/init(persistentreference:).md)
  Returns the identity object matching the persistent reference data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/collaboration/cbidentity/init(uuidstring:authority:))*