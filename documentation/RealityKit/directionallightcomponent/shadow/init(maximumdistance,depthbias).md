# init(maximumDistance:depthBias:)

**Framework**: RealityKit  
**Kind**: init  
**Role**: Initializer

Creates a directional light shadow with a maximum distance and depth bias.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
init(maximumDistance: Float = 5.0, depthBias: Float = 1.0)
```

#### Discussion

The `maximumDistance` parameter in this initializer is equivalent to setting [`shadowProjection`](./shadowprojection.md) to `.automatic(maximumDistance: maximumDistance)`.

## Parameters

- `maximumDistance`: The maximum distance for the shadow.
- `depthBias`: The depth bias for the shadow.

## See Also

### Creating the shadow
- [init()](./init%28%29.md)
  Creates a directional light shadow using default values.
- [init(shadowProjection: DirectionalLightComponent.Shadow.ShadowProjectionType, depthBias: Float, cullMode: DirectionalLightComponent.Shadow.ShadowMapCullMode?)](./init%28shadowprojection,depthbias,cullmode%29.md)
  Creates a directional light shadow with a shadow projection, depth bias and cull mode.
- [init(layers: RenderLayer.Set?)](./init%28layers%29.md)
  Creates a directional light shadow that accepts shadow casters from the specified layers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/directionallightcomponent/shadow/init(maximumdistance:depthbias:))*