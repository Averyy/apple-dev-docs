# shadowProjection

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

Sets the shadow projection used for shadow map rendering

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
var shadowProjection: DirectionalLightComponent.Shadow.ShadowProjectionType { get set }
```

## See Also

### Configuring the shadow
- [var depthBias: Float](./depthbias.md)
  A constant value that RealityKit applies as a bias to its shadow calculations.
- [var cullModeOverride: DirectionalLightComponent.Shadow.ShadowMapCullMode?](./cullmodeoverride.md)
  The light’s culling mode for shadow map rendering.
- [var maximumDistance: Float](./maximumdistance.md)
  The maximum distance for the shadow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/directionallightcomponent/shadow/shadowprojection)*