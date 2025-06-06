# LowLevelMesh.Layout

**Framework**: RealityKit  
**Kind**: struct

An object that describes a set of attributes that share a buffer index, offset, and stride.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
struct Layout
```

#### Overview

Applications typically express their types using contiguous or interleaved (strided) memory.

If you interleave your data (meaning that you represent it with a structure), use one `Layout` object where [`bufferStride`](lowlevelmesh/layout/bufferstride.md) is equal to `MemoryLayout<Type>.stride()`.

If you store your attributes separately, use one `Layout` per attribute.

## Topics

### Creating a low-level mesh layout
- [init(bufferIndex: Int, bufferOffset: Int, bufferStride: Int)](lowlevelmesh/layout/init(bufferindex:bufferoffset:bufferstride:).md)
### Describing a low-level mesh layout
- [var bufferIndex: Int](lowlevelmesh/layout/bufferindex.md)
  The index of the buffer to use for this layout.
- [var bufferOffset: Int](lowlevelmesh/layout/bufferoffset.md)
  The byte offset into the buffer for the first byte of this layout.
- [var bufferStride: Int](lowlevelmesh/layout/bufferstride.md)
  The distance, in bytes, between consecutive vertices for attributes using this layout.

## See Also

- [Creating a spatial drawing app with RealityKit](creating-a-spatial-drawing-app-with-realitykit.md)
  Use low-level mesh and texture APIs to achieve fast updates to a person’s brush strokes by integrating RealityKit with ARKit and SwiftUI.
- [Creating a plane with low-level mesh](creating-a-plane-with-low-level-mesh.md)
  Create a low-level mesh and set its vertex positions and normals to form a plane.
- [class LowLevelMesh](lowlevelmesh.md)
  A container for vertex data that you can use to create and update meshes using your own format.
- [LowLevelMesh.Descriptor](lowlevelmesh/descriptor-swift.struct.md)
  An object that describes the data format and layout of the buffers in a low-level mesh.
- [LowLevelMesh.Part](lowlevelmesh/part.md)
  An object that describes a range of primitives to display, and their material index.
- [LowLevelMesh.Attribute](lowlevelmesh/attribute.md)
  An object that determines how to store vertex attribute data in memory and map it to RealityKit shader attributes.
- [LowLevelMesh.VertexSemantic](lowlevelmesh/vertexsemantic.md)
  Designates the intended usage of a vertex attribute.
- [LowLevelMesh.PartsCollection](lowlevelmesh/partscollection.md)
  An object that holds a mutable collection low-level mesh parts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmesh/layout)*