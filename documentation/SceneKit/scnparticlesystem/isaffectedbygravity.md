# isAffectedByGravity

**Framework**: SceneKit  
**Kind**: property

A Boolean value that determines whether gravity, as defined by the scene’s physics simulation, affects the motion of particles.

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
var isAffectedByGravity: Bool { get set }
```

#### Discussion

Gravity applies a constant acceleration to all particles in the system. SceneKit offers two options for simulating the effect of gravity on particles:

- The [`isAffectedByGravity`](scnparticlesystem/isaffectedbygravity.md) property, which uses the [`gravity`](scnphysicsworld/gravity.md) vector specified by the [`physicsWorld`](scnscene/physicsworld.md) object of the scene containing the particle system. Use this option when you want the system’s particles to be affected by the same gravity as the [`SCNPhysicsBody`](scnphysicsbody.md) objects in your scene.
- The [`acceleration`](scnparticlesystem/acceleration.md) property, which is independent of the simulation SceneKit uses for physics bodies in the scene. Use acceleration to simulate gravity if you have no [`SCNPhysicsBody`](scnphysicsbody.md) objects in your scene, or if you want particles to be affected both by the physics world’s gravity and another constant acceleration (such as wind).

The default value is [`false`](https://developer.apple.com/documentation/swift/false), specifying that the physics world’s gravity does not affect particles.

## See Also

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
- [var particleFrictionVariation: CGFloat](scnparticlesystem/particlefrictionvariation.md)
  The range of randomized friction coefficients for particles. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlesystem/isaffectedbygravity)*