# LowLevelArgumentTable.Descriptor

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

The buffer and texture slot configuration for an argument table.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct Descriptor
```

## Topics

### Specifying resources
- [var buffers: [LowLevelArgumentTable.Descriptor.Buffer]](./descriptor-swift.struct/buffers.md)
  The ordered list of buffer slots in this table.
- [LowLevelArgumentTable.Descriptor.Buffer](./descriptor-swift.struct/buffer.md)
  A buffer slot descriptor in an argument table.
- [var textures: [LowLevelArgumentTable.Descriptor.Texture]](./descriptor-swift.struct/textures.md)
  The ordered list of texture slots in this table.
- [LowLevelArgumentTable.Descriptor.Texture](./descriptor-swift.struct/texture.md)
  A texture slot descriptor in an argument table.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Inspecting the table
- [var descriptor: LowLevelArgumentTable.Descriptor](./descriptor-swift.property.md)
  The descriptor that describes the buffer and texture slots of this argument table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelargumenttable/descriptor-swift.struct)*