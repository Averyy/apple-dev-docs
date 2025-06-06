# MeshAnchor.Geometry

**Framework**: ARKit  
**Kind**: struct

The shapes that make up a mesh anchor.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
struct Geometry
```

## Topics

### Inspecting mesh geometry
- [var faces: GeometryElement](meshanchor/geometry-swift.struct/faces.md)
  The faces of the mesh.
- [var vertices: GeometrySource](meshanchor/geometry-swift.struct/vertices.md)
  The vertices of the mesh.
- [var normals: GeometrySource](meshanchor/geometry-swift.struct/normals.md)
  The normals of the mesh.
- [var classifications: GeometrySource?](meshanchor/geometry-swift.struct/classifications.md)
  The classification of each face in the mesh.
### Instance Properties
- [var description: String](meshanchor/geometry-swift.struct/description.md)
  A textual representation of this geometry.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var originFromAnchorTransform: simd_float4x4](meshanchor/originfromanchortransform.md)
  The location and orientation of a mesh in world space.
- [var geometry: MeshAnchor.Geometry](meshanchor/geometry-swift.property.md)
  The shape of a mesh anchor.
- [MeshAnchor.MeshClassification](meshanchor/meshclassification.md)
  The kinds of classification a face of a mesh can have.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/meshanchor/geometry-swift.struct)*