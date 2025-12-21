# usesDefaultMomentOfInertia

**Framework**: SceneKit  
**Kind**: property

A Boolean value that determines whether SceneKit automatically calculates the body’s moment of inertia or allows setting a custom value.

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
var usesDefaultMomentOfInertia: Bool { get set }
```

#### Discussion

A body’s moment of inertia determines how it responds to torques (that is, forces with a rotational component).

If this property is [`true`](https://developer.apple.com/documentation/Swift/true) (the default), SceneKit automatically determines the body’s moment of inertia based on its shape and mass. Set this property to [`false`](https://developer.apple.com/documentation/Swift/false) and use the [`momentOfInertia`](scnphysicsbody/momentofinertia.md) property to define a custom moment of inertia (for example, to model an object of non-uniform density).

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
- [var angularDamping: CGFloat](scnphysicsbody/angulardamping.md)
  A factor that reduces the body’s angular velocity.
- [var momentOfInertia: SCNVector3](scnphysicsbody/momentofinertia.md)
  The body’s moment of inertia, expressed in the local coordinate system of the node that contains the body.
- [var centerOfMassOffset: SCNVector3](scnphysicsbody/centerofmassoffset.md)
  The position of the body’s center of mass relative to its local coordinate origin.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsbody/usesdefaultmomentofinertia)*