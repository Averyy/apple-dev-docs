# PhysicsSphericalJoint

**Framework**: RealityKit  
**Kind**: struct

A spherical joint that allows free rotational movement between two entities’ pins.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
struct PhysicsSphericalJoint
```

#### Overview

This joint has three rotational degrees of freedom and removes all translational degrees of freedom by making the positions of `pin0` and `pin1` coincide. This is also called a “ball-socket joint”.

To add limits to the rotational freedom of `pin1`, define a tuple value for [`angularLimitInYZ`](physicssphericaljoint/angularlimitinyz.md). This tuple defines an elliptical cone shape around the x-axis of `pin0`, which limits the rotational freedom of `pin1`. The rotation around the x-axis is never limited with this joint.

> 💡 **Tip**: Pass an orientation when creating the [`GeometricPin`](geometricpin.md) instances to change the axis of rotation.

## Topics

### Initializers
- [init(pin0: GeometricPin, pin1: GeometricPin, angularLimitInYZ: (Float, Float)?, checksForInternalCollisions: Bool)](physicssphericaljoint/init(pin0:pin1:angularlimitinyz:checksforinternalcollisions:).md)
  Creates a new spherical joint.
### Instance Properties
- [var angularLimitInYZ: (Float, Float)?](physicssphericaljoint/angularlimitinyz.md)
  A cone-shaped limit of rotational freedom.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [PhysicsJoint](physicsjoint.md)

## See Also

- [struct PhysicsRevoluteJoint](physicsrevolutejoint.md)
  A joint that allows one degree of rotational freedom between two entity pins, similar to a door swinging on its hinges.
- [struct PhysicsPrismaticJoint](physicsprismaticjoint.md)
  A joint that allows movement along a straight line, similar to a sliding drawer.
- [struct PhysicsCustomJoint](physicscustomjoint.md)
  A joint with six degrees of freedom that can be individually specified.
- [struct PhysicsDistanceJoint](physicsdistancejoint.md)
  A joint that maintains a minimum and maximum distance between two entity pins.
- [struct PhysicsFixedJoint](physicsfixedjoint.md)
  A joint that rigidly connects two entity pins, with zero degrees of freedom.
- [struct PhysicsJoints](physicsjoints.md)
  A collection of physics joints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicssphericaljoint)*