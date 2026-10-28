# isAffectedByGravity

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether gravity, as defined by the scene’s physics simulation, affects the motion of particles.

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
var isAffectedByGravity: Bool { get set }
```

```objc
@property (nonatomic) BOOL affectedByGravity;
```

## Discussion

Gravity applies a constant acceleration to all particles in the system. SceneKit offers two options for simulating the effect of gravity on particles:

- The [`isAffectedByGravity`](./isaffectedbygravity.md) property, which uses the [`gravity`](../scnphysicsworld/gravity.md) vector specified by the [`physicsWorld`](../scnscene/physicsworld.md) object of the scene containing the particle system. Use this option when you want the system’s particles to be affected by the same gravity as the [`SCNPhysicsBody`](../scnphysicsbody.md) objects in your scene.
- The [`acceleration`](./acceleration.md) property, which is independent of the simulation SceneKit uses for physics bodies in the scene. Use acceleration to simulate gravity if you have no [`SCNPhysicsBody`](../scnphysicsbody.md) objects in your scene, or if you want particles to be affected both by the physics world’s gravity and another constant acceleration (such as wind).

The default value is [`false`](../../Swift/false.md), specifying that the physics world’s gravity does not affect particles.

## See Also

### Simulating Physics for Particles
- [var isAffectedByPhysicsFields: Bool](./isaffectedbyphysicsfields.md)
  A Boolean value that determines whether physics fields in the scene affect the motion of particles.
- [var colliderNodes: [SCNNode]?](./collidernodes.md)
  The nodes whose geometry the system’s particles can collide with.
- [var particleDiesOnCollision: Bool](./particlediesoncollision.md)
  A Boolean value that determines whether particles are removed from the scene upon colliding with another object.
- [var acceleration: SCNVector3](./acceleration.md)
  The constant acceleration vector, in units per second per second, applied to all particles in the system. Animatable.
- [var dampingFactor: CGFloat](./dampingfactor.md)
  A factor that slows particles relative to their velocity. Animatable.
- [var particleMass: CGFloat](./particlemass.md)
  The mass, in kilograms, of each particle in the system. Animatable.
- [var particleMassVariation: CGFloat](./particlemassvariation.md)
  The range, in kilograms, of randomized particle masses. Animatable.
- [var particleCharge: CGFloat](./particlecharge.md)
  The electric charge, in coulombs, of each particle in the system. Animatable.
- [var particleChargeVariation: CGFloat](./particlechargevariation.md)
  The range, in coulombs, of randomized particle charges. Animatable.
- [var particleBounce: CGFloat](./particlebounce.md)
  The restitution coefficient of each particle in the system. Animatable.
- [var particleBounceVariation: CGFloat](./particlebouncevariation.md)
  The range of randomized restitution coefficients for particles. Animatable.
- [var particleFriction: CGFloat](./particlefriction.md)
  The friction coefficient of each particle in the system. Animatable.
- [var particleFrictionVariation: CGFloat](./particlefrictionvariation.md)
  The range of randomized friction coefficients for particles. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlesystem/isaffectedbygravity)*