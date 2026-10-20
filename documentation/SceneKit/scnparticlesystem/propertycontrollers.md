# propertyControllers

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

A dictionary that optionally associates particle properties with objects that animate a property’s value for each particle.

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
var propertyControllers: [SCNParticleSystem.ParticleProperty : SCNParticlePropertyController]? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSDictionary<NSString *,SCNParticlePropertyController *> * propertyControllers;
```

#### Discussion

Each key in this dictionary is one of the constants listed in `Particle Property Keys`, and the value for each key is a [`SCNParticlePropertyController`](../scnparticlepropertycontroller.md) object responsible for varying that property over time. Use particle property controllers to add efficient animations that change the appearance or behavior of each particle emitted by the system.

To add more complex behavior that cannot be described by a [`SCNParticlePropertyController`](../scnparticlepropertycontroller.md) object, use the [`addModifier(forProperties:at:modifier:)`](./addmodifier%28forproperties,at,modifier%29.md) to add a particle modifier block. However, be aware that particle modifier blocks can severely impact rendering performance.

## See Also

### Modifying Particles Over Time
- [func addModifier(forProperties: [SCNParticleSystem.ParticleProperty], at: SCNParticleModifierStage, modifier: SCNParticleModifierBlock)](./addmodifier%28forproperties,at,modifier%29.md)
  Adds a block that modifies particle properties, to be executed each time SceneKit renders a frame.
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

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlesystem/propertycontrollers)*