# TossableRepresentation.OctahedronFace

**Framework**: TabletopKit  
**Kind**: enum

One of the faces of an octahedron

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
enum OctahedronFace
```

## Topics

### Enumeration Cases
- [TossableRepresentation.OctahedronFace.a](tossablerepresentation/octahedronface/a.md)
- [TossableRepresentation.OctahedronFace.b](tossablerepresentation/octahedronface/b.md)
- [TossableRepresentation.OctahedronFace.c](tossablerepresentation/octahedronface/c.md)
- [TossableRepresentation.OctahedronFace.d](tossablerepresentation/octahedronface/d.md)
- [TossableRepresentation.OctahedronFace.e](tossablerepresentation/octahedronface/e.md)
- [TossableRepresentation.OctahedronFace.f](tossablerepresentation/octahedronface/f.md)
- [TossableRepresentation.OctahedronFace.g](tossablerepresentation/octahedronface/g.md)
- [TossableRepresentation.OctahedronFace.h](tossablerepresentation/octahedronface/h.md)
### Initializers
- [init(restingOrientation: Rotation3D)](tossablerepresentation/octahedronface/init(restingorientation:).md)
  Constructs the face in contact with the table when the equipment has the given resting orientation. If the resting orientation is an unexpected rotation, constructs the face corresponding to the closest expected orientation.
### Instance Properties
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tossablerepresentation/octahedronface)*