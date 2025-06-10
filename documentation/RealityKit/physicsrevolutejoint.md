# PhysicsRevoluteJoint

**Framework**: RealityKit  
**Kind**: struct

A joint that allows one degree of rotational freedom between two entity pins, similar to a door swinging on its hinges.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
struct PhysicsRevoluteJoint
```

#### Overview

`PhysicsRevoluteJoint` allows one rotational degree of freedom along the x-axis of two entity pins.

> 💡 **Tip**: Pass an orientation when creating the [`GeometricPin`](geometricpin.md) instances to change the axis of rotation.

## Topics

### Initializers
- [init(pin0: GeometricPin, pin1: GeometricPin, angularLimit: ClosedRange<Float>?, checksForInternalCollisions: Bool)](physicsrevolutejoint/init(pin0:pin1:angularlimit:checksforinternalcollisions:).md)
  Creates a new revolute joint.
### Instance Properties
- [var angularLimit: ClosedRange<Float>?](physicsrevolutejoint/angularlimit.md)
  A limit of the rotational freedom between the pins around the x-axis.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [PhysicsJoint](physicsjoint.md)

## See Also

- [struct PhysicsPrismaticJoint](physicsprismaticjoint.md)
  A joint that allows movement along a straight line, similar to a sliding drawer.
- [struct PhysicsSphericalJoint](physicssphericaljoint.md)
  A spherical joint that allows free rotational movement between two entities’ pins.
- [struct PhysicsCustomJoint](physicscustomjoint.md)
  A joint with six degrees of freedom that can be individually specified.
- [struct PhysicsDistanceJoint](physicsdistancejoint.md)
  A joint that maintains a minimum and maximum distance between two entity pins.
- [struct PhysicsFixedJoint](physicsfixedjoint.md)
  A joint that rigidly connects two entity pins, with zero degrees of freedom.
- [struct PhysicsJoints](physicsjoints.md)
  A collection of physics joints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicsrevolutejoint)*