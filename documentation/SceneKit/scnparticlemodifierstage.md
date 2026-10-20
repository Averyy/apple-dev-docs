# SCNParticleModifierStage

**Framework**: SceneKit  
**Kind**: enum  
**Role**: Enumeration

Stages of SceneKit’s particle simulation process into which you can insert modifier blocks, used by the [`addModifier(forProperties:at:modifier:)`](./scnparticlesystem/addmodifier%28forproperties,at,modifier%29.md) method.

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
enum SCNParticleModifierStage
```

```c
enum SCNParticleModifierStage : NSInteger;
```

## Topics

### Constants
- [SCNParticleModifierStage.preDynamics](./scnparticlemodifierstage/predynamics.md)
  The stage before SceneKit simulates the motion of particles.
- [SCNParticleModifierStage.postDynamics](./scnparticlemodifierstage/postdynamics.md)
  The stage after SceneKit simulates the motion of particles.
- [SCNParticleModifierStage.preCollision](./scnparticlemodifierstage/precollision.md)
  The stage before SceneKit simulates the results of collisions between particles and scene geometry.
- [SCNParticleModifierStage.postCollision](./scnparticlemodifierstage/postcollision.md)
  The stage after SceneKit simulates the results of collisions between particles and scene geometry.
### Initializers
- [init?(rawValue: Int)](./scnparticlemodifierstage/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Modifying Particles Over Time
- [var propertyControllers: [SCNParticleSystem.ParticleProperty : SCNParticlePropertyController]?](./scnparticlesystem/propertycontrollers.md)
  A dictionary that optionally associates particle properties with objects that animate a property’s value for each particle.
- [func addModifier(forProperties: [SCNParticleSystem.ParticleProperty], at: SCNParticleModifierStage, modifier: SCNParticleModifierBlock)](./scnparticlesystem/addmodifier%28forproperties,at,modifier%29.md)
  Adds a block that modifies particle properties, to be executed each time SceneKit renders a frame.
- [func removeModifiers(at: SCNParticleModifierStage)](./scnparticlesystem/removemodifiers%28at%29.md)
  Removes particle modifier blocks for the specified stage of the particle simulation.
- [func removeAllModifiers()](./scnparticlesystem/removeallmodifiers%28%29.md)
  Removes all particle modifier blocks associated with the particle system.
- [SCNParticleSystem.ParticleProperty](./scnparticlesystem/particleproperty.md)
  Keys identifying properties of individual particles, used by the [`propertyControllers`](./scnparticlesystem/propertycontrollers.md) dictionary and the [`handle(_:forProperties:handler:)`](./scnparticlesystem/handle%28_,forproperties,handler%29.md) and [`addModifier(forProperties:at:modifier:)`](./scnparticlesystem/addmodifier%28forproperties,at,modifier%29.md) methods.
- [typealias SCNParticleModifierBlock](./scnparticlemodifierblock.md)
  The signature for blocks called by SceneKit to modify particle properties on each frame of simulation, used by the [`addModifier(forProperties:at:modifier:)`](./scnparticlesystem/addmodifier%28forproperties,at,modifier%29.md) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlemodifierstage)*