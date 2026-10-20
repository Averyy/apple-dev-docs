# PlaneAnchor.Geometry

**Framework**: ARKit  
**Kind**: struct  
**Role**: Structure

The geometry of a plane anchor.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
struct Geometry
```

## Topics

### Inspecting plane geometry
- [var meshFaces: GeometryElement](./geometry-swift.struct/meshfaces.md)
  The faces in the mesh that describes a plane.
- [var meshVertices: GeometrySource](./geometry-swift.struct/meshvertices.md)
  The vertices in the mesh that describes a plane.
- [var extent: PlaneAnchor.Geometry.Extent](./geometry-swift.struct/extent-swift.property.md)
  The size of a plane.
- [PlaneAnchor.Geometry.Extent](./geometry-swift.struct/extent-swift.struct.md)
  The size of a plane.
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

### Getting the shape of a plane anchor
- [var geometry: PlaneAnchor.Geometry](./geometry-swift.property.md)
  Get the geometry of the plane in the anchor’s coordinate system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/planeanchor/geometry-swift.struct)*