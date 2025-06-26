# releaseBehavior

**Framework**: RealityKit  
**Kind**: property

The behavior to apply to the object’s transform when someone releases it.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
var releaseBehavior: ManipulationComponent.ReleaseBehavior
```

#### Discussion

By default, the `releaseBehavior` is [`reset`](manipulationcomponent/releasebehavior-swift.struct/reset.md), which animates the object to its initial pose relative to its parent.

## See Also

- [static func configureEntity(Entity, hoverEffect: HoverEffectComponent.HoverEffect?, allowedInputTypes: InputTargetComponent.InputType?, collisionShapes: [ShapeResource]?)](manipulationcomponent/configureentity(_:hovereffect:allowedinputtypes:collisionshapes:).md)
  Apply a default configuration to an entity to enable to it for use with manipulation component.
- [var audioConfiguration: ManipulationComponent.AudioConfiguration](manipulationcomponent/audioconfiguration-swift.property.md)
  The audio configuration to apply to the object over the course of the interaction.
- [var dynamics: ManipulationComponent.Dynamics](manipulationcomponent/dynamics-swift.property.md)
  The dynamics controlling the object’s movement and behaviors during the interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/manipulationcomponent/releasebehavior-swift.property)*