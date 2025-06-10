# TossableRepresentation.SphereFace

**Framework**: TabletopKit  
**Kind**: struct

An object that represents an infinitely small area on the surface of a sphere (effectively a point).

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct SphereFace
```

## Topics

### Initializers
- [init(latitude: Angle2D, longitude: Angle2D)](tossablerepresentation/sphereface/init(latitude:longitude:).md)
- [init(restingOrientation: Rotation3D)](tossablerepresentation/sphereface/init(restingorientation:).md)
  Constructs the face in contact with the table when the equipment has the given resting orientation. If the resting orientation is an unexpected rotation, constructs the face corresponding to the closest expected orientation.
### Instance Properties
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tossablerepresentation/sphereface)*