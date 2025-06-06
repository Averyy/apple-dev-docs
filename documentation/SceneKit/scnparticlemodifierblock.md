# SCNParticleModifierBlock

**Framework**: SceneKit  
**Kind**: typealias

The signature for blocks called by SceneKit to modify particle properties on each frame of simulation, used by the [`addModifier(forProperties:at:modifier:)`](scnparticlesystem/addmodifier(forproperties:at:modifier:).md) method.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
typealias SCNParticleModifierBlock = (UnsafeMutablePointer<UnsafeMutableRawPointer>, UnsafeMutablePointer<Int>, Int, Int, Float) -> Void
```

#### Discussion

The block takes the following parameters:

Use this block to change properties of individual particles on each frame of simulation.

> ❗ **Important**:  Running your own code to update particle properties every frame can have a severe impact on rendering performance. If the behavior over time that you want for your particle system can be described more declaratively, use the [`propertyControllers`](scnparticlesystem/propertycontrollers.md) property and [`SCNParticlePropertyController`](scnparticlepropertycontroller.md) class instead. If you need to change particle properties only at certain times (rather than continuously), add a handler block for an event using the [`handle(_:forProperties:handler:)`](scnparticlesystem/handle(_:forproperties:handler:).md) method.

 Running your own code to update particle properties every frame can have a severe impact on rendering performance. If the behavior over time that you want for your particle system can be described more declaratively, use the [`propertyControllers`](scnparticlesystem/propertycontrollers.md) property and [`SCNParticlePropertyController`](scnparticlepropertycontroller.md) class instead. If you need to change particle properties only at certain times (rather than continuously), add a handler block for an event using the [`handle(_:forProperties:handler:)`](scnparticlesystem/handle(_:forproperties:handler:).md) method.

The following example illustrates setting up a modifier block that alters particle’s position and velocity:

```objc
[system addModifierForProperties:@[SCNParticlePropertyPosition,
                                   SCNParticlePropertyVelocity]
                         atStage:SCNParticleModifierStagePostDynamics
                       withBlock:^(void **data, size_t *dataStride, NSInteger start, NSInteger end, float deltaTime) {
                           // For each particle to be processed,
                           // calculate pointers in the data to each property's value:
                           for (NSInteger i = start; i < end; ++i) {
                               // SCNParticlePropertyPosition (float3)
                               float *pos = (float *)((char *)data[0] + dataStride[0] * i);
                               // pos[0..2] are the xyz components of the particle's position.
 
                               // SCNParticlePropertyVelocity (float3)
                               float *vel = (float *)((char *)data[1] + dataStride[1] * i);
                               // vel[0..2] are the xyz components of the particle's position.
 
                               // Now, compute a new position and velocity (not shown).
                           }
                       }];
```

## See Also

- [var propertyControllers: [SCNParticleSystem.ParticleProperty : SCNParticlePropertyController]?](scnparticlesystem/propertycontrollers.md)
  A dictionary that optionally associates particle properties with objects that animate a property’s value for each particle.
- [func addModifier(forProperties: [SCNParticleSystem.ParticleProperty], at: SCNParticleModifierStage, modifier: SCNParticleModifierBlock)](scnparticlesystem/addmodifier(forproperties:at:modifier:).md)
  Adds a block that modifies particle properties, to be executed each time SceneKit renders a frame.
- [func removeModifiers(at: SCNParticleModifierStage)](scnparticlesystem/removemodifiers(at:).md)
  Removes particle modifier blocks for the specified stage of the particle simulation.
- [func removeAllModifiers()](scnparticlesystem/removeallmodifiers.md)
  Removes all particle modifier blocks associated with the particle system.
- [SCNParticleSystem.ParticleProperty](scnparticlesystem/particleproperty.md)
  Keys identifying properties of individual particles, used by the [`propertyControllers`](scnparticlesystem/propertycontrollers.md) dictionary and the [`handle(_:forProperties:handler:)`](scnparticlesystem/handle(_:forproperties:handler:).md) and [`addModifier(forProperties:at:modifier:)`](scnparticlesystem/addmodifier(forproperties:at:modifier:).md) methods.
- [enum SCNParticleModifierStage](scnparticlemodifierstage.md)
  Stages of SceneKit’s particle simulation process into which you can insert modifier blocks, used by the [`addModifier(forProperties:at:modifier:)`](scnparticlesystem/addmodifier(forproperties:at:modifier:).md) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlemodifierblock)*