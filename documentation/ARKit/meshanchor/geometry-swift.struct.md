# MeshAnchor.Geometry

**Framework**: ARKit  
**Kind**: struct  
**Role**: Structure

The shapes that make up a mesh anchor.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
struct Geometry
```

## Topics

### Inspecting mesh geometry
- [var faces: GeometryElement](./geometry-swift.struct/faces.md)
  The faces of the mesh.
- [var vertices: GeometrySource](./geometry-swift.struct/vertices.md)
  The vertices of the mesh.
- [var normals: GeometrySource](./geometry-swift.struct/normals.md)
  The normals of the mesh.
- [var classifications: GeometrySource?](./geometry-swift.struct/classifications.md)
  The classification of each face in the mesh.
### Instance Properties
- [var description: String](./geometry-swift.struct/description.md)
  A textual representation of this geometry.
### Default Implementations
- [Equatable Implementations](./geometry-swift.struct/equatable-implementations.md)

## Relationships

### Conforms To
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting mesh information
- [var originFromAnchorTransform: simd_float4x4](./originfromanchortransform.md)
  The location and orientation of a mesh in world space.
- [var geometry: MeshAnchor.Geometry](./geometry-swift.property.md)
  The shape of a mesh anchor.
- [MeshAnchor.MeshClassification](./meshclassification.md)
  The kinds of classification a face of a mesh can have.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/meshanchor/geometry-swift.struct)*