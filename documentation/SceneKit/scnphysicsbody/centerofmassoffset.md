# centerOfMassOffset

**Framework**: SceneKit  
**Kind**: property

The position of the body’s center of mass relative to its local coordinate origin.

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
var centerOfMassOffset: SCNVector3 { get set }
```

#### Discussion

The results of physics interactions with a body depend on its center of mass. For example, a collision close to or in line with the center of mass tends to move the whole body (that is, it adds linear velocity), but a collision not aligned with the center of mass tends to cause the body to rotate or topple (that is, it adds angular velocity).

When this property’s value is the vector `(0, 0, 0)` (the default), SceneKit simulates interactions with the assumption that the body’s center of mass is at the origin of its local coordinate space (the [`simdPosition`](scnnode/simdposition.md) of the node owning the physics body).

Change this value when you want to introduce a difference between the object’s geometric center and its center of mass. For example:

- To simulate a body with uneven distribution of mass, such as a hammer with a long handle and heavy head.
- To use a point other than the center of mass for positioning the object in the scene, such as the point where the object rests on a surface.

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
- [var usesDefaultMomentOfInertia: Bool](scnphysicsbody/usesdefaultmomentofinertia.md)
  A Boolean value that determines whether SceneKit automatically calculates the body’s moment of inertia or allows setting a custom value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsbody/centerofmassoffset)*