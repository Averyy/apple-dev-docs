# TossableRepresentation.IcosahedronFace

**Framework**: TabletopKit  
**Kind**: enum

One of the faces of an icosahedron

**Availability**:
- visionOS 26.0+

## Declaration

```swift
enum IcosahedronFace
```

## Topics

### Faces
- [TossableRepresentation.IcosahedronFace.a](tossablerepresentation/icosahedronface/a.md)
- [TossableRepresentation.IcosahedronFace.b](tossablerepresentation/icosahedronface/b.md)
- [TossableRepresentation.IcosahedronFace.c](tossablerepresentation/icosahedronface/c.md)
- [TossableRepresentation.IcosahedronFace.d](tossablerepresentation/icosahedronface/d.md)
- [TossableRepresentation.IcosahedronFace.e](tossablerepresentation/icosahedronface/e.md)
- [TossableRepresentation.IcosahedronFace.f](tossablerepresentation/icosahedronface/f.md)
- [TossableRepresentation.IcosahedronFace.g](tossablerepresentation/icosahedronface/g.md)
- [TossableRepresentation.IcosahedronFace.h](tossablerepresentation/icosahedronface/h.md)
- [TossableRepresentation.IcosahedronFace.i](tossablerepresentation/icosahedronface/i.md)
- [TossableRepresentation.IcosahedronFace.j](tossablerepresentation/icosahedronface/j.md)
- [TossableRepresentation.IcosahedronFace.k](tossablerepresentation/icosahedronface/k.md)
- [TossableRepresentation.IcosahedronFace.l](tossablerepresentation/icosahedronface/l.md)
- [TossableRepresentation.IcosahedronFace.m](tossablerepresentation/icosahedronface/m.md)
- [TossableRepresentation.IcosahedronFace.n](tossablerepresentation/icosahedronface/n.md)
- [TossableRepresentation.IcosahedronFace.o](tossablerepresentation/icosahedronface/o.md)
- [TossableRepresentation.IcosahedronFace.p](tossablerepresentation/icosahedronface/p.md)
- [TossableRepresentation.IcosahedronFace.q](tossablerepresentation/icosahedronface/q.md)
- [TossableRepresentation.IcosahedronFace.r](tossablerepresentation/icosahedronface/r.md)
- [TossableRepresentation.IcosahedronFace.s](tossablerepresentation/icosahedronface/s.md)
- [TossableRepresentation.IcosahedronFace.t](tossablerepresentation/icosahedronface/t.md)
### Creating a face
- [init(restingOrientation: Rotation3D)](tossablerepresentation/icosahedronface/init(restingorientation:).md)
  Constructs the face in contact with the table when the equipment has the given resting orientation. If the resting orientation is an unexpected rotation, constructs the face corresponding to the closest expected orientation.
### Getting the resting orientation
- [var restingOrientation: Rotation3D](tossablerepresentation/icosahedronface/restingorientation.md)
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
- [TossableRepresentation.OctahedronFace](tossablerepresentation/octahedronface.md)
  One of the faces of an octahedron
- [TossableRepresentation.TetrahedronFace](tossablerepresentation/tetrahedronface.md)
  One of the faces of a tetrahedron


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tossablerepresentation/icosahedronface)*