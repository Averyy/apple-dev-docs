# particleFrictionVariation

**Framework**: SceneKit  
**Kind**: property

The range of randomized friction coefficients for particles. Animatable.

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
var particleFrictionVariation: CGFloat { get set }
```

#### Discussion

Setting a nonzero value for this property randomizes the effect of the [`particleFriction`](scnparticlesystem/particlefriction.md) property. SceneKit randomly adjusts the friction coefficient of each particle by up to half the [`particleFrictionVariation`](scnparticlesystem/particlefrictionvariation.md) value. For example, if the [`particleFriction`](scnparticlesystem/particlefriction.md) value is `1.0` and the [`particleFrictionVariation`](scnparticlesystem/particlefrictionvariation.md) value is `0.5`, each particle uses a random friction coefficient between `0.75` and `1.25` for physics simulation.

The default value is `0.0`, specifying no randomization.

You can animate changes to this property’s value. See [`Animating SceneKit Content`](animating-scenekit-content.md).

## See Also

- [var isAffectedByGravity: Bool](scnparticlesystem/isaffectedbygravity.md)
  A Boolean value that determines whether gravity, as defined by the scene’s physics simulation, affects the motion of particles.
- [var isAffectedByPhysicsFields: Bool](scnparticlesystem/isaffectedbyphysicsfields.md)
  A Boolean value that determines whether physics fields in the scene affect the motion of particles.
- [var colliderNodes: [SCNNode]?](scnparticlesystem/collidernodes.md)
  The nodes whose geometry the system’s particles can collide with.
- [var particleDiesOnCollision: Bool](scnparticlesystem/particlediesoncollision.md)
  A Boolean value that determines whether particles are removed from the scene upon colliding with another object.
- [var acceleration: SCNVector3](scnparticlesystem/acceleration.md)
  The constant acceleration vector, in units per second per second, applied to all particles in the system. Animatable.
- [var dampingFactor: CGFloat](scnparticlesystem/dampingfactor.md)
  A factor that slows particles relative to their velocity. Animatable.
- [var particleMass: CGFloat](scnparticlesystem/particlemass.md)
  The mass, in kilograms, of each particle in the system. Animatable.
- [var particleMassVariation: CGFloat](scnparticlesystem/particlemassvariation.md)
  The range, in kilograms, of randomized particle masses. Animatable.
- [var particleCharge: CGFloat](scnparticlesystem/particlecharge.md)
  The electric charge, in coulombs, of each particle in the system. Animatable.
- [var particleChargeVariation: CGFloat](scnparticlesystem/particlechargevariation.md)
  The range, in coulombs, of randomized particle charges. Animatable.
- [var particleBounce: CGFloat](scnparticlesystem/particlebounce.md)
  The restitution coefficient of each particle in the system. Animatable.
- [var particleBounceVariation: CGFloat](scnparticlesystem/particlebouncevariation.md)
  The range of randomized restitution coefficients for particles. Animatable.
- [var particleFriction: CGFloat](scnparticlesystem/particlefriction.md)
  The friction coefficient of each particle in the system. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlesystem/particlefrictionvariation)*