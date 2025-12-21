# TossableRepresentation.OctahedronFace

**Framework**: TabletopKit  
**Kind**: enum

One of the faces of an octahedron

**Availability**:
- visionOS 26.0+

## Declaration

```swift
enum OctahedronFace
```

## Topics

### Faces
- [TossableRepresentation.OctahedronFace.a](tossablerepresentation/octahedronface/a.md)
- [TossableRepresentation.OctahedronFace.b](tossablerepresentation/octahedronface/b.md)
- [TossableRepresentation.OctahedronFace.c](tossablerepresentation/octahedronface/c.md)
- [TossableRepresentation.OctahedronFace.d](tossablerepresentation/octahedronface/d.md)
- [TossableRepresentation.OctahedronFace.e](tossablerepresentation/octahedronface/e.md)
- [TossableRepresentation.OctahedronFace.f](tossablerepresentation/octahedronface/f.md)
- [TossableRepresentation.OctahedronFace.g](tossablerepresentation/octahedronface/g.md)
- [TossableRepresentation.OctahedronFace.h](tossablerepresentation/octahedronface/h.md)
### Creating a face
- [init(restingOrientation: Rotation3D)](tossablerepresentation/octahedronface/init(restingorientation:).md)
  Constructs the face in contact with the table when the equipment has the given resting orientation. If the resting orientation is an unexpected rotation, constructs the face corresponding to the closest expected orientation.
### Getting the resting orientation
- [var restingOrientation: Rotation3D](tossablerepresentation/octahedronface/restingorientation.md)
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
- [TossableRepresentation.CubeFace](tossablerepresentation/cubeface.md)
  One of the faces of a cube
- [TossableRepresentation.DecahedronFace](tossablerepresentation/decahedronface.md)
  One of the faces of an decahedron
- [TossableRepresentation.DodecahedronFace](tossablerepresentation/dodecahedronface.md)
  One of the faces of an dodecahedron
- [TossableRepresentation.IcosahedronFace](tossablerepresentation/icosahedronface.md)
  One of the faces of an icosahedron
- [TossableRepresentation.TetrahedronFace](tossablerepresentation/tetrahedronface.md)
  One of the faces of a tetrahedron


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tossablerepresentation/octahedronface)*