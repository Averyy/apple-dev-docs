# TossableRepresentation.CubeFace

**Framework**: TabletopKit  
**Kind**: enum

One of the faces of a cube

**Availability**:
- visionOS 26.0+

## Declaration

```swift
enum CubeFace
```

## Topics

### Faces
- [TossableRepresentation.CubeFace.a](tossablerepresentation/cubeface/a.md)
- [TossableRepresentation.CubeFace.b](tossablerepresentation/cubeface/b.md)
- [TossableRepresentation.CubeFace.c](tossablerepresentation/cubeface/c.md)
- [TossableRepresentation.CubeFace.d](tossablerepresentation/cubeface/d.md)
- [TossableRepresentation.CubeFace.e](tossablerepresentation/cubeface/e.md)
- [TossableRepresentation.CubeFace.f](tossablerepresentation/cubeface/f.md)
### Creating a face
- [init(restingOrientation: Rotation3D)](tossablerepresentation/cubeface/init(restingorientation:).md)
  Constructs the face in contact with the table when the equipment has the given resting orientation. If the resting orientation is an unexpected rotation, constructs the face corresponding to the closest expected orientation.
### Getting the resting orientation
- [var restingOrientation: Rotation3D](tossablerepresentation/cubeface/restingorientation.md)
  Provides the resting orientation for when this face is in contact with the table.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [TossableRepresentation.TossableFace](tossablerepresentation/tossableface.md)

## See Also

- [func face(for: Rotation3D) -> any TossableRepresentation.TossableFace](tossablerepresentation/face(for:).md)
  For the shape corresponding to this tossable representation, constructs the face in contact with the table when the equipment has the given resting orientation.
- [TossableRepresentation.TossableFace](tossablerepresentation/tossableface.md)
  A protocol that represents a face of a tossable shape.
- [TossableRepresentation.SphereFace](tossablerepresentation/sphereface.md)
  An object that represents an infinitely small area on the surface of a sphere (effectively a point).
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

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tossablerepresentation/cubeface)*