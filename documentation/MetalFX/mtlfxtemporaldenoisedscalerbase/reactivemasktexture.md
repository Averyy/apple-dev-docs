# reactiveMaskTexture

**Framework**: MetalFX  
**Kind**: property  
**Required**: Yes

A reactive-mask texture input for this scaler to evaluate.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var reactiveMaskTexture: (any MTLTexture)? { get set }
```

#### Discussion

This texture helps guide the denoiser when objects move quickly in a scene with inaccurate motion information, such as when they involve alpha blending. In these situations, you can get better results by guiding MetalFX whether to favor the current frame on a per-pixel basis with a reactive mask texture.

When providing this texture, you are responsible for ensuring each pixel is in the range `[0.0, 1.0]`, where a value:

- Equal to `0.0` tells MetalFX to follow its normal behavior for the corresponding pixel
- Equal to `1.0` tells MetalFX to ignore temporal history for the corresponding pixel
- In the range `(0.0, 1.0)` proportionally blends the effect for the corresponding pixel


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxtemporaldenoisedscalerbase/reactivemasktexture)*