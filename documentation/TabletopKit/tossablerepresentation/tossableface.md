# TossableRepresentation.TossableFace

**Framework**: TabletopKit  
**Kind**: protocol  
**Role**: Protocol

A protocol that represents a face of a tossable shape.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
protocol TossableFace : RawRepresentable where Self.RawValue == UInt64
```

## Topics

### Creating a tossable face
- [init(restingOrientation: Rotation3D)](./tossableface/init%28restingorientation%29.md)
  Constructs the face in contact with the table when the equipment has the given resting orientation. If the resting orientation is an unexpected rotation, constructs the face corresponding to the closest expected orientation.
### Getting the orientation
- [var restingOrientation: Rotation3D](./tossableface/restingorientation.md)
  Provides the resting orientation for when this face is in contact with the table.

## Relationships

### Inherits From
- [RawRepresentable](../../Swift/rawrepresentable.md)
### Conforming Types
- [TossableRepresentation.CubeFace](./cubeface.md)
- [TossableRepresentation.DecahedronFace](./decahedronface.md)
- [TossableRepresentation.DodecahedronFace](./dodecahedronface.md)
- [TossableRepresentation.IcosahedronFace](./icosahedronface.md)
- [TossableRepresentation.OctahedronFace](./octahedronface.md)
- [TossableRepresentation.SphereFace](./sphereface.md)
- [TossableRepresentation.TetrahedronFace](./tetrahedronface.md)

## See Also

### Getting the face
- [func face(for: Rotation3D) -> any TossableRepresentation.TossableFace](./face%28for%29.md)
  For the shape corresponding to this tossable representation, constructs the face in contact with the table when the equipment has the given resting orientation.
- [TossableRepresentation.SphereFace](./sphereface.md)
  An object that represents an infinitely small area on the surface of a sphere (effectively a point).
- [TossableRepresentation.CubeFace](./cubeface.md)
  One of the faces of a cube
- [TossableRepresentation.DecahedronFace](./decahedronface.md)
  One of the faces of an decahedron
- [TossableRepresentation.DodecahedronFace](./dodecahedronface.md)
  One of the faces of an dodecahedron
- [TossableRepresentation.IcosahedronFace](./icosahedronface.md)
  One of the faces of an icosahedron
- [TossableRepresentation.OctahedronFace](./octahedronface.md)
  One of the faces of an octahedron
- [TossableRepresentation.TetrahedronFace](./tetrahedronface.md)
  One of the faces of a tetrahedron


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tossablerepresentation/tossableface)*