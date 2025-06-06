# init(uuid:qualifier:)

**Framework**: FSKit  
**Kind**: init

Creates an entity identifier with the given UUID and qualifier data as a 64-bit unsigned integer.

**Availability**:
- macOS 15.4+

## Declaration

```swift
init(uuid: UUID, qualifier: UInt64)
```

## Parameters

- `uuid`: The UUID to use for this identifier.
- `qualifier`: The data to distinguish entities that otherwise share the same UUID.

## See Also

- [init()](fsentityidentifier/init.md)
  Creates an entity identifier with a random UUID.
- [init(uuid: UUID)](fsentityidentifier/init(uuid:).md)
  Creates an entity identifier with the given UUID.
- [init(uuid: UUID, data: Data)](fsentityidentifier/init(uuid:data:).md)
  Creates an entity identifier with the given UUID and qualifier data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsentityidentifier/init(uuid:qualifier:))*