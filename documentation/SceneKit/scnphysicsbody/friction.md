# friction

**Framework**: SceneKit  
**Kind**: property

The body’s resistance to sliding motion.

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
var friction: CGFloat { get set }
```

#### Discussion

This property simulates the roughness of the body’s surface. When two bodies are in contact and a force is applied that would cause them to slide against one another, the friction values for both bodies determine their resistance to motion. If both bodies’ friction value is `0.0`, they slide freely against each other. If both bodies’ friction value is `1.0`, they do not slide at all. The default friction is `0.5`.

## See Also

- [var mass: CGFloat](scnphysicsbody/mass.md)
  The mass of the body, in kilograms.
- [var charge: CGFloat](scnphysicsbody/charge.md)
  The electric charge of the body, in coulombs.
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
- [var usesDefaultMomentOfInertia: Bool](scnphysicsbody/usesdefaultmomentofinertia.md)
  A Boolean value that determines whether SceneKit automatically calculates the body’s moment of inertia or allows setting a custom value.
- [var centerOfMassOffset: SCNVector3](scnphysicsbody/centerofmassoffset.md)
  The position of the body’s center of mass relative to its local coordinate origin.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsbody/friction)*