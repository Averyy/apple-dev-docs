# preExposure

**Framework**: Metalfx  
**Kind**: property  
**Required**: Yes

The exposure value that you’ve already applied to your color texture input.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+

## Declaration

```swift
var preExposure: Float { get set }
```

#### Discussion

If your app applies an exposure adjustment to your color texture input, set this property to that adjustment value.

> **Note**: Most apps don’t need to set this property, which defaults `1.0`.

The temporal scaler divides each value in the color texture input by this pre-exposure value before it applies any regular exposure adjustments. The regular exposure adjustments either come from the [`exposureTexture`](mtlfxtemporalscaler/exposuretexture.md) property or the temporal scaler’s autoexposure feature (see [`isAutoExposureEnabled`](mtlfxtemporalscalerdescriptor/isautoexposureenabled.md)).

## See Also

- [var colorTextureUsage: MTLTextureUsage](mtlfxtemporalscaler/colortextureusage.md)
  The minimal texture usage options that your app’s input color texture must set to apply the temporal scaler.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/MetalFX/mtlfxtemporalscaler/preexposure)*