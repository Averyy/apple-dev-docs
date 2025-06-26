# configureEntity(_:hoverEffect:allowedInputTypes:collisionShapes:)

**Framework**: RealityKit  
**Kind**: method

Apply a default configuration to an entity to enable to it for use with manipulation component.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
static func configureEntity(_ entity: Entity, hoverEffect: HoverEffectComponent.HoverEffect? = nil, allowedInputTypes: InputTargetComponent.InputType? = nil, collisionShapes: [ShapeResource]? = nil)
```

#### Discussion

This function applies an [`InputTargetComponent`](inputtargetcomponent.md), [`CollisionComponent`](collisioncomponent.md), and [`HoverEffectComponent`](hovereffectcomponent.md) to an [`Entity`](entity.md).

Use this method on an entity that already has a mesh asset in a [`ModelComponent`](modelcomponent.md). The system generates a collision mesh based on the entity’s bounding box if you don’t set one. This function will replace any pre-existing components of these types.

## Parameters

- `entity`: The entity to configure.
- `hoverEffect`: A replacement for the default   this method applies.
- `allowedInputTypes`: A replacement for the allowed input types this method applies.
- `collisionShapes`: A replacement for the deafult collision shape this method   generates based on the entity’s bounding box.

## See Also

- [var audioConfiguration: ManipulationComponent.AudioConfiguration](manipulationcomponent/audioconfiguration-swift.property.md)
  The audio configuration to apply to the object over the course of the interaction.
- [var dynamics: ManipulationComponent.Dynamics](manipulationcomponent/dynamics-swift.property.md)
  The dynamics controlling the object’s movement and behaviors during the interaction.
- [var releaseBehavior: ManipulationComponent.ReleaseBehavior](manipulationcomponent/releasebehavior-swift.property.md)
  The behavior to apply to the object’s transform when someone releases it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/manipulationcomponent/configureentity(_:hovereffect:allowedinputtypes:collisionshapes:))*