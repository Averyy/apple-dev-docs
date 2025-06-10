# DirectionalLightComponent.Shadow

**Framework**: RealityKit  
**Kind**: struct

A directional light component that adds shadows to entities that it illuminates

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
struct Shadow
```

## Topics

### Creating the shadow
- [init()](directionallightcomponent/shadow/init.md)
  Creates a directional light shadow using default values.
- [init(shadowProjection:depthBias:cullMode:)](directionallightcomponent/shadow/init(shadowprojection:depthbias:cullmode:).md)
  Creates a directional light shadow with a shadow projection, depth bias and cull mode.
- [init(maximumDistance: Float, depthBias: Float)](directionallightcomponent/shadow/init(maximumdistance:depthbias:).md)
  Creates a directional light shadow with a maximum distance and depth bias.
### Configuring the shadow
- [var depthBias: Float](directionallightcomponent/shadow/depthbias.md)
  A constant value that RealityKit applies as a bias to its shadow calculations.
- [var maximumDistance: Float](directionallightcomponent/shadow/maximumdistance.md)
  The maximum distance for the shadow.
### Instance Properties
- [var cullModeOverride: DirectionalLightComponent.Shadow.ShadowMapCullMode?](directionallightcomponent/shadow/cullmodeoverride-9scrz.md)
  The light’s culling mode for shadow map rendering.
- [var cullModeOverride: DirectionalLightComponent.Shadow.ShadowMapCullMode?](directionallightcomponent/shadow/cullmodeoverride-ga2r.md)
  The light’s culling mode for shadow map rendering.
- [var shadowProjection: DirectionalLightComponent.Shadow.ShadowProjectionType](directionallightcomponent/shadow/shadowprojection-3je1g.md)
  Sets the shadow projection used for shadow map rendering
- [var shadowProjection: DirectionalLightComponent.Shadow.ShadowProjectionType](directionallightcomponent/shadow/shadowprojection-4la8b.md)
  Sets the shadow projection used for shadow map rendering
### Type Aliases
- [DirectionalLightComponent.Shadow.ShadowMapCullMode](directionallightcomponent/shadow/shadowmapcullmode-2j2li.md)
- [DirectionalLightComponent.Shadow.ShadowMapCullMode](directionallightcomponent/shadow/shadowmapcullmode-441hn.md)
### Enumerations
- [DirectionalLightComponent.Shadow.ShadowProjectionType](directionallightcomponent/shadow/shadowprojectiontype-1h04e.md)
- [DirectionalLightComponent.Shadow.ShadowProjectionType](directionallightcomponent/shadow/shadowprojectiontype-8pbl5.md)

## Relationships

### Conforms To
- [Component](component.md)
- [Equatable](../Swift/Equatable.md)

## See Also

- [struct DirectionalLightComponent](directionallightcomponent.md)
  A component that defines a directional light source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/directionallightcomponent/shadow)*