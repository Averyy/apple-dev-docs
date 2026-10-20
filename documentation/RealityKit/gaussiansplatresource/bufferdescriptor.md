# GaussianSplatResource.BufferDescriptor

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

A description of where one per-splat property lives within a buffer.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct BufferDescriptor
```

#### Overview

Express the stride and offset in bytes. The framework finds the value for each splat by starting at the offset and advancing one stride per splat.

## Topics

### Initializers
- [init(buffer: LowLevelBuffer, format: MTLAttributeFormat, stride: Int, offset: Int)](./bufferdescriptor/init%28buffer,format,stride,offset%29.md)
  Creates a descriptor that locates a property within a buffer.
### Instance Properties
- [let buffer: LowLevelBuffer](./bufferdescriptor/buffer.md)
  The buffer that stores the property’s values.
- [let format: MTLAttributeFormat](./bufferdescriptor/format.md)
  The element format of each value in the buffer.
- [let offset: Int](./bufferdescriptor/offset.md)
  The byte offset of the first splat’s value within the buffer.
- [let stride: Int](./bufferdescriptor/stride.md)
  The distance, in bytes, between consecutive splats’ values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/gaussiansplatresource/bufferdescriptor)*