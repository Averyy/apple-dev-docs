# angularDamping

**Framework**: SceneKit  
**Kind**: property

A factor that reduces the body’s angular velocity.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var angularDamping: CGFloat { get set }
```

#### Discussion

This property simulates the effect of rotational friction on a body. A damping factor of `0.0` specifies no loss in angular velocity, and a damping factor of `1.0` prevents the body from rotating. The default damping factor is `0.1`.

## See Also

- [var mass: CGFloat](scnphysicsbody/mass.md)
  The mass of the body, in kilograms.
- [var charge: CGFloat](scnphysicsbody/charge.md)
  The electric charge of the body, in coulombs.
- [var friction: CGFloat](scnphysicsbody/friction.md)
  The body’s resistance to sliding motion.
- [var rollingFriction: CGFloat](scnphysicsbody/rollingfriction.md)
  The body’s resistance to rolling motion.
- [var restitution: CGFloat](scnphysicsbody/restitution.md)
  A factor that determines how much kinetic energy the body loses or gains in collisions.
- [var damping: CGFloat](scnphysicsbody/damping.md)
  A factor that reduces the body’s linear velocity.
- [var momentOfInertia: SCNVector3](scnphysicsbody/momentofinertia.md)
  The body’s moment of inertia, expressed in the local coordinate system of the node that contains the body.
- [var usesDefaultMomentOfInertia: Bool](scnphysicsbody/usesdefaultmomentofinertia.md)
  A Boolean value that determines whether SceneKit automatically calculates the body’s moment of inertia or allows setting a custom value.
- [var centerOfMassOffset: SCNVector3](scnphysicsbody/centerofmassoffset.md)
  The position of the body’s center of mass relative to its local coordinate origin.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsbody/angulardamping)*