# init(layers:)

**Framework**: RealityKit  
**Kind**: init  
**Role**: Initializer

Creates a directional light shadow that accepts shadow casters from the specified layers.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
init(layers: RenderLayer.Set? = nil)
```

## Parameters

- `layers`: The layers of entities that cast shadows from this light. Pass `nil` (the default) to inherit [`layers`](../layers.md), or an empty set to disable shadow casting entirely.

## See Also

### Creating the shadow
- [init()](./init%28%29.md)
  Creates a directional light shadow using default values.
- [init(shadowProjection: DirectionalLightComponent.Shadow.ShadowProjectionType, depthBias: Float, cullMode: DirectionalLightComponent.Shadow.ShadowMapCullMode?)](./init%28shadowprojection,depthbias,cullmode%29.md)
  Creates a directional light shadow with a shadow projection, depth bias and cull mode.
- [init(maximumDistance: Float, depthBias: Float)](./init%28maximumdistance,depthbias%29.md)
  Creates a directional light shadow with a maximum distance and depth bias.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/directionallightcomponent/shadow/init(layers:))*