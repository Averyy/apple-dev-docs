# reactiveMaskTexture

**Framework**: MetalFX  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A reactive-mask texture input you set for a temporal scaler that supports the correct usage options.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.11+
- tvOS 27.2+
- visionOS 1.0+

## Declaration

```swift
var reactiveMaskTexture: (any MTLTexture)? { get set }
```

```objc
@property (nonatomic, retain, nullable) id<MTLTexture> reactiveMaskTexture;
```

## Discussion

This texture helps when objects move quickly in a scene with inaccurate motion information, such as when they involve alpha blending. In these situations, you can get better results by guiding MetalFX whether to favor the current frame on a per-pixel basis with a reactive mask texture. Each pixel needs to be in the range `[0.0, 1.0]`, where a value:

- Equal to `0.0` tells MetalFX to follow its normal behavior for the corresponding pixel
- Equal to `1.0` tells MetalFX to ignore temporal history for the corresponding pixel
- In the range `(0.0, 1.0)` proportionally blends the effect for the corresponding pixel

The [`usage`](../../Metal/mtltexture/usage.md) property of the texture you set to this property needs to be the same as, or a superset of, the temporal scaling effect’s [`reactiveTextureUsage`](./reactivetextureusage.md) property.

## See Also

### Configuring the reactive mask input
- [var reactiveTextureUsage: MTLTextureUsage](./reactivetextureusage.md)
  The minimal texture-usage options that your app’s reactive-mask texture input needs to have for the temporal scaler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxtemporalscalerbase/reactivemasktexture)*