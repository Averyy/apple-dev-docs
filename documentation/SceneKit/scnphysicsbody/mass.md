# mass

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The mass of the body, in kilograms.

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
var mass: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat mass;
```

## Discussion

The mass of a body affects its momentum and how it responds to forces. The default mass for dynamic bodies is `1.0`. The default mass for static and kinematic bodies is `0.0`, but these bodies are unaffected by mass.

Note that you need not use realistic measurements for the bodies in your app—the effects of the physics simulation depend on the relative masses of different bodies, not the absolute values. You may use whatever values produce the behavior or gameplay you’re looking for as long as you use them consistently.

## See Also

### Defining a Body’s Physical Properties
- [var charge: CGFloat](./charge.md)
  The electric charge of the body, in coulombs.
- [var friction: CGFloat](./friction.md)
  The body’s resistance to sliding motion.
- [var rollingFriction: CGFloat](./rollingfriction.md)
  The body’s resistance to rolling motion.
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

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsbody/mass)*