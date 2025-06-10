# TossableRepresentation.TossableFace

**Framework**: TabletopKit  
**Kind**: protocol

A protocol that represents a face of a tossable shape.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
protocol TossableFace : RawRepresentable where Self.RawValue == UInt64
```

## Topics

### Initializers
- [init(restingOrientation: Rotation3D)](tossablerepresentation/tossableface/init(restingorientation:).md)
  Constructs the face in contact with the table when the equipment has the given resting orientation. If the resting orientation is an unexpected rotation, constructs the face corresponding to the closest expected orientation.
### Instance Properties
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tossablerepresentation/tossableface)*