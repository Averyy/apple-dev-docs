# motionVectorScaleY

**Framework**: MetalFX  
**Kind**: property  
**Required**: Yes

The vertical scale factor the temporal scaler applies to the input motion texture.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+

## Declaration

```swift
var motionVectorScaleY: Float { get set }
```

#### Discussion

The scaler converts the vertical component of each value in [`motionTexture`](mtlfxtemporalscaler/motiontexture.md) into fragment (pixel) coordinates by multiplying it by this property’s value.

## See Also

- [var motionTextureUsage: MTLTextureUsage](mtlfxtemporalscaler/motiontextureusage.md)
  The minimal texture usage options that your app’s input motion texture must set to apply the temporal scaler.
- [var motionTexture: (any MTLTexture)?](mtlfxtemporalscaler/motiontexture.md)
  An input motion texture you set for the temporal scaler that supports the correct motion texture usage options.
- [var motionVectorScaleX: Float](mtlfxtemporalscaler/motionvectorscalex.md)
  The horizontal scale factor the temporal scaler applies to the input motion texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxtemporalscaler/motionvectorscaley)*