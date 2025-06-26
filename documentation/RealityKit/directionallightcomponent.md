# DirectionalLightComponent

**Framework**: RealityKit  
**Kind**: struct

A component that defines a directional light source.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
struct DirectionalLightComponent
```

#### Overview

A directional light shines in the entity’s forward direction `[0, 0, -1]`.

Change the a directional light’s direction with the `Entity/orientation` or [`look(at:from:upVector:relativeTo:)`](hastransform/look(at:from:upvector:relativeto:).md) method of the [`Entity`](entity.md) with a `DirectionalLightComponent`. The position of the entity does not play a part in the directional light’s effect.

> 💡 **Tip**: Turn on shadows for a directional light by adding the [`DirectionalLightComponent.Shadow`](directionallightcomponent/shadow.md) component to an entity that has a `DirectionalLightComponent`.

Use this component with shadows by adding `DirectionalLightComponent` and [`DirectionalLightComponent.Shadow`](directionallightcomponent/shadow.md) to an entity’s [`components`](entity/components.md) set. In this example, the light’s color is red, and the intensity is `10_000`, which is an approximate lux for ambient daylight:

```swift
let lightEntity = Entity()

let redLightComponent = DirectionalLightComponent(
    color: .red, intensity: 10_000
)
let lightShadowComponent = DirectionalLightComponent.Shadow()
lightEntity.components.set([redLightComponent, lightShadowComponent])
```

The directional light illuminates entities evenly in the direction it derives from the orientation of `lightEntity`. Here is a visual example of how the above code snippet could illuminates entities in a scene:

| Without a directional light | With a directional light |
| --- | --- |
| ![A screenshot of a RealityKit scene with a dark gray floor, a light gray cube. There is no obvious lighting in the scene, so the edges of the cube are not clear.](https://docs-assets.developer.apple.com/published/e8b038bfa7b07c3d0dcacbd9fc181188/directionallight-cube-off.jpg) | ![A screenshot of a RealityKit scene with a dark gray floor, a light gray cube, and five small green arrows in a row above the cube. There is a red light uniformly affecting the scene from above, casting a shadow to the right of the cube.](https://docs-assets.developer.apple.com/published/f01ce460b71220e95e8772c713bd9d84/directionallight-cube-on.jpg) |

> **Note**: The green arrows in the above illustration are only a visual representation of the light’s direction.

## Topics

### Creating a directional light
- [init(color: DirectionalLightComponent.Color, intensity: Float)](directionallightcomponent/init(color:intensity:).md)
  Creates a directional light with a configuration.
- [init(color: DirectionalLightComponent.Color, intensity: Float, isRealWorldProxy: Bool)](directionallightcomponent/init(color:intensity:isrealworldproxy:)-d4x3.md)
  Creates a directional light with a configuration.
- [init(color: DirectionalLightComponent.Color, intensity: Float, isRealWorldProxy: Bool)](directionallightcomponent/init(color:intensity:isrealworldproxy:)-hbe.md)
  Creates a directional light with a configuration.
### Setting the color
- [var color: DirectionalLightComponent.Color](directionallightcomponent/color-3q6ln.md)
  A color for the directional light.
- [var color: DirectionalLightComponent.Color](directionallightcomponent/color-2a2x9.md)
  A color for the directional light.
### Setting intensity and shadows
- [var intensity: Float](directionallightcomponent/intensity.md)
  The intensity of the directional light, measured in lumen per square meter.
- [var isRealWorldProxy: Bool](directionallightcomponent/isrealworldproxy.md)
  A Boolean that you use to control whether the directional light operates as a proxy for a real-world light.
### Structures
- [DirectionalLightComponent.Shadow](directionallightcomponent/shadow.md)
  A directional light component that adds shadows to entities that it illuminates
### Initializers
- [init(color:intensity:isRealWorldProxy:)](directionallightcomponent/init(color:intensity:isrealworldproxy:).md)
  Creates a directional light with a configuration.
### Instance Properties
- [var color: DirectionalLightComponent.Color](directionallightcomponent/color-7hs4n.md)
  A color for the directional light.
### Type Aliases
- [DirectionalLightComponent.Color](directionallightcomponent/color-26h21.md)
  A platform-specific type used to define color for a directional light.
- [DirectionalLightComponent.Color](directionallightcomponent/color-3iw1j.md)
  A platform-specific type used to define color for a directional light.

## Relationships

### Conforms To
- [Component](component.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)

## See Also

- [DirectionalLightComponent.Shadow](directionallightcomponent/shadow.md)
  A directional light component that adds shadows to entities that it illuminates


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/directionallightcomponent)*