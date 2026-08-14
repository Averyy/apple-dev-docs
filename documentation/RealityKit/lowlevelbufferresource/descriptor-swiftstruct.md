# LowLevelBufferResource.Descriptor

**Framework**: RealityKit  
**Kind**: struct

The capacity and alignment requirements for a buffer resource.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct Descriptor
```

## Topics

### Creating a descriptor
- [init(capacity: Int, sizeMultiple: Int)](lowlevelbufferresource/descriptor-swift.struct/init(capacity:sizemultiple:).md)
  Creates a buffer descriptor with the given capacity and size alignment.
### Configuring the buffer size
- [var capacity: Int](lowlevelbufferresource/descriptor-swift.struct/capacity.md)
  The capacity of the buffer, in bytes.
- [var sizeMultiple: Int](lowlevelbufferresource/descriptor-swift.struct/sizemultiple.md)
  The required alignment of the buffer’s size, in bytes.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var descriptor: LowLevelBufferResource.Descriptor](lowlevelbufferresource/descriptor-swift.property.md)
  The descriptor used to create this buffer resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelbufferresource/descriptor-swift.struct)*