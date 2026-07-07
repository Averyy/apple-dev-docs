# GaussianSplatResource.BufferDescriptor

**Framework**: RealityKit  
**Kind**: struct

A description of where one per-splat property lives within a buffer.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct BufferDescriptor
```

#### Overview

Express the stride and offset in bytes. The framework finds the value for each splat by starting at the offset and advancing one stride per splat.

## Topics

### Initializers
- [init(buffer: LowLevelBuffer, format: MTLAttributeFormat, stride: Int, offset: Int)](gaussiansplatresource/bufferdescriptor/init(buffer:format:stride:offset:).md)
  Creates a descriptor that locates a property within a buffer.
### Instance Properties
- [let buffer: LowLevelBuffer](gaussiansplatresource/bufferdescriptor/buffer.md)
  The buffer that stores the property’s values.
- [let format: MTLAttributeFormat](gaussiansplatresource/bufferdescriptor/format.md)
  The element format of each value in the buffer.
- [let offset: Int](gaussiansplatresource/bufferdescriptor/offset.md)
  The byte offset of the first splat’s value within the buffer.
- [let stride: Int](gaussiansplatresource/bufferdescriptor/stride.md)
  The distance, in bytes, between consecutive splats’ values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/gaussiansplatresource/bufferdescriptor)*