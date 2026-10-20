# LowLevelBuffer.Descriptor

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct Descriptor
```

## Topics

### Initializers
- [init(capacity: Int, sizeMultiple: Int)](./descriptor-swift.struct/init%28capacity,sizemultiple%29.md)
### Instance Properties
- [var capacity: Int](./descriptor-swift.struct/capacity.md)
  Length of the buffer in bytes.
- [var sizeMultiple: Int](./descriptor-swift.struct/sizemultiple.md)
  For variable length buffers, bytesUsed needs to be a multiple of this value.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelbuffer/descriptor-swift.struct)*