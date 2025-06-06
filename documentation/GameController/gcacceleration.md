# GCAcceleration

**Framework**: Game Controller  
**Kind**: struct

A three-dimensional acceleration vector.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
struct GCAcceleration
```

## Topics

### Getting Acceleration Values
- [var x: Double](gcacceleration/x.md)
  The acceleration measurement along the x-axis, in multiples of earth’s gravity.
- [var y: Double](gcacceleration/y.md)
  The acceleration measurement along the y-axis, in multiples of earth’s gravity.
- [var z: Double](gcacceleration/z.md)
  The acceleration measurement along the z-axis, in multiples of earth’s gravity.
### Initializers
- [init()](gcacceleration/init.md)
  Creates an acceleration structure.
- [init(x: Double, y: Double, z: Double)](gcacceleration/init(x:y:z:).md)
  Creates an acceleration structure with the specified values.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var acceleration: GCAcceleration](gcmotion/acceleration.md)
  The total acceleration of the controller that includes gravity and the acceleration the user applies to the controller.
- [var gravity: GCAcceleration](gcmotion/gravity.md)
  The gravity acceleration vector from the controller’s reference frame.
- [var userAcceleration: GCAcceleration](gcmotion/useracceleration.md)
  The acceleration that the user applies to the controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcacceleration)*