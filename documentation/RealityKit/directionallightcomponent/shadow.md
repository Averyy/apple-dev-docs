# DirectionalLightComponent.Shadow

**Framework**: RealityKit  
**Kind**: struct

A directional light component that adds shadows to entities that it illuminates

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
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
### Configuring the shadow
- [var depthBias: Float](directionallightcomponent/shadow/depthbias.md)
  A constant value that RealityKit applies as a bias to its shadow calculations.
- [var cullModeOverride: DirectionalLightComponent.Shadow.ShadowMapCullMode?](directionallightcomponent/shadow/cullmodeoverride.md)
  The light’s culling mode for shadow map rendering.
- [var shadowProjection: DirectionalLightComponent.Shadow.ShadowProjectionType](directionallightcomponent/shadow/shadowprojection.md)
  Sets the shadow projection used for shadow map rendering
- [var maximumDistance: Float](directionallightcomponent/shadow/maximumdistance.md)
  The maximum distance for the shadow.
### Registering a component type
- [static func registerComponent()](directionallightcomponent/shadow/registercomponent.md)
  Registers a new component type.
### Comparing shadows
- [static func == (DirectionalLightComponent.Shadow, DirectionalLightComponent.Shadow) -> Bool](directionallightcomponent/shadow/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
- [static func != (Self, Self) -> Bool](directionallightcomponent/shadow/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
### Type Aliases
- [DirectionalLightComponent.Shadow.ShadowMapCullMode](directionallightcomponent/shadow/shadowmapcullmode.md)
### Enumerations
- [DirectionalLightComponent.Shadow.ShadowProjectionType](directionallightcomponent/shadow/shadowprojectiontype.md)
### Default Implementations
- [Component Implementations](directionallightcomponent/shadow/component-implementations.md)
- [Equatable Implementations](directionallightcomponent/shadow/equatable-implementations.md)

## Relationships

### Conforms To
- [Component](component.md)
- [Equatable](../Swift/Equatable.md)

## See Also

- [struct DirectionalLightComponent](directionallightcomponent.md)
  A component that defines a directional light source.
- [DirectionalLightComponent.Shadow.ShadowProjectionType](directionallightcomponent/shadow/shadowprojectiontype.md)
- [DirectionalLightComponent.Shadow.ShadowMapCullMode](directionallightcomponent/shadow/shadowmapcullmode.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/directionallightcomponent/shadow)*