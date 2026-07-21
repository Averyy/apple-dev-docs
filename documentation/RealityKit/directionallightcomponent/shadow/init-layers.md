# init(layers:)

**Framework**: RealityKit  
**Kind**: init

Creates a directional light shadow that accepts shadow casters from the specified layers.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(layers: RenderLayer.Set? = nil)
```

## Parameters

- `layers`: The layers of entities that cast shadows from this light. Pass `nil` (the default) to inherit [`layers`](directionallightcomponent/layers.md), or an empty set to disable shadow casting entirely.

## See Also

- [init()](directionallightcomponent/shadow/init.md)
  Creates a directional light shadow using default values.
- [init(shadowProjection: DirectionalLightComponent.Shadow.ShadowProjectionType, depthBias: Float, cullMode: DirectionalLightComponent.Shadow.ShadowMapCullMode?)](directionallightcomponent/shadow/init(shadowprojection:depthbias:cullmode:).md)
  Creates a directional light shadow with a shadow projection, depth bias and cull mode.
- [init(maximumDistance: Float, depthBias: Float)](directionallightcomponent/shadow/init(maximumdistance:depthbias:).md)
  Creates a directional light shadow with a maximum distance and depth bias.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/directionallightcomponent/shadow/init(layers:))*