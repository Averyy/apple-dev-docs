# init(uuid:qualifier:)

**Framework**: FSKit  
**Kind**: init  
**Role**: Initializer

Creates an entity identifier with the given UUID and qualifier data as a 64-bit unsigned integer.

**Availability**:
- macOS 15.4+

## Declaration

```swift
init(uuid: UUID, qualifier: UInt64)
```

```objc
- (instancetype) initWithUUID:(NSUUID *) uuid qualifier:(uint64_t) qualifier;
```

## Parameters

- `uuid`: The UUID to use for this identifier.
- `qualifier`: The data to distinguish entities that otherwise share the same UUID.

## See Also

### Creating an entity identifier
- [init()](./init%28%29.md)
  Creates an entity identifier with a random UUID.
- [init(uuid: UUID)](./init%28uuid%29-9e20k.md)
  Creates an entity identifier with the given UUID.
- [init(uuid: UUID, data: Data)](./init%28uuid,data%29-8dixs.md)
  Creates an entity identifier with the given UUID and qualifier data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsentityidentifier/init(uuid:qualifier:)-9ty70)*