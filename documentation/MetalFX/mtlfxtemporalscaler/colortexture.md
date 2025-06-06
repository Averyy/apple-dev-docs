# colorTexture

**Framework**: MetalFX  
**Kind**: property  
**Required**: Yes

An input color texture you set for the temporal scaler that supports the correct color texture usage options.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+

## Declaration

```swift
var colorTexture: (any MTLTexture)? { get set }
```

#### Discussion

The texture you set to this property must meet the following requirements:

- The texture’s [`usage`](https://developer.apple.com/documentation/Metal/MTLTexture/usage) property must use the same [`MTLTextureUsage`](https://developer.apple.com/documentation/Metal/MTLTextureUsage) options as (or be a superset of) the temporal scaling effect’s [`colorTextureUsage`](mtlfxtemporalscaler/colortextureusage.md) property.
- The texture’s dimensions must be equal to the [`inputWidth`](mtlfxtemporalscaler/inputwidth.md) and [`inputHeight`](mtlfxtemporalscaler/inputheight.md) properties.

## See Also

- [var colorTextureUsage: MTLTextureUsage](mtlfxtemporalscaler/colortextureusage.md)
  The minimal texture usage options that your app’s input color texture must set to apply the temporal scaler.
- [var inputContentWidth: Int](mtlfxtemporalscaler/inputcontentwidth.md)
  The width, in pixels, of the region within the color texture the temporal scaler uses as its input.
- [var inputContentHeight: Int](mtlfxtemporalscaler/inputcontentheight.md)
  The height, in pixels, of the region within the color texture the temporal scaler uses as its input.
- [var jitterOffsetX: Float](mtlfxtemporalscaler/jitteroffsetx.md)
  The horizontal component of the subpixel sampling coordinate you use to generate the color texture input.
- [var jitterOffsetY: Float](mtlfxtemporalscaler/jitteroffsety.md)
  The vertical component of the subpixel sampling coordinate you use to generate the color texture input.
- [var exposureTexture: (any MTLTexture)?](mtlfxtemporalscaler/exposuretexture.md)
  A texture that sets the exposure level for the color texture input.
- [var preExposure: Float](mtlfxtemporalscaler/preexposure.md)
  The exposure value that you’ve already applied to your color texture input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxtemporalscaler/colortexture)*