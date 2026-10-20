# DirectionalLightComponent.Shadow

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

A directional light component that adds shadows to entities that it illuminates

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
struct Shadow
```

## Topics

### Creating the shadow
- [init()](./shadow/init%28%29.md)
  Creates a directional light shadow using default values.
- [init(shadowProjection: DirectionalLightComponent.Shadow.ShadowProjectionType, depthBias: Float, cullMode: DirectionalLightComponent.Shadow.ShadowMapCullMode?)](./shadow/init%28shadowprojection,depthbias,cullmode%29.md)
  Creates a directional light shadow with a shadow projection, depth bias and cull mode.
- [init(maximumDistance: Float, depthBias: Float)](./shadow/init%28maximumdistance,depthbias%29.md)
  Creates a directional light shadow with a maximum distance and depth bias.
- [init(layers: RenderLayer.Set?)](./shadow/init%28layers%29.md)
  Creates a directional light shadow that accepts shadow casters from the specified layers.
### Configuring the shadow
- [var depthBias: Float](./shadow/depthbias.md)
  A constant value that RealityKit applies as a bias to its shadow calculations.
- [var cullModeOverride: DirectionalLightComponent.Shadow.ShadowMapCullMode?](./shadow/cullmodeoverride.md)
  The light’s culling mode for shadow map rendering.
- [var shadowProjection: DirectionalLightComponent.Shadow.ShadowProjectionType](./shadow/shadowprojection.md)
  Sets the shadow projection used for shadow map rendering
- [var maximumDistance: Float](./shadow/maximumdistance.md)
  The maximum distance for the shadow.
### Specifying affected layers
- [var layers: RenderLayer.Set?](./shadow/layers.md)
  The layers of entities that cast shadows from this light.
### Configuring shadow cascades
- [var cascades: DirectionalLightComponent.Shadow.Cascades](./shadow/cascades-swift.property.md)
  Number of shadow cascades to use when rendering shadows for this light.
- [DirectionalLightComponent.Shadow.Cascades](./shadow/cascades-swift.struct.md)
### Type Aliases
- [DirectionalLightComponent.Shadow.ShadowMapCullMode](./shadow/shadowmapcullmode.md)
### Enumerations
- [DirectionalLightComponent.Shadow.ShadowProjectionType](./shadow/shadowprojectiontype.md)

## Relationships

### Conforms To
- [Component](../component.md)
- [Equatable](../../Swift/equatable.md)

## See Also

### Directional lights and their shadows
- [struct DirectionalLightComponent](../directionallightcomponent.md)
  A component that defines a directional light source.
- [DirectionalLightComponent.Shadow.ShadowProjectionType](./shadow/shadowprojectiontype.md)
- [DirectionalLightComponent.Shadow.ShadowMapCullMode](./shadow/shadowmapcullmode.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/directionallightcomponent/shadow)*