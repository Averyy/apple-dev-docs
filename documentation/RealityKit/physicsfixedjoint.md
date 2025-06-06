# PhysicsFixedJoint

**Framework**: RealityKit  
**Kind**: struct

A joint that rigidly connects two entity pins, with zero degrees of freedom.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
struct PhysicsFixedJoint
```

#### Overview

A fixed joint connects two [`GeometricPin`](geometricpin.md) instances, [`pin0`](physicsfixedjoint/pin0.md) and [`pin1`](physicsfixedjoint/pin1.md), so that their poses coincide.

There are zero degrees of rotational or linear freedom between the two pins.

## Topics

### Operators
- [static func == (PhysicsFixedJoint, PhysicsFixedJoint) -> Bool](physicsfixedjoint/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Initializers
- [init(pin0: GeometricPin, pin1: GeometricPin)](physicsfixedjoint/init(pin0:pin1:).md)
  Creates a new fixed joint.
### Instance Properties
- [let checksForInternalCollisions: Bool](physicsfixedjoint/checksforinternalcollisions.md)
  A Boolean that indicates whether the joint checks and reports collisions between the two entity instances.
- [var isActive: Bool](physicsfixedjoint/isactive.md)
  A Boolean that indicates whether the joint is active.
- [var pin0: GeometricPin](physicsfixedjoint/pin0.md)
  The pin that defines a local position and orientation on the first entity.
- [var pin1: GeometricPin](physicsfixedjoint/pin1.md)
  The pin that defines a local position and orientation on the second entity.
### Default Implementations
- [Equatable Implementations](physicsfixedjoint/equatable-implementations.md)
- [PhysicsJoint Implementations](physicsfixedjoint/physicsjoint-implementations.md)

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