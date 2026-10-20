# init(uuid:)

**Framework**: FSKit  
**Kind**: init  
**Role**: Initializer

Creates an entity identifier with the given UUID.

**Availability**:
- macOS 15.4+

## Declaration

```swift
init(uuid: UUID)
```

```objc
- (instancetype) initWithUUID:(NSUUID *) uuid;
```

## Parameters

- `uuid`: The UUID to use for this identifier.

## See Also

### Creating an entity identifier
- [init()](./init%28%29.md)
  Creates an entity identifier with a random UUID.
- [init(uuid: UUID, data: Data)](./init%28uuid,data%29-8dixs.md)
  Creates an entity identifier with the given UUID and qualifier data.
- [init(uuid: UUID, qualifier: UInt64)](./init%28uuid,qualifier%29-9ty70.md)
  Creates an entity identifier with the given UUID and qualifier data as a 64-bit unsigned integer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsentityidentifier/init(uuid:)-9e20k)*