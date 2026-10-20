# momentOfInertia

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The body’s moment of inertia, expressed in the local coordinate system of the node that contains the body.

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
var momentOfInertia: SCNVector3 { get set }
```

```objc
@property (nonatomic) SCNVector3 momentOfInertia;
```

#### Discussion

A body’s moment of inertia determines how it responds to torques (that is, forces with a rotational component). Each component of this vector is the moment of inertia for the corresponding principal axis (in the coordinate system containing the physics body). For example, if the x-component value of the moment vector is less than the y-component value, the body rotates more freely about its x-axis than its y-axis.

By default, SceneKit automatically determines the body’s moment of inertia based on its shape and mass. Use this property to define a custom moment of inertia (for example, to model an object of non-uniform density). Using a custom moment of inertia requires setting the [`usesDefaultMomentOfInertia`](./usesdefaultmomentofinertia.md) property to [`false`](../../Swift/false.md).

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
- [var restitution: CGFloat](./restitution.md)
  A factor that determines how much kinetic energy the body loses or gains in collisions.
- [var damping: CGFloat](./damping.md)
  A factor that reduces the body’s linear velocity.
- [var angularDamping: CGFloat](./angulardamping.md)
  A factor that reduces the body’s angular velocity.
- [var usesDefaultMomentOfInertia: Bool](./usesdefaultmomentofinertia.md)
  A Boolean value that determines whether SceneKit automatically calculates the body’s moment of inertia or allows setting a custom value.
- [var centerOfMassOffset: SCNVector3](./centerofmassoffset.md)
  The position of the body’s center of mass relative to its local coordinate origin.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsbody/momentofinertia)*