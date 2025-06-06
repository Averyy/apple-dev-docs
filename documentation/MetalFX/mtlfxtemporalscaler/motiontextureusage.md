# motionTextureUsage

**Framework**: MetalFX  
**Kind**: property  
**Required**: Yes

The minimal texture usage options that your app’s input motion texture must set to apply the temporal scaler.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+

## Declaration

```swift
var motionTextureUsage: MTLTextureUsage { get }
```

#### Discussion

The input texture you set to the [`motionTexture`](mtlfxtemporalscaler/motiontexture.md) property must use the same set (or a superset) of the [`MTLTextureUsage`](https://developer.apple.com/documentation/Metal/MTLTextureUsage) options in this property.

## See Also

- [var motionTexture: (any MTLTexture)?](mtlfxtemporalscaler/motiontexture.md)
  An input motion texture you set for the temporal scaler that supports the correct motion texture usage options.
- [var motionVectorScaleX: Float](mtlfxtemporalscaler/motionvectorscalex.md)
  The horizontal scale factor the temporal scaler applies to the input motion texture.
- [var motionVectorScaleY: Float](mtlfxtemporalscaler/motionvectorscaley.md)
  The vertical scale factor the temporal scaler applies to the input motion texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxtemporalscaler/motiontextureusage)*