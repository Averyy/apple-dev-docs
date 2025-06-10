# particleMass

**Framework**: SceneKit  
**Kind**: property

The mass, in kilograms, of each particle in the system. Animatable.

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
var particleMass: CGFloat { get set }
```

#### Discussion

A particle’s mass determines its resistance to forces. The effects of the [`dampingFactor`](scnparticlesystem/dampingfactor.md) property and any [`SCNPhysicsField`](scnphysicsfield.md) objects affecting each particle are proportional to its mass. You can randomize the masses of particles in the system with the [`particleMassVariation`](scnparticlesystem/particlemassvariation.md) property.

The default value is `1.0` kilograms.

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
- [var particleFrictionVariation: CGFloat](scnparticlesystem/particlefrictionvariation.md)
  The range of randomized friction coefficients for particles. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlesystem/particlemass)*