# addModifier(forProperties:at:modifier:)

**Framework**: SceneKit  
**Kind**: method

Adds a block that modifies particle properties, to be executed each time SceneKit renders a frame.

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
func addModifier(forProperties properties: [SCNParticleSystem.ParticleProperty], at stage: SCNParticleModifierStage, modifier block: @escaping SCNParticleModifierBlock)
```

#### Discussion

By associating a block with one or more particle properties, you can run arbitrary code that modifies those properties during each frame of animation. This option provides maximum flexibility for changing the appearance or behavior of particles over time.

> ❗ **Important**:  Running your own code to update particle properties every frame can have a severe impact on rendering performance. If the behavior over time that you want for your particle system can be described more declaratively, use the [`propertyControllers`](scnparticlesystem/propertycontrollers.md) property and [`SCNParticlePropertyController`](scnparticlepropertycontroller.md) class instead. If you need to change particle properties only at certain times (rather than continuously), add a handler block for an event using the [`handle(_:forProperties:handler:)`](scnparticlesystem/handle(_:forproperties:handler:).md) method.

 Running your own code to update particle properties every frame can have a severe impact on rendering performance. If the behavior over time that you want for your particle system can be described more declaratively, use the [`propertyControllers`](scnparticlesystem/propertycontrollers.md) property and [`SCNParticlePropertyController`](scnparticlepropertycontroller.md) class instead. If you need to change particle properties only at certain times (rather than continuously), add a handler block for an event using the [`handle(_:forProperties:handler:)`](scnparticlesystem/handle(_:forproperties:handler:).md) method.

## Parameters

- `properties`: An array containing one or more of the constants listed in  , each of which specifies a property of the appearance or behaviors of particles in the particle system.
- `stage`: The stage of SceneKit’s particle simulation during which to call the block. See   for allowed values.
- `block`: A   block to be called every time SceneKit renders a frame. In this block you can modify the properties of all particles in the system.

## See Also

- [func handle(SCNParticleEvent, forProperties: [SCNParticleSystem.ParticleProperty], handler: SCNParticleEventBlock)](scnparticlesystem/handle(_:forproperties:handler:).md)
  Adds a block that modifies particle properties, to be executed at a specified event in the lifetimes of particles in the system.
- [var propertyControllers: [SCNParticleSystem.ParticleProperty : SCNParticlePropertyController]?](scnparticlesystem/propertycontrollers.md)
  A dictionary that optionally associates particle properties with objects that animate a property’s value for each particle.
- [func removeModifiers(at: SCNParticleModifierStage)](scnparticlesystem/removemodifiers(at:).md)
  Removes particle modifier blocks for the specified stage of the particle simulation.
- [func removeAllModifiers()](scnparticlesystem/removeallmodifiers.md)
  Removes all particle modifier blocks associated with the particle system.
- [SCNParticleSystem.ParticleProperty](scnparticlesystem/particleproperty.md)
  Keys identifying properties of individual particles, used by the [`propertyControllers`](scnparticlesystem/propertycontrollers.md) dictionary and the [`handle(_:forProperties:handler:)`](scnparticlesystem/handle(_:forproperties:handler:).md) and [`addModifier(forProperties:at:modifier:)`](scnparticlesystem/addmodifier(forproperties:at:modifier:).md) methods.
- [enum SCNParticleModifierStage](scnparticlemodifierstage.md)
  Stages of SceneKit’s particle simulation process into which you can insert modifier blocks, used by the [`addModifier(forProperties:at:modifier:)`](scnparticlesystem/addmodifier(forproperties:at:modifier:).md) method.
- [typealias SCNParticleModifierBlock](scnparticlemodifierblock.md)
  The signature for blocks called by SceneKit to modify particle properties on each frame of simulation, used by the [`addModifier(forProperties:at:modifier:)`](scnparticlesystem/addmodifier(forproperties:at:modifier:).md) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlesystem/addmodifier(forproperties:at:modifier:))*