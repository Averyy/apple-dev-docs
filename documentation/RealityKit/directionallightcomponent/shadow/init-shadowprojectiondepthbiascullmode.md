# init(shadowProjection:depthBias:cullMode:)

**Framework**: RealityKit  
**Kind**: init

Creates a directional light shadow with a shadow projection, depth bias and cull mode.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
init(shadowProjection: DirectionalLightComponent.Shadow.ShadowProjectionType, depthBias: Float, cullMode: DirectionalLightComponent.Shadow.ShadowMapCullMode? = nil)
```

## Parameters

- `shadowProjection`: The shadow projection used for shadow map rendering.
- `depthBias`: The depth bias for the shadow.
- `cullMode`: The mode used to cull faces when generating the shadow.

## See Also

- [init()](directionallightcomponent/shadow/init.md)
  Creates a directional light shadow using default values.
- [init(maximumDistance: Float, depthBias: Float)](directionallightcomponent/shadow/init(maximumdistance:depthbias:).md)
  Creates a directional light shadow with a maximum distance and depth bias.
- [init(layers: RenderLayer.Set?)](directionallightcomponent/shadow/init(layers:).md)
  Creates a directional light shadow that accepts shadow casters from the specified layers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/directionallightcomponent/shadow/init(shadowprojection:depthbias:cullmode:))*