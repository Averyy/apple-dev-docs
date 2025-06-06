# motionTexture

**Framework**: MetalFX  
**Kind**: property  
**Required**: Yes

An input motion texture you set for the temporal scaler that supports the correct motion texture usage options.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+

## Declaration

```swift
var motionTexture: (any MTLTexture)? { get set }
```

#### Discussion

The texture you set to this property must meet the following requirements:

- The texture’s [`usage`](https://developer.apple.com/documentation/Metal/MTLTexture/usage) property must use the same [`MTLTextureUsage`](https://developer.apple.com/documentation/Metal/MTLTextureUsage) options as (or be a superset of) the temporal scaling effect’s [`motionTextureUsage`](mtlfxtemporalscaler/motiontextureusage.md) property.
- The texture’s dimensions must be equal to the [`inputWidth`](mtlfxtemporalscaler/inputwidth.md) and [`inputHeight`](mtlfxtemporalscaler/inputheight.md) properties.

## See Also

- [var motionTextureUsage: MTLTextureUsage](mtlfxtemporalscaler/motiontextureusage.md)
  The minimal texture usage options that your app’s input motion texture must set to apply the temporal scaler.
- [var motionVectorScaleX: Float](mtlfxtemporalscaler/motionvectorscalex.md)
  The horizontal scale factor the temporal scaler applies to the input motion texture.
- [var motionVectorScaleY: Float](mtlfxtemporalscaler/motionvectorscaley.md)
  The vertical scale factor the temporal scaler applies to the input motion texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxtemporalscaler/motiontexture)*