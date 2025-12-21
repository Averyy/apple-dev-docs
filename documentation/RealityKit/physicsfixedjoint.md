# PhysicsFixedJoint

**Framework**: RealityKit  
**Kind**: struct

A joint that rigidly connects two entity pins, with zero degrees of freedom.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
struct PhysicsFixedJoint
```

#### Overview

A fixed joint connects two [`GeometricPin`](geometricpin.md) instances, `pin0` and `pin1`, so that their poses coincide.

There are zero degrees of rotational or linear freedom between the two pins.

## Topics

### Initializers
- [init(pin0: GeometricPin, pin1: GeometricPin)](physicsfixedjoint/init(pin0:pin1:).md)
  Creates a new fixed joint.
### Instance Properties
- [let checksForInternalCollisions: Bool](physicsfixedjoint/checksforinternalcollisions.md)
  A Boolean that indicates whether the joint checks and reports collisions between the two entity instances.

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
- [struct PhysicsDistanceJoint](physicsdistancejoint.md)
  A joint that maintains a minimum and maximum distance between two entity pins.
- [struct PhysicsJoints](physicsjoints.md)
  A collection of physics joints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicsfixedjoint)*