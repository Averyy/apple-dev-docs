# audioConfiguration

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

The audio configuration to apply to the object over the course of the interaction.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
var audioConfiguration: ManipulationComponent.AudioConfiguration
```

#### Discussion

By default, the system applies standard audio for key moments of the interaction, such as when the interaction begins, a handoff occurs, or the object is released. To apply custom sounds, set the configuration to [`none`](./audioconfiguration-swift.struct/none.md) and apply audio as needed using the various `ManipulationEvents` you can subscribe to in the scene.

## See Also

### Configuring the manipulation
- [static func configureEntity(Entity, hoverEffect: HoverEffectComponent.HoverEffect?, allowedInputTypes: InputTargetComponent.InputType?, collisionShapes: [ShapeResource]?)](./configureentity%28_,hovereffect,allowedinputtypes,collisionshapes%29.md)
  Apply a default configuration to an entity to enable to it for use with manipulation component.
- [var dynamics: ManipulationComponent.Dynamics](./dynamics-swift.property.md)
  The dynamics controlling the object’s movement and behaviors during the interaction.
- [var releaseBehavior: ManipulationComponent.ReleaseBehavior](./releasebehavior-swift.property.md)
  The behavior to apply to the object’s transform when someone releases it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/manipulationcomponent/audioconfiguration-swift.property)*