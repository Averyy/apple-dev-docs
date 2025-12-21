# TossableRepresentation.DecahedronFace

**Framework**: TabletopKit  
**Kind**: enum

One of the faces of an decahedron

**Availability**:
- visionOS 26.0+

## Declaration

```swift
enum DecahedronFace
```

## Topics

### Faces
- [TossableRepresentation.DecahedronFace.a](tossablerepresentation/decahedronface/a.md)
- [TossableRepresentation.DecahedronFace.b](tossablerepresentation/decahedronface/b.md)
- [TossableRepresentation.DecahedronFace.c](tossablerepresentation/decahedronface/c.md)
- [TossableRepresentation.DecahedronFace.d](tossablerepresentation/decahedronface/d.md)
- [TossableRepresentation.DecahedronFace.e](tossablerepresentation/decahedronface/e.md)
- [TossableRepresentation.DecahedronFace.f](tossablerepresentation/decahedronface/f.md)
- [TossableRepresentation.DecahedronFace.g](tossablerepresentation/decahedronface/g.md)
- [TossableRepresentation.DecahedronFace.h](tossablerepresentation/decahedronface/h.md)
- [TossableRepresentation.DecahedronFace.i](tossablerepresentation/decahedronface/i.md)
- [TossableRepresentation.DecahedronFace.j](tossablerepresentation/decahedronface/j.md)
### Creating a face
- [init(restingOrientation: Rotation3D)](tossablerepresentation/decahedronface/init(restingorientation:).md)
  Constructs the face in contact with the table when the equipment has the given resting orientation. If the resting orientation is an unexpected rotation, constructs the face corresponding to the closest expected orientation.
### Getting the resting orientation
- [var restingOrientation: Rotation3D](tossablerepresentation/decahedronface/restingorientation.md)
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
- [TossableRepresentation.DodecahedronFace](tossablerepresentation/dodecahedronface.md)
  One of the faces of an dodecahedron
- [TossableRepresentation.IcosahedronFace](tossablerepresentation/icosahedronface.md)
  One of the faces of an icosahedron
- [TossableRepresentation.OctahedronFace](tossablerepresentation/octahedronface.md)
  One of the faces of an octahedron
- [TossableRepresentation.TetrahedronFace](tossablerepresentation/tetrahedronface.md)
  One of the faces of a tetrahedron


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tossablerepresentation/decahedronface)*