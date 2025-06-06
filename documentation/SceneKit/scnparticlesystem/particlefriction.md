# particleFriction

**Framework**: SceneKit  
**Kind**: property

The friction coefficient of each particle in the system. Animatable.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var particleFriction: CGFloat { get set }
```

#### Discussion

Friction determines a particle’s resistance to sliding motion after a collision. (To define collision behavior, see the [`colliderNodes`](scnparticlesystem/collidernodes.md) property.) You can randomize the friction coefficients of particles in the system with the [`particleFrictionVariation`](scnparticlesystem/particlefrictionvariation.md) property.

A value of `1.0` (the default) allows a particle to slide freely, and a value of `0.0` prevents a particle from sliding.

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
- [var particleFrictionVariation: CGFloat](scnparticlesystem/particlefrictionvariation.md)
  The range of randomized friction coefficients for particles. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlesystem/particlefriction)*