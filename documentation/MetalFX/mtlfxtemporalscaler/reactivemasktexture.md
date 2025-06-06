# reactiveMaskTexture

**Framework**: MetalFX  
**Kind**: property  
**Required**: Yes

A reactive-mask texture input you set for a temporal scaler that supports the correct usage options.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.4+
- tvOS 17.4+

## Declaration

```swift
var reactiveMaskTexture: (any MTLTexture)? { get set }
```

#### Discussion

This texture helps when objects move quickly in a scene with inaccurate motion information, such as when they involve alpha blending. In these situations, you can get better results by guiding MetalFX whether to favor the current frame on a per-pixel basis with a reactive mask texture. Each pixel needs to be in the range `[0.0, 1.0]`, where a value:

- Equal to `0.0` tells MetalFX to follow its normal behavior for the corresponding pixel
- Equal to `1.0` tells MetalFX to ignore temporal history for the corresponding pixel
- In the range `(0.0, 1.0)` proportionally blends the effect for the corresponding pixel

The [`usage`](https://developer.apple.com/documentation/Metal/MTLTexture/usage) property of the texture you set to this property needs to be the same as, or a superset of, the temporal scaling effect’s [`reactiveTextureUsage`](mtlfxtemporalscaler/reactivetextureusage.md) property.

## See Also

- [var reactiveTextureUsage: MTLTextureUsage](mtlfxtemporalscaler/reactivetextureusage.md)
  The minimal texture-usage options that your app’s reactive-mask texture input needs to have for the temporal scaler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxtemporalscaler/reactivemasktexture)*