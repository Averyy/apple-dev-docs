# colorTextureUsage

**Framework**: MetalFX  
**Kind**: property  
**Required**: Yes

The minimal texture usage options that your app’s input color texture must set to apply the temporal scaler.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+

## Declaration

```swift
var colorTextureUsage: MTLTextureUsage { get }
```

#### Discussion

The input texture you set to the [`colorTexture`](mtlfxtemporalscaler/colortexture.md) property must use the same set (or a superset) of the [`MTLTextureUsage`](https://developer.apple.com/documentation/Metal/MTLTextureUsage) options in this property.

## See Also

- [var colorTexture: (any MTLTexture)?](mtlfxtemporalscaler/colortexture.md)
  An input color texture you set for the temporal scaler that supports the correct color texture usage options.
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

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxtemporalscaler/colortextureusage)*