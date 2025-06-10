# removeAllModifiers()

**Framework**: SceneKit  
**Kind**: method

Removes all particle modifier blocks associated with the particle system.

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
func removeAllModifiers()
```

## See Also

- [var propertyControllers: [SCNParticleSystem.ParticleProperty : SCNParticlePropertyController]?](scnparticlesystem/propertycontrollers.md)
  A dictionary that optionally associates particle properties with objects that animate a property’s value for each particle.
- [func addModifier(forProperties: [SCNParticleSystem.ParticleProperty], at: SCNParticleModifierStage, modifier: SCNParticleModifierBlock)](scnparticlesystem/addmodifier(forproperties:at:modifier:).md)
  Adds a block that modifies particle properties, to be executed each time SceneKit renders a frame.
- [func removeModifiers(at: SCNParticleModifierStage)](scnparticlesystem/removemodifiers(at:).md)
  Removes particle modifier blocks for the specified stage of the particle simulation.
- [SCNParticleSystem.ParticleProperty](scnparticlesystem/particleproperty.md)
  Keys identifying properties of individual particles, used by the [`propertyControllers`](scnparticlesystem/propertycontrollers.md) dictionary and the [`handle(_:forProperties:handler:)`](scnparticlesystem/handle(_:forproperties:handler:).md) and [`addModifier(forProperties:at:modifier:)`](scnparticlesystem/addmodifier(forproperties:at:modifier:).md) methods.
- [enum SCNParticleModifierStage](scnparticlemodifierstage.md)
  Stages of SceneKit’s particle simulation process into which you can insert modifier blocks, used by the [`addModifier(forProperties:at:modifier:)`](scnparticlesystem/addmodifier(forproperties:at:modifier:).md) method.
- [typealias SCNParticleModifierBlock](scnparticlemodifierblock.md)
  The signature for blocks called by SceneKit to modify particle properties on each frame of simulation, used by the [`addModifier(forProperties:at:modifier:)`](scnparticlesystem/addmodifier(forproperties:at:modifier:).md) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlesystem/removeallmodifiers())*