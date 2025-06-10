# GeometrySource

**Framework**: ARKit  
**Kind**: struct

A container for geometrical vector data.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
struct GeometrySource
```

#### Overview

Mesh-anchor geometry ([`MeshDescriptor`](https://developer.apple.com/documentation/RealityKit/MeshDescriptor)) uses geometry sources to hold 3D data like vertices and normals in an efficent, array-like format. A Metal buffer wraps the data and other properties specify how to interpret that data.

If [`componentsPerVector`](geometrysource/componentspervector.md) is greater than one, the element type of the geometry-source array is itself a sequence (pairs, triplets, and so on).

## Topics

### Inspecting geometry data
- [var buffer: any MTLBuffer](geometrysource/buffer.md)
  A Metal buffer that contains per-vector data for a geometry source.
- [var count: Int](geometrysource/count.md)
  The number of vectors in a geometry source.
- [var format: MTLVertexFormat](geometrysource/format.md)
  The vertex format for data in a geometry source’s buffer.
- [var componentsPerVector: Int](geometrysource/componentspervector.md)
  The number of scalar components in each vector in a geometry source.
- [var offset: Int](geometrysource/offset.md)
  The offset, in bytes, from the beginning of a geometry source’s buffer.
- [var stride: Int](geometrysource/stride.md)
  The number of bytes between one vector and another in a geometry source’s buffer.
- [var description: String](geometrysource/description.md)
  A textual representation of this geometry source.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct GeometryElement](geometryelement.md)
  A container for vertex indices of lines or triangles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/geometrysource)*