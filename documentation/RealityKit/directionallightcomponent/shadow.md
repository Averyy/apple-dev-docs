# DirectionalLightComponent.Shadow

**Framework**: RealityKit  
**Kind**: struct

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
- [init()](directionallightcomponent/shadow/init.md)
  Creates a directional light shadow using default values.
- [init(shadowProjection: DirectionalLightComponent.Shadow.ShadowProjectionType, depthBias: Float, cullMode: DirectionalLightComponent.Shadow.ShadowMapCullMode?)](directionallightcomponent/shadow/init(shadowprojection:depthbias:cullmode:).md)
  Creates a directional light shadow with a shadow projection, depth bias and cull mode.
- [init(maximumDistance: Float, depthBias: Float)](directionallightcomponent/shadow/init(maximumdistance:depthbias:).md)
  Creates a directional light shadow with a maximum distance and depth bias.
- [init(layers: RenderLayer.Set?)](directionallightcomponent/shadow/init(layers:).md)
  Creates a directional light shadow that accepts shadow casters from the specified layers.
### Configuring the shadow
- [var depthBias: Float](directionallightcomponent/shadow/depthbias.md)
  A constant value that RealityKit applies as a bias to its shadow calculations.
- [var cullModeOverride: DirectionalLightComponent.Shadow.ShadowMapCullMode?](directionallightcomponent/shadow/cullmodeoverride.md)
  The light’s culling mode for shadow map rendering.
- [var shadowProjection: DirectionalLightComponent.Shadow.ShadowProjectionType](directionallightcomponent/shadow/shadowprojection.md)
  Sets the shadow projection used for shadow map rendering
- [var maximumDistance: Float](directionallightcomponent/shadow/maximumdistance.md)
  The maximum distance for the shadow.
### Specifying affected layers
- [var layers: RenderLayer.Set?](directionallightcomponent/shadow/layers.md)
  The layers of entities that cast shadows from this light.
### Configuring shadow cascades
- [var cascades: DirectionalLightComponent.Shadow.Cascades](directionallightcomponent/shadow/cascades-swift.property.md)
  Number of shadow cascades to use when rendering shadows for this light.
- [DirectionalLightComponent.Shadow.Cascades](directionallightcomponent/shadow/cascades-swift.struct.md)
### Type Aliases
- [DirectionalLightComponent.Shadow.ShadowMapCullMode](directionallightcomponent/shadow/shadowmapcullmode.md)
### Enumerations
- [DirectionalLightComponent.Shadow.ShadowProjectionType](directionallightcomponent/shadow/shadowprojectiontype.md)

## Relationships

### Conforms To
- [Component](component.md)
- [Equatable](../swift/equatable.md)

## See Also

- [struct DirectionalLightComponent](directionallightcomponent.md)
  A component that defines a directional light source.
- [DirectionalLightComponent.Shadow.ShadowProjectionType](directionallightcomponent/shadow/shadowprojectiontype.md)
- [DirectionalLightComponent.Shadow.ShadowMapCullMode](directionallightcomponent/shadow/shadowmapcullmode.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/directionallightcomponent/shadow)*