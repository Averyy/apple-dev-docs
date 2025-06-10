# TossableRepresentation.TetrahedronFace

**Framework**: TabletopKit  
**Kind**: enum

One of the faces of a tetrahedron

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
enum TetrahedronFace
```

## Topics

### Enumeration Cases
- [TossableRepresentation.TetrahedronFace.a](tossablerepresentation/tetrahedronface/a.md)
- [TossableRepresentation.TetrahedronFace.b](tossablerepresentation/tetrahedronface/b.md)
- [TossableRepresentation.TetrahedronFace.c](tossablerepresentation/tetrahedronface/c.md)
- [TossableRepresentation.TetrahedronFace.d](tossablerepresentation/tetrahedronface/d.md)
### Initializers
- [init(restingOrientation: Rotation3D)](tossablerepresentation/tetrahedronface/init(restingorientation:).md)
  Constructs the face in contact with the table when the equipment has the given resting orientation. If the resting orientation is an unexpected rotation, constructs the face corresponding to the closest expected orientation.
### Instance Properties
- [var restingOrientation: Rotation3D](tossablerepresentation/tetrahedronface/restingorientation.md)
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tossablerepresentation/tetrahedronface)*