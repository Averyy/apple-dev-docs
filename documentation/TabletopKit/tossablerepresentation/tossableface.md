# TossableRepresentation.TossableFace

**Framework**: TabletopKit  
**Kind**: protocol

A protocol that represents a face of a tossable shape.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
protocol TossableFace : RawRepresentable where Self.RawValue == UInt64
```

## Topics

### Creating a tossable face
- [init(restingOrientation: Rotation3D)](tossablerepresentation/tossableface/init(restingorientation:).md)
  Constructs the face in contact with the table when the equipment has the given resting orientation. If the resting orientation is an unexpected rotation, constructs the face corresponding to the closest expected orientation.
### Getting the orientation
- [var restingOrientation: Rotation3D](tossablerepresentation/tossableface/restingorientation.md)
  Provides the resting orientation for when this face is in contact with the table.

## Relationships

### Inherits From
- [RawRepresentable](../Swift/RawRepresentable.md)
### Conforming Types
- [TossableRepresentation.CubeFace](tossablerepresentation/cubeface.md)
- [TossableRepresentation.DecahedronFace](tossablerepresentation/decahedronface.md)
- [TossableRepresentation.DodecahedronFace](tossablerepresentation/dodecahedronface.md)
- [TossableRepresentation.IcosahedronFace](tossablerepresentation/icosahedronface.md)
- [TossableRepresentation.OctahedronFace](tossablerepresentation/octahedronface.md)
- [TossableRepresentation.SphereFace](tossablerepresentation/sphereface.md)
- [TossableRepresentation.TetrahedronFace](tossablerepresentation/tetrahedronface.md)

## See Also

- [func face(for: Rotation3D) -> any TossableRepresentation.TossableFace](tossablerepresentation/face(for:).md)
  For the shape corresponding to this tossable representation, constructs the face in contact with the table when the equipment has the given resting orientation.
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
- [TossableRepresentation.OctahedronFace](tossablerepresentation/octahedronface.md)
  One of the faces of an octahedron
- [TossableRepresentation.TetrahedronFace](tossablerepresentation/tetrahedronface.md)
  One of the faces of a tetrahedron


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tossablerepresentation/tossableface)*