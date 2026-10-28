# addModifier(forProperties:at:modifier:)

**Framework**: SceneKit  
**Kind**: method  
**Role**: Instance Method

Adds a block that modifies particle properties, to be executed each time SceneKit renders a frame.

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
func addModifier(forProperties properties: [SCNParticleSystem.ParticleProperty], at stage: SCNParticleModifierStage, modifier block: @escaping SCNParticleModifierBlock)
```

```objc
- (void) addModifierForProperties:(NSArray<NSString *> *) properties atStage:(SCNParticleModifierStage) stage withBlock:(SCNParticleModifierBlock) block;
```

## Discussion

By associating a block with one or more particle properties, you can run arbitrary code that modifies those properties during each frame of animation. This option provides maximum flexibility for changing the appearance or behavior of particles over time.

> ❗ **Important**:  Running your own code to update particle properties every frame can have a severe impact on rendering performance. If the behavior over time that you want for your particle system can be described more declaratively, use the [`propertyControllers`](./propertycontrollers.md) property and [`SCNParticlePropertyController`](../scnparticlepropertycontroller.md) class instead. If you need to change particle properties only at certain times (rather than continuously), add a handler block for an event using the [`handle(_:forProperties:handler:)`](./handle%28_,forproperties,handler%29.md) method.

## Parameters

- `properties`: An array containing one or more of the constants listed in `Particle Property Keys`, each of which specifies a property of the appearance or behaviors of particles in the particle system.
- `stage`: The stage of SceneKit’s particle simulation during which to call the block. See [`SCNParticleModifierStage`](../scnparticlemodifierstage.md) for allowed values.
- `block`: A [`SCNParticleModifierBlock`](../scnparticlemodifierblock.md) block to be called every time SceneKit renders a frame. In this block you can modify the properties of all particles in the system.

## See Also

### Related Documentation
- [func handle(SCNParticleEvent, forProperties: [SCNParticleSystem.ParticleProperty], handler: SCNParticleEventBlock)](./handle%28_,forproperties,handler%29.md)
  Adds a block that modifies particle properties, to be executed at a specified event in the lifetimes of particles in the system.
### Modifying Particles Over Time
- [var propertyControllers: [SCNParticleSystem.ParticleProperty : SCNParticlePropertyController]?](./propertycontrollers.md)
  A dictionary that optionally associates particle properties with objects that animate a property’s value for each particle.
- [func removeModifiers(at: SCNParticleModifierStage)](./removemodifiers%28at%29.md)
  Removes particle modifier blocks for the specified stage of the particle simulation.
- [func removeAllModifiers()](./removeallmodifiers%28%29.md)
  Removes all particle modifier blocks associated with the particle system.
- [SCNParticleSystem.ParticleProperty](./particleproperty.md)
  Keys identifying properties of individual particles, used by the [`propertyControllers`](./propertycontrollers.md) dictionary and the [`handle(_:forProperties:handler:)`](./handle%28_,forproperties,handler%29.md) and [`addModifier(forProperties:at:modifier:)`](./addmodifier%28forproperties,at,modifier%29.md) methods.
- [enum SCNParticleModifierStage](../scnparticlemodifierstage.md)
  Stages of SceneKit’s particle simulation process into which you can insert modifier blocks, used by the [`addModifier(forProperties:at:modifier:)`](./addmodifier%28forproperties,at,modifier%29.md) method.
- [typealias SCNParticleModifierBlock](../scnparticlemodifierblock.md)
  The signature for blocks called by SceneKit to modify particle properties on each frame of simulation, used by the [`addModifier(forProperties:at:modifier:)`](./addmodifier%28forproperties,at,modifier%29.md) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlesystem/addmodifier(forproperties:at:modifier:))*