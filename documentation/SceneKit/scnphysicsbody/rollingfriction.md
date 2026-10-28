# rollingFriction

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The body’s resistance to rolling motion.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
var rollingFriction: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat rollingFriction;
```

## Discussion

This property simulates the traction between a rounded body and bodies it might roll against. A rolling friction of `0.0` (the default) means that a body induced to roll (for example, by being placed on an inclined surface) will continue to roll without slowing down unless otherwise acted upon, and a rolling friction of `1.0` prevents the body from rolling.

## See Also

### Defining a Body’s Physical Properties
- [var mass: CGFloat](./mass.md)
  The mass of the body, in kilograms.
- [var charge: CGFloat](./charge.md)
  The electric charge of the body, in coulombs.
- [var friction: CGFloat](./friction.md)
  The body’s resistance to sliding motion.
- [var restitution: CGFloat](./restitution.md)
  A factor that determines how much kinetic energy the body loses or gains in collisions.
- [var damping: CGFloat](./damping.md)
  A factor that reduces the body’s linear velocity.
- [var angularDamping: CGFloat](./angulardamping.md)
  A factor that reduces the body’s angular velocity.
- [var momentOfInertia: SCNVector3](./momentofinertia.md)
  The body’s moment of inertia, expressed in the local coordinate system of the node that contains the body.
- [var usesDefaultMomentOfInertia: Bool](./usesdefaultmomentofinertia.md)
  A Boolean value that determines whether SceneKit automatically calculates the body’s moment of inertia or allows setting a custom value.
- [var centerOfMassOffset: SCNVector3](./centerofmassoffset.md)
  The position of the body’s center of mass relative to its local coordinate origin.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsbody/rollingfriction)*