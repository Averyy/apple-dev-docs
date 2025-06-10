# particleMassVariation

**Framework**: SceneKit  
**Kind**: property

The range, in kilograms, of randomized particle masses. Animatable.

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
var particleMassVariation: CGFloat { get set }
```

#### Discussion

Setting a nonzero value for this property randomizes the effect of the [`particleMass`](scnparticlesystem/particlemass.md) property. SceneKit randomly adjusts the mass of each particle by up to half the [`particleMassVariation`](scnparticlesystem/particlemassvariation.md) value. For example, if the [`particleMass`](scnparticlesystem/particlemass.md) value is `1.0` kilograms and the [`particleMassVariation`](scnparticlesystem/particlemassvariation.md) value is `0.5` kilograms, each particle uses a random mass value between `0.75` and `1.25` kilograms for physics simulation.

The default value is `0.0` kilograms, specifying no randomization.

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
- [var particleFrictionVariation: CGFloat](scnparticlesystem/particlefrictionvariation.md)
  The range of randomized friction coefficients for particles. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlesystem/particlemassvariation)*