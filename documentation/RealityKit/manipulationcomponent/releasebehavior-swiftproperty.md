# releaseBehavior

**Framework**: RealityKit  
**Kind**: property

The behavior to apply to the object’s transform when it’s released. By default, the `releaseBehavior` is `.reset`, which will animate the object to its initial pose relative to its parent.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
var releaseBehavior: ManipulationComponent.ReleaseBehavior
```

## See Also

- [static func configureEntity(Entity, hoverEffect: HoverEffectComponent.HoverEffect?, allowedInputTypes: InputTargetComponent.InputType?, collisionShapes: [ShapeResource]?)](manipulationcomponent/configureentity(_:hovereffect:allowedinputtypes:collisionshapes:).md)
  Apply a default configuration to the entity to enable to it for use with `ManipulationComponent`. This function applies an `InputTargetComponent`, `CollisionComponent`, and `HoverEffectComponent` all configured. Before calling this function the entity should have a loaded mesh asset. If `collisionShapes` is not set, the system will generate a collision mesh based on the entity’s bounding box. This function will not replace any pre-existing components of these types.
- [var audioConfiguration: ManipulationComponent.AudioConfiguration](manipulationcomponent/audioconfiguration-swift.property.md)
  The audio configuration to apply to the object over the course of the interaction. By default, the system applies standard audio for key moments of the interaction, such as when the interaction begins, a handoff occurs, or the object is released. To apply custom sounds, set the configuration to `none` and apply audio as needed using the various `ManipulationEvents` delivered to the scene.
- [var dynamics: ManipulationComponent.Dynamics](manipulationcomponent/dynamics-swift.property.md)
  The dynamics controlling the object’s movement and behaviors during the interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/manipulationcomponent/releasebehavior-swift.property)*