# PhysicsDistanceJoint

**Framework**: RealityKit  
**Kind**: struct

A joint that maintains a minimum and maximum distance between two entity pins.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
struct PhysicsDistanceJoint
```

#### Overview

A distance joint restricts the distance between `pin0` and `pin1`. The joint determines this closed range according to [`distanceLimit`](physicsdistancejoint/distancelimit.md).

This joint allows full rotational freedom between `pin0` and `pin1`.

## Topics

### Initializers
- [init(pin0: GeometricPin, pin1: GeometricPin, distanceLimit: ClosedRange<Float>, checksForInternalCollisions: Bool)](physicsdistancejoint/init(pin0:pin1:distancelimit:checksforinternalcollisions:).md)
  Creates a new distance joint.
### Instance Properties
- [var distanceLimit: ClosedRange<Float>](physicsdistancejoint/distancelimit.md)
  Specifies the minimum and maximum allowed distance between the pins.
- [var tolerance: Float](physicsdistancejoint/tolerance.md)
  An extension of the distance limit, as a percentage-based error tolerance.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [PhysicsJoint](physicsjoint.md)

## See Also

- [struct PhysicsRevoluteJoint](physicsrevolutejoint.md)
  A joint that allows one degree of rotational freedom between two entity pins, similar to a door swinging on its hinges.
- [struct PhysicsPrismaticJoint](physicsprismaticjoint.md)
  A joint that allows movement along a straight line, similar to a sliding drawer.
- [struct PhysicsSphericalJoint](physicssphericaljoint.md)
  A spherical joint that allows free rotational movement between two entities’ pins.
- [struct PhysicsCustomJoint](physicscustomjoint.md)
  A joint with six degrees of freedom that can be individually specified.
- [struct PhysicsFixedJoint](physicsfixedjoint.md)
  A joint that rigidly connects two entity pins, with zero degrees of freedom.
- [struct PhysicsJoints](physicsjoints.md)
  A collection of physics joints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicsdistancejoint)*