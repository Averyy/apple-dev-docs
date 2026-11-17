# inputContentWidth

**Framework**: MetalFX  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The width, in pixels, of the region within the color texture the temporal scaler uses as its input.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 27.2+
- visionOS 1.0+

## Declaration

```swift
var inputContentWidth: Int { get set }
```

```objc
@property (nonatomic) NSUInteger inputContentWidth;
```

## Discussion

The input content width must be less than or equal to [`inputWidth`](./inputwidth.md).

## See Also

### Configuring the image input
- [var colorTextureUsage: MTLTextureUsage](./colortextureusage.md)
  The minimal texture usage options that your app’s input color texture must set to apply the temporal scaler.
- [var colorTexture: (any MTLTexture)?](./colortexture.md)
  An input color texture you set for the temporal scaler that supports the correct color texture usage options.
- [var inputContentHeight: Int](./inputcontentheight.md)
  The height, in pixels, of the region within the color texture the temporal scaler uses as its input.
- [var jitterOffsetX: Float](./jitteroffsetx.md)
  The horizontal component of the subpixel sampling coordinate you use to generate the color texture input.
- [var jitterOffsetY: Float](./jitteroffsety.md)
  The vertical component of the subpixel sampling coordinate you use to generate the color texture input.
- [var exposureTexture: (any MTLTexture)?](./exposuretexture.md)
  A texture that sets the exposure level for the color texture input.
- [var preExposure: Float](./preexposure.md)
  The exposure value that you’ve already applied to your color texture input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxtemporalscalerbase/inputcontentwidth)*