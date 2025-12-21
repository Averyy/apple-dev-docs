# PhysicsPrismaticJoint

**Framework**: RealityKit  
**Kind**: struct

A joint that allows movement along a straight line, similar to a sliding drawer.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
struct PhysicsPrismaticJoint
```

#### Overview

`PhysicsPrismaticJoint`, also called a “slider joint”, allows one linear degree of freedom along the x-axis between two [`Entity`](entity.md) pins.

> 💡 **Tip**: Pass an orientation when creating the [`GeometricPin`](geometricpin.md) instances to change the axis of rotation.

## Topics

### Initializers
- [init(pin0: GeometricPin, pin1: GeometricPin, linearLimit: ClosedRange<Float>?, checksForInternalCollisions: Bool)](physicsprismaticjoint/init(pin0:pin1:linearlimit:checksforinternalcollisions:).md)
  Creates a new prismatic joint.
### Instance Properties
- [var linearLimit: ClosedRange<Float>?](physicsprismaticjoint/linearlimit.md)
  A limit of the translation between the pins in the direction of the x-axis.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [PhysicsJoint](physicsjoint.md)

## See Also

- [struct PhysicsRevoluteJoint](physicsrevolutejoint.md)
  A joint that allows one degree of rotational freedom between two entity pins, similar to a door swinging on its hinges.
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

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicsprismaticjoint)*