# restitution

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

A factor that determines how much kinetic energy the body loses or gains in collisions.

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
var restitution: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat restitution;
```

## Discussion

This property simulates the “bounciness” of a body. A restitution of `1.0` means that the body loses no energy in a collision—for example, a ball dropped onto a flat surface will bounce back to the height it fell from. A restitution of `0.0` means the body does not bounce after a collision. A restitution of greater than `1.0` causes the body to gain energy in collisions. The default restitution is `0.5`.

## See Also

### Defining a Body’s Physical Properties
- [var mass: CGFloat](./mass.md)
  The mass of the body, in kilograms.
- [var charge: CGFloat](./charge.md)
  The electric charge of the body, in coulombs.
- [var friction: CGFloat](./friction.md)
  The body’s resistance to sliding motion.
- [var rollingFriction: CGFloat](./rollingfriction.md)
  The body’s resistance to rolling motion.
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

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsbody/restitution)*