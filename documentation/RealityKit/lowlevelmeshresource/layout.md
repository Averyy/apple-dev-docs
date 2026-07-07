# LowLevelMeshResource.Layout

**Framework**: RealityKit  
**Kind**: struct

An object that describes a set of attributes that share a buffer index, offset, and stride.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct Layout
```

#### Overview

If you interleave your data (that is, represent it with a structure), use one `Layout` object where `bufferStride` equals `MemoryLayout<Type>.stride`. If you store attributes separately, use one `Layout` per attribute.

## Topics

### Creating a layout
- [init(bufferIndex: Int, bufferOffset: Int, bufferStride: Int, stepFunction: MTLVertexStepFunction, stepRate: Int)](lowlevelmeshresource/layout/init(bufferindex:bufferoffset:bufferstride:stepfunction:steprate:).md)
  Creates a layout with the given buffer index, offset, stride, step function, and step rate.
### Configuring vertex stepping
- [var stepFunction: MTLVertexStepFunction](lowlevelmeshresource/layout/stepfunction.md)
  Determines how the vertex shader steps through the data in this layout.
- [var stepRate: Int](lowlevelmeshresource/layout/steprate.md)
  The number of instances that share the same per-instance vertex data.
### Initializers
- [init()](lowlevelmeshresource/layout/init.md)
  Creates a layout with all fields set to their zero/default values.
### Instance Properties
- [var bufferIndex: Int](lowlevelmeshresource/layout/bufferindex.md)
  The index of the buffer to use for this layout.
- [var bufferOffset: Int](lowlevelmeshresource/layout/bufferoffset.md)
  The byte offset into the buffer for the first byte of this layout.
- [var bufferStride: Int](lowlevelmeshresource/layout/bufferstride.md)
  The distance, in bytes, between consecutive vertices for attributes using this layout.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var descriptor: LowLevelMeshResource.Descriptor](lowlevelmeshresource/descriptor-swift.property.md)
  The descriptor used to create this mesh resource.
- [LowLevelMeshResource.Descriptor](lowlevelmeshresource/descriptor-swift.struct.md)
  An object that describes the data format and layout of the buffers in a low-level mesh.
- [LowLevelMeshResource.Attribute](lowlevelmeshresource/attribute.md)
  An object that determines how to store vertex attribute data in memory and map it to RealityKit custom shader attributes.
- [LowLevelMeshResource.VertexSemantic](lowlevelmeshresource/vertexsemantic.md)
  The intended usage of a vertex attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmeshresource/layout)*