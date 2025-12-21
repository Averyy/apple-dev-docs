# depthBias

**Framework**: RealityKit  
**Kind**: property

A constant value that RealityKit applies as a bias to its shadow calculations.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
var depthBias: Float
```

#### Discussion

Reduce visual effects such as , by adjusting this property. The default value is `1.0`.

## See Also

- [var cullModeOverride: DirectionalLightComponent.Shadow.ShadowMapCullMode?](directionallightcomponent/shadow/cullmodeoverride.md)
  The light’s culling mode for shadow map rendering.
- [var shadowProjection: DirectionalLightComponent.Shadow.ShadowProjectionType](directionallightcomponent/shadow/shadowprojection.md)
  Sets the shadow projection used for shadow map rendering
- [var maximumDistance: Float](directionallightcomponent/shadow/maximumdistance.md)
  The maximum distance for the shadow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/directionallightcomponent/shadow/depthbias)*