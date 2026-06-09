# portalSize

**Framework**: RealityKit  
**Kind**: property

The portal entity size in meters.

**Availability**:
- visionOS 27.0+ (Beta)

## Declaration

```swift
var portalSize: SIMD2<Float> { get set }
```

#### Discussion

This property has the format `[width, height]`. Defaults to [1.0, 0.5625] to have 16:9 aspect ratio. This is not available for Spatial Videos.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/videoplayercomponent/portalsize)*