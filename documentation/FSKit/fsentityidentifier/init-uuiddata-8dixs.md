# init(uuid:data:)

**Framework**: FSKit  
**Kind**: init

Creates an entity identifier with the given UUID and qualifier data.

**Availability**:
- macOS 15.4+

## Declaration

```swift
init(uuid: UUID, data qualifierData: Data)
```

#### Discussion

> ⚠️ **Warning**: This initializer is annotated as returning a non-optional value but silently returns `nil` when `qualifierData` is not exactly eight bytes, which can surface as a null value in a non-optional Swift variable. Use [`init(uuid:qualifierData:)`](fsentityidentifier/init(uuid:qualifierdata:)-8xlg1.md) instead, which is explicitly failable.

## Parameters

- `uuid`: The UUID to use for this identifier.
- `qualifierData`: The data to distinguish entities that otherwise share the same UUID.

## See Also

- [init()](fsentityidentifier/init.md)
  Creates an entity identifier with a random UUID.
- [init(uuid: UUID)](fsentityidentifier/init(uuid:)-9e20k.md)
  Creates an entity identifier with the given UUID.
- [init(uuid: UUID, qualifier: UInt64)](fsentityidentifier/init(uuid:qualifier:)-9ty70.md)
  Creates an entity identifier with the given UUID and qualifier data as a 64-bit unsigned integer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsentityidentifier/init(uuid:data:)-8dixs)*