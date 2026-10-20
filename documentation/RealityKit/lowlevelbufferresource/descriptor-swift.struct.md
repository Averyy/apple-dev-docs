# LowLevelBufferResource.Descriptor

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

The capacity and alignment requirements for a buffer resource.

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

### Creating a descriptor
- [init(capacity: Int, sizeMultiple: Int)](./descriptor-swift.struct/init%28capacity,sizemultiple%29.md)
  Creates a buffer descriptor with the given capacity and size alignment.
### Configuring the buffer size
- [var capacity: Int](./descriptor-swift.struct/capacity.md)
  The capacity of the buffer, in bytes.
- [var sizeMultiple: Int](./descriptor-swift.struct/sizemultiple.md)
  The required alignment of the buffer’s size, in bytes.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Inspecting the descriptor
- [var descriptor: LowLevelBufferResource.Descriptor](./descriptor-swift.property.md)
  The descriptor used to create this buffer resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelbufferresource/descriptor-swift.struct)*