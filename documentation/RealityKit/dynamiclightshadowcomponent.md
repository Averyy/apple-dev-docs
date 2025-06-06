# DynamicLightShadowComponent

**Framework**: RealityKit  
**Kind**: struct

A component that controls an entity’s shadow from dynamic (virtual) lights.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
struct DynamicLightShadowComponent
```

#### Overview

Use `DynamicLightShadowComponent` to control whether an entity casts shadows from dynamic (virtual) lights. Dynamic lights cast shadows on other virtual objects, but not on physical objects. You can add a dynamic light shadow component to any entity that has a [`ModelComponent`](modelcomponent.md) in its component set by adding a dynamic light shadow component to the entity’s [`components`](entity/components.md) property.

```swift
if let model = try? await ModelEntity(named: "tv_retro") {
    let shadowComponent = DynamicLightShadowComponent(castsShadow: false)
    model.components.set(shadowComponent)
}
```

You need to add the dynamic lights shadow component to each entity you want to apply the effect to because the dynamic light shadow component doesn’t apply to hierarchies.

> **Note**: By default, without a dynamic light shadow component, entities cast shadows from dynamic lights.

By default, without a dynamic light shadow component, entities cast shadows from dynamic lights.

## Topics

### Initializers
- [init(castsShadow: Bool)](dynamiclightshadowcomponent/init(castsshadow:).md)
  Creates a dynamic light shadow component.
### Instance Properties
- [var castsShadow: Bool](dynamiclightshadowcomponent/castsshadow.md)
  A Boolean value that indicates whether an entity casts a shadow.
### Default Implementations
- [Component Implementations](dynamiclightshadowcomponent/component-implementations.md)

## Relationships

### Conforms To
- [Component](component.md)

## See Also

- [struct GroundingShadowComponent](groundingshadowcomponent.md)
  A component that controls an entity’s grounding shadow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/dynamiclightshadowcomponent)*