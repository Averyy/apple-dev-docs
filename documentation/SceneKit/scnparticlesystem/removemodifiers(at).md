# removeModifiers(at:)

**Framework**: SceneKit  
**Kind**: method  
**Role**: Instance Method

Removes particle modifier blocks for the specified stage of the particle simulation.

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
func removeModifiers(at stage: SCNParticleModifierStage)
```

```objc
- (void) removeModifiersOfStage:(SCNParticleModifierStage) stage;
```

## Parameters

- `stage`: The stage of SceneKit’s particle simulation during which to call the block. See [`SCNParticleModifierStage`](../scnparticlemodifierstage.md) for allowed values.

## See Also

### Modifying Particles Over Time
- [var propertyControllers: [SCNParticleSystem.ParticleProperty : SCNParticlePropertyController]?](./propertycontrollers.md)
  A dictionary that optionally associates particle properties with objects that animate a property’s value for each particle.
- [func addModifier(forProperties: [SCNParticleSystem.ParticleProperty], at: SCNParticleModifierStage, modifier: SCNParticleModifierBlock)](./addmodifier%28forproperties,at,modifier%29.md)
  Adds a block that modifies particle properties, to be executed each time SceneKit renders a frame.
- [func removeAllModifiers()](./removeallmodifiers%28%29.md)
  Removes all particle modifier blocks associated with the particle system.
- [SCNParticleSystem.ParticleProperty](./particleproperty.md)
  Keys identifying properties of individual particles, used by the [`propertyControllers`](./propertycontrollers.md) dictionary and the [`handle(_:forProperties:handler:)`](./handle%28_,forproperties,handler%29.md) and [`addModifier(forProperties:at:modifier:)`](./addmodifier%28forproperties,at,modifier%29.md) methods.
- [enum SCNParticleModifierStage](../scnparticlemodifierstage.md)
  Stages of SceneKit’s particle simulation process into which you can insert modifier blocks, used by the [`addModifier(forProperties:at:modifier:)`](./addmodifier%28forproperties,at,modifier%29.md) method.
- [typealias SCNParticleModifierBlock](../scnparticlemodifierblock.md)
  The signature for blocks called by SceneKit to modify particle properties on each frame of simulation, used by the [`addModifier(forProperties:at:modifier:)`](./addmodifier%28forproperties,at,modifier%29.md) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlesystem/removemodifiers(at:))*