# init(persistentReference:)

**Framework**: Collaboration  
**Kind**: init

Returns the identity object matching the persistent reference data.

**Availability**:
- macOS 10.5+

## Declaration

```swift
init?(persistentReference data: Data)
```

#### Return Value

The identity object matching the persistent data object, or `nil` if the identity is not found.

#### Discussion

A persistent reference is an opaque data object suitable for persistent storage.

## Parameters

- `data`: The persistent data object that refers to an identity.

## See Also

- [init?(name: String, authority: CBIdentityAuthority)](cbidentity/init(name:authority:).md)
  Returns the identity object with the given name from the specified identity authority.
- [init?(uuidString: String, authority: CBIdentityAuthority)](cbidentity/init(uuidstring:authority:).md)
  Returns the identity object with the given UUID from the specified identity authority.


---

*[View on Apple Developer](https://developer.apple.com/documentation/collaboration/cbidentity/init(persistentreference:))*