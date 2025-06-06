# GroundingShadowComponent

**Framework**: RealityKit  
**Kind**: struct

A component that controls an entity’s grounding shadow.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 1.0+

## Declaration

```swift
struct GroundingShadowComponent
```

#### Overview

A grounding shadow is an effect that makes an entity look like it has a light source directly above it. You can add a grounding shadow to any entity that has a [`ModelComponent`](modelcomponent.md) in its component set by adding a grounding shadow component to the entity’s [`components`](entity/components.md) property.

```swift
if let model = try? await ModelEntity(named: "tv_retro") {
    let shadowComponent = GroundingShadowComponent(castsShadow: true)
    model.components.set(shadowComponent)
}
```

| Without shadow | With shadow |
| --- | --- |
| ![A screenshot of a vintage-style TV near the floor of a kitchen scene, which doesn’t cast a shadow onto the floor.](https://docs-assets.developer.apple.com/published/a57f9bda1580e70d550ac8b4026fac5e/groundingshadowcomponent-tv-off.jpg) | ![A screenshot of a vintage-style TV near the floor of a kitchen scene, which casts a shadow onto the floor.](https://docs-assets.developer.apple.com/published/8f57b03abf162b5614b406e000856d69/groundingshadowcomponent-tv-on.jpg) |

You need to add the grounding shadow component to each entity you want to apply the effect to, because the grounding shadow component doesn’t apply to hierarchies.

> **Note**: Neither virtual nor physical light sources affect grounding shadows.

Neither virtual nor physical light sources affect grounding shadows.

##### Receiving Shadows

By default, all entity models with a grounding shadow component can cast a shadow onto any other model entities in the scene. However, you can configure an entity to opt out of receiving shadows from other entities by setting a grounding shadow component’s [`receivesShadow`](groundingshadowcomponent/receivesshadow.md) property to `false` and adding that component to the entity that’s opting out.

```swift
let tvShadow = GroundingShadowComponent(castsShadow: true)
tvShadow.receivesShadow = false
tv.components.set(tvShadow)
```

Alternatively, you can create a new grounding shadow component instance that opts out of receiving shadows by passing `false` to the `receivesShadow` parameter of the [`init(castsShadow:receivesShadow:)`](groundingshadowcomponent/init(castsshadow:receivesshadow:).md) initializer.

```swift
let robotShadow = GroundingShadowComponent(castsShadow: true,
                                           receivesShadow: false)
robot.components.set(robotShadow)
```

| Receiving shadows | Not receiving shadows |
| --- | --- |
| ![A screenshot of a vintage toy robot on a vintage TV set in a RealityKit scene where the robot casts a shadow onto both the TV that it’s standing on, and onto own body.](https://docs-assets.developer.apple.com/published/8ce34c59e6850c3e45a336650441edec/groundingshadowcomponent-tv-robot-receive-on.jpg) | ![A screenshot of a vintage toy robot on a vintage TV set in a RealityKit scene where the robot doesn’t cast a shadow on any entity in the scene, including itself.](https://docs-assets.developer.apple.com/published/c3a53c8ed1306ca6859138782b48f635/groundingshadowcomponent-tv-robot-receive-off.jpg) |

RealityKit generates grounding shadows from the perspective of another entity that receives the first entity’s shadow. One-sided geometry only casts a shadow if its facets face the entity that receives the shadow, which typically means they face downward. Make each 2D object cast a grounding shadow by applying a material that disables face culling, or by replacing it with a watertight mesh.

## Topics

### Initializers
- [init(castsShadow: Bool)](groundingshadowcomponent/init(castsshadow:).md)
  Creates a grounding shadow component.
- [init(castsShadow: Bool, receivesShadow: Bool)](groundingshadowcomponent/init(castsshadow:receivesshadow:).md)
  Creates a grounding shadow component by configuring whether its entity receives shadows from other model entities with the component.
- [init(castsShadow: Bool, receivesShadow: Bool, fadeBehaviorNearPhysicalObjects: GroundingShadowComponent.FadeBehaviorNearPhysicalObjects)](groundingshadowcomponent/init(castsshadow:receivesshadow:fadebehaviornearphysicalobjects:).md)
  Creates a grounding shadow component by configuring whether its entity receives shadows and its fade behavior near physical objects.
### Instance Properties
- [var castsShadow: Bool](groundingshadowcomponent/castsshadow.md)
  A Boolean value that indicates whether an entity casts a shadow onto other model entities in the scene.
- [var fadeBehaviorNearPhysicalObjects: GroundingShadowComponent.FadeBehaviorNearPhysicalObjects](groundingshadowcomponent/fadebehaviornearphysicalobjects-swift.property.md)
  Configures the grounding shadow’s fade behavior when the entity is near physical objects.
- [var receivesShadow: Bool](groundingshadowcomponent/receivesshadow.md)
  A Boolean value that indicates whether an entity with the grounding shadow component receives grounding shadows from other model entities.
### Enumerations
- [GroundingShadowComponent.FadeBehaviorNearPhysicalObjects](groundingshadowcomponent/fadebehaviornearphysicalobjects-swift.enum.md)
  Describes the behavior of an entity’s grounding shadow when it’s near physical objects.
### Default Implementations
- [Component Implementations](groundingshadowcomponent/component-implementations.md)

## Relationships

### Conforms To
- [Component](component.md)

## See Also

- [struct DynamicLightShadowComponent](dynamiclightshadowcomponent.md)
  A component that controls an entity’s shadow from dynamic (virtual) lights.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/groundingshadowcomponent)*