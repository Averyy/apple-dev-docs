# PlaneAnchor.Geometry.Extent

**Framework**: ARKit  
**Kind**: struct  
**Role**: Structure

The size of a plane.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
struct Extent
```

## Topics

### Inspecting a plane extent
- [var width: Float](./extent-swift.struct/width.md)
  The width of a plane.
- [var height: Float](./extent-swift.struct/height.md)
  The height of a plane.
- [var anchorFromExtentTransform: simd_float4x4](./extent-swift.struct/anchorfromextenttransform.md)
  The transform from the plane extent to the plane anchor’s coordinate system.
### Instance Properties
- [var description: String](./extent-swift.struct/description.md)
  A textual representation of this extent.
### Default Implementations
- [Equatable Implementations](./extent-swift.struct/equatable-implementations.md)

## Relationships

### Conforms To
- [CustomStringConvertible](../../../Swift/customstringconvertible.md)
- [Equatable](../../../Swift/equatable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Inspecting plane geometry
- [var meshFaces: GeometryElement](./meshfaces.md)
  The faces in the mesh that describes a plane.
- [var meshVertices: GeometrySource](./meshvertices.md)
  The vertices in the mesh that describes a plane.
- [var extent: PlaneAnchor.Geometry.Extent](./extent-swift.property.md)
  The size of a plane.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/planeanchor/geometry-swift.struct/extent-swift.struct)*