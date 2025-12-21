# TossableRepresentation.SphereFace

**Framework**: TabletopKit  
**Kind**: struct

An object that represents an infinitely small area on the surface of a sphere (effectively a point).

**Availability**:
- visionOS 26.0+

## Declaration

```swift
struct SphereFace
```

## Topics

### Creating a sphere face
- [init(latitude: Angle2D, longitude: Angle2D)](tossablerepresentation/sphereface/init(latitude:longitude:).md)
- [init(restingOrientation: Rotation3D)](tossablerepresentation/sphereface/init(restingorientation:).md)
  Constructs the face in contact with the table when the equipment has the given resting orientation. If the resting orientation is an unexpected rotation, constructs the face corresponding to the closest expected orientation.
### Getting the sphere face properties
- [var latitude: Angle2D](tossablerepresentation/sphereface/latitude.md)
- [var longitude: Angle2D](tossablerepresentation/sphereface/longitude.md)
- [var restingOrientation: Rotation3D](tossablerepresentation/sphereface/restingorientation.md)
  Provides the resting orientation for when this face is in contact with the table.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [TossableRepresentation.TossableFace](tossablerepresentation/tossableface.md)

## See Also

- [func face(for: Rotation3D) -> any TossableRepresentation.TossableFace](tossablerepresentation/face(for:).md)
  For the shape corresponding to this tossable representation, constructs the face in contact with the table when the equipment has the given resting orientation.
- [TossableRepresentation.TossableFace](tossablerepresentation/tossableface.md)
  A protocol that represents a face of a tossable shape.
- [TossableRepresentation.CubeFace](tossablerepresentation/cubeface.md)
  One of the faces of a cube
- [TossableRepresentation.DecahedronFace](tossablerepresentation/decahedronface.md)
  One of the faces of an decahedron
- [TossableRepresentation.DodecahedronFace](tossablerepresentation/dodecahedronface.md)
  One of the faces of an dodecahedron
- [TossableRepresentation.IcosahedronFace](tossablerepresentation/icosahedronface.md)
  One of the faces of an icosahedron
- [TossableRepresentation.OctahedronFace](tossablerepresentation/octahedronface.md)
  One of the faces of an octahedron
- [TossableRepresentation.TetrahedronFace](tossablerepresentation/tetrahedronface.md)
  One of the faces of a tetrahedron


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tossablerepresentation/sphereface)*