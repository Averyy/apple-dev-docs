# colliderNodes

**Framework**: SceneKit  
**Kind**: property

The nodes whose geometry the system’s particles can collide with.

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
var colliderNodes: [SCNNode]? { get set }
```

#### Discussion

A particle system can perform limited collision detection and resolution with geometries in the scene. If a moving particle intersects a geometry attached to one of the [`SCNNode`](scnnode.md) objects in this array, SceneKit resolves the collision, either by removing the particle from the scene or allowing it to bounce off or slide along the geometry’s surface.

> **Note**:  Collision detection is computationally intensive. For the best rendering performance, limit the number of collider nodes for each particle system, and use only simple geometries—represented by the [`SCNSphere`](scnsphere.md), [`SCNPlane`](scnplane.md), and [`SCNFloor`](scnfloor.md) classes—as collision surfaces.

 Collision detection is computationally intensive. For the best rendering performance, limit the number of collider nodes for each particle system, and use only simple geometries—represented by the [`SCNSphere`](scnsphere.md), [`SCNPlane`](scnplane.md), and [`SCNFloor`](scnfloor.md) classes—as collision surfaces.

This array is empty by default.

## See Also

- [var isAffectedByGravity: Bool](scnparticlesystem/isaffectedbygravity.md)
  A Boolean value that determines whether gravity, as defined by the scene’s physics simulation, affects the motion of particles.
- [var isAffectedByPhysicsFields: Bool](scnparticlesystem/isaffectedbyphysicsfields.md)
  A Boolean value that determines whether physics fields in the scene affect the motion of particles.
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

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlesystem/collidernodes)*