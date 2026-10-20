# maximumDistance

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

The maximum distance for the shadow.

**Availability**:
- iOS 13.0+ - Deprecated in 18.0
- iPadOS 13.0+ - Deprecated in 18.0
- Mac Catalyst 13.0+ - Deprecated in 18.0
- macOS 10.15+ - Deprecated in 15.0

> **Deprecated**: Use .shadowProjection = .automatic(maximumDistance:)

## Declaration

```swift
var maximumDistance: Float { get set }
```

## See Also

### Configuring the shadow
- [var depthBias: Float](./depthbias.md)
  A constant value that RealityKit applies as a bias to its shadow calculations.
- [var cullModeOverride: DirectionalLightComponent.Shadow.ShadowMapCullMode?](./cullmodeoverride.md)
  The light’s culling mode for shadow map rendering.
- [var shadowProjection: DirectionalLightComponent.Shadow.ShadowProjectionType](./shadowprojection.md)
  Sets the shadow projection used for shadow map rendering


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/directionallightcomponent/shadow/maximumdistance)*