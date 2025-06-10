# SCNParticleSystem.ParticleProperty

**Framework**: SceneKit  
**Kind**: struct

Keys identifying properties of individual particles, used by the [`propertyControllers`](scnparticlesystem/propertycontrollers.md) dictionary and the [`handle(_:forProperties:handler:)`](scnparticlesystem/handle(_:forproperties:handler:).md) and [`addModifier(forProperties:at:modifier:)`](scnparticlesystem/addmodifier(forproperties:at:modifier:).md) methods.

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
struct ParticleProperty
```

## Topics

### Type Properties
- [static let angle: SCNParticleSystem.ParticleProperty](scnparticlesystem/particleproperty/angle.md)
  The rotation angle, in radians, of the particle about its axis.
- [static let angularVelocity: SCNParticleSystem.ParticleProperty](scnparticlesystem/particleproperty/angularvelocity.md)
  The particle’s angular velocity (or rate of spin), in radians per second.
- [static let bounce: SCNParticleSystem.ParticleProperty](scnparticlesystem/particleproperty/bounce.md)
  The particle’s restitution coefficient.
- [static let charge: SCNParticleSystem.ParticleProperty](scnparticlesystem/particleproperty/charge.md)
  The particle’s electric charge, in coulombs.
- [static let color: SCNParticleSystem.ParticleProperty](scnparticlesystem/particleproperty/color.md)
  The particle’s tint color, as a vector of red, green, blue, and alpha component values.
- [static let contactNormal: SCNParticleSystem.ParticleProperty](scnparticlesystem/particleproperty/contactnormal.md)
  The normal vector, in scene coordinate space, of a collision between a particle and a geometry in the scene.
- [static let contactPoint: SCNParticleSystem.ParticleProperty](scnparticlesystem/particleproperty/contactpoint.md)
  The location, in scene coordinate space, of a collision between a particle and a geometry in the scene.
- [static let frame: SCNParticleSystem.ParticleProperty](scnparticlesystem/particleproperty/frame.md)
  The current frame index of the particle’s image animation.
- [static let frameRate: SCNParticleSystem.ParticleProperty](scnparticlesystem/particleproperty/framerate.md)
  The rate, in frames per second, of the particle’s image animation.
- [static let friction: SCNParticleSystem.ParticleProperty](scnparticlesystem/particleproperty/friction.md)
  The particle’s friction coefficient.
- [static let life: SCNParticleSystem.ParticleProperty](scnparticlesystem/particleproperty/life.md)
  The remaining time in the particle’s life span, in seconds.
- [static let opacity: SCNParticleSystem.ParticleProperty](scnparticlesystem/particleproperty/opacity.md)
  The particle’s opacity (or alpha value).
- [static let position: SCNParticleSystem.ParticleProperty](scnparticlesystem/particleproperty/position.md)
  The particle’s position vector in scene coordinate space.
- [static let rotationAxis: SCNParticleSystem.ParticleProperty](scnparticlesystem/particleproperty/rotationaxis.md)
  The particle’s axis of rotation, expressed as a vector in the particle’s local coordinate space.
- [static let size: SCNParticleSystem.ParticleProperty](scnparticlesystem/particleproperty/size.md)
  The width and height of the rendered particle image, in units of scene coordinate space.
- [static let velocity: SCNParticleSystem.ParticleProperty](scnparticlesystem/particleproperty/velocity.md)
  The particle’s velocity vector in units (of scene coordinate space) per second.
### Initializers
- [init(rawValue: String)](scnparticlesystem/particleproperty/init(rawvalue:).md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var propertyControllers: [SCNParticleSystem.ParticleProperty : SCNParticlePropertyController]?](scnparticlesystem/propertycontrollers.md)
  A dictionary that optionally associates particle properties with objects that animate a property’s value for each particle.
- [func addModifier(forProperties: [SCNParticleSystem.ParticleProperty], at: SCNParticleModifierStage, modifier: SCNParticleModifierBlock)](scnparticlesystem/addmodifier(forproperties:at:modifier:).md)
  Adds a block that modifies particle properties, to be executed each time SceneKit renders a frame.
- [func removeModifiers(at: SCNParticleModifierStage)](scnparticlesystem/removemodifiers(at:).md)
  Removes particle modifier blocks for the specified stage of the particle simulation.
- [func removeAllModifiers()](scnparticlesystem/removeallmodifiers.md)
  Removes all particle modifier blocks associated with the particle system.
- [enum SCNParticleModifierStage](scnparticlemodifierstage.md)
  Stages of SceneKit’s particle simulation process into which you can insert modifier blocks, used by the [`addModifier(forProperties:at:modifier:)`](scnparticlesystem/addmodifier(forproperties:at:modifier:).md) method.
- [typealias SCNParticleModifierBlock](scnparticlemodifierblock.md)
  The signature for blocks called by SceneKit to modify particle properties on each frame of simulation, used by the [`addModifier(forProperties:at:modifier:)`](scnparticlesystem/addmodifier(forproperties:at:modifier:).md) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlesystem/particleproperty)*