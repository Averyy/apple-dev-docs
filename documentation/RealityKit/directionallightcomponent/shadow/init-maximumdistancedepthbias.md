# init(maximumDistance:depthBias:)

**Framework**: RealityKit  
**Kind**: init

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

The `maximumDistance` parameter in this initializer is equivalent to setting [`shadowProjection`](directionallightcomponent/shadow/shadowprojection.md) to `.automatic(maximumDistance: maximumDistance)`.

## Parameters

- `maximumDistance`: The maximum distance for the shadow.
- `depthBias`: The depth bias for the shadow.

## See Also

- [init()](directionallightcomponent/shadow/init.md)
  Creates a directional light shadow using default values.
- [init(shadowProjection: DirectionalLightComponent.Shadow.ShadowProjectionType, depthBias: Float, cullMode: DirectionalLightComponent.Shadow.ShadowMapCullMode?)](directionallightcomponent/shadow/init(shadowprojection:depthbias:cullmode:).md)
  Creates a directional light shadow with a shadow projection, depth bias and cull mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/directionallightcomponent/shadow/init(maximumdistance:depthbias:))*