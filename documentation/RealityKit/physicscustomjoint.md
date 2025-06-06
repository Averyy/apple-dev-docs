# PhysicsCustomJoint

**Framework**: Realitykit  
**Kind**: struct

A joint with six degrees of freedom that can be individually specified.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
struct PhysicsCustomJoint
```

#### Overview

A custom joint allows you to choose the restraints of all 6 degrees of freedom. You can set a [`PhysicsCustomJoint.MotionLimit`](physicscustomjoint/motionlimit.md) for each degrees’ motion.

> **Note**: By default all degrees of freedom are locked, similar to [`PhysicsFixedJoint`](physicsfixedjoint.md).

For example, you can constrain the motion of [`pin1`](physicscustomjoint/pin1.md) in the xy-plane of [`pin0`](physicscustomjoint/pin0.md), set movement along the x-axis to [`PhysicsCustomJoint.MotionLimit.unlimited`](physicscustomjoint/motionlimit/unlimited.md), and leave all rotations as the default value of [`PhysicsCustomJoint.MotionLimit.fixed`](physicscustomjoint/motionlimit/fixed.md).

> **Note**: The xy-plane is a plane that aligns with the x and y axes.

```swift
let joint = PhysicsCustomJoint(
    pin0: entity0pin,
    pin1: entity1pin,
    linearMotionAlongX: .unlimited,
    linearMotionAlongY: .range(-5...5)
)
```

If [`pin0`](physicscustomjoint/pin0.md) is in a fixed location for the example above, this joint allows [`pin1`](physicscustomjoint/pin1.md) to move anywhere along the x-axis of [`pin0`](physicscustomjoint/pin0.md), and can move up to 5 local meters above or below the y-axis of [`pin0`](physicscustomjoint/pin0.md).

## Topics

### Operators
- [static func == (PhysicsCustomJoint, PhysicsCustomJoint) -> Bool](physicscustomjoint/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Initializers
- [init(pin0: GeometricPin, pin1: GeometricPin, linearMotionAlongX: PhysicsCustomJoint.MotionLimit, linearMotionAlongY: PhysicsCustomJoint.MotionLimit, linearMotionAlongZ: PhysicsCustomJoint.MotionLimit, angularMotionAroundX: PhysicsCustomJoint.MotionLimit, angularMotionAroundY: PhysicsCustomJoint.MotionLimit, angularMotionAroundZ: PhysicsCustomJoint.MotionLimit, checksForInternalCollisions: Bool)](physicscustomjoint/init(pin0:pin1:linearmotionalongx:linearmotionalongy:linearmotionalongz:angularmotionaroundx:angularmotionaroundy:angularmotionaroundz:checksforinternalcollisions:).md)
  Creates a new custom joint.
### Instance Properties
- [var angularMotionAroundX: PhysicsCustomJoint.MotionLimit](physicscustomjoint/angularmotionaroundx.md)
  The angular motion limits around the x-axis.
- [var angularMotionAroundY: PhysicsCustomJoint.MotionLimit](physicscustomjoint/angularmotionaroundy.md)
  The angular motion limits around the y-axis.
- [var angularMotionAroundZ: PhysicsCustomJoint.MotionLimit](physicscustomjoint/angularmotionaroundz.md)
  The angular motion limits around the z-axis.
- [var checksForInternalCollisions: Bool](physicscustomjoint/checksforinternalcollisions.md)
  A Boolean that indicates whether the joint checks and reports collisions between the two entity instances.
- [var isActive: Bool](physicscustomjoint/isactive.md)
  A Boolean that indicates whether the joint is active.
- [var linearMotionAlongX: PhysicsCustomJoint.MotionLimit](physicscustomjoint/linearmotionalongx.md)
  The linear motion limits along the x-axis.
- [var linearMotionAlongY: PhysicsCustomJoint.MotionLimit](physicscustomjoint/linearmotionalongy.md)
  The linear motion limits along the y-axis.
- [var linearMotionAlongZ: PhysicsCustomJoint.MotionLimit](physicscustomjoint/linearmotionalongz.md)
  The linear motion limits along the z-axis.
- [var pin0: GeometricPin](physicscustomjoint/pin0.md)
  The pin that defines a local position and orientation on the first entity.
- [var pin1: GeometricPin](physicscustomjoint/pin1.md)
  The pin that defines a local position and orientation on the second entity.
### Enumerations
- [PhysicsCustomJoint.MotionLimit](physicscustomjoint/motionlimit.md)
  Specifies allowed linear or angular motion.
### Default Implementations
- [Equatable Implementations](physicscustomjoint/equatable-implementations.md)
- [PhysicsJoint Implementations](physicscustomjoint/physicsjoint-implementations.md)

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
- [struct PhysicsDistanceJoint](physicsdistancejoint.md)
  A joint that maintains a minimum and maximum distance between two entity pins.
- [struct PhysicsFixedJoint](physicsfixedjoint.md)
  A joint that rigidly connects two entity pins, with zero degrees of freedom.
- [struct PhysicsJoints](physicsjoints.md)
  A collection of physics joints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/RealityKit/physicscustomjoint)*