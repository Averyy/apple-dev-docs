# exposureTexture

**Framework**: MetalFX  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A texture that sets the exposure level for the color texture input.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.11+
- tvOS 27.2+
- visionOS 1.0+

## Declaration

```swift
var exposureTexture: (any MTLTexture)? { get set }
```

```objc
@property (nonatomic, retain, nullable) id<MTLTexture> exposureTexture;
```

## Discussion

The property is a texture (unlike [`preExposure`](./preexposure.md)) so that the GPU can directly modify the exposure level for each frame at runtime.

> 💡 **Tip**: For best results, set this property to a texture with a single [`MTLPixelFormat.r16Float`](../../Metal/mtlpixelformat/r16float.md) element.

The temporal scaler uses only the red component of the texture’s first value, at location (0, 0), as the exposure factor. If the property is `nil`, the default exposure factor is `1.0`.

> **Note**: The temporal scaler ignores this property if you create it with a descriptor that has its [`isAutoExposureEnabled`](../mtlfxtemporalscalerdescriptor/isautoexposureenabled.md) property set to [`true`](../../Swift/true.md).

## See Also

### Configuring the image input
- [var colorTextureUsage: MTLTextureUsage](./colortextureusage.md)
  The minimal texture usage options that your app’s input color texture must set to apply the temporal scaler.
- [var colorTexture: (any MTLTexture)?](./colortexture.md)
  An input color texture you set for the temporal scaler that supports the correct color texture usage options.
- [var inputContentWidth: Int](./inputcontentwidth.md)
  The width, in pixels, of the region within the color texture the temporal scaler uses as its input.
- [var inputContentHeight: Int](./inputcontentheight.md)
  The height, in pixels, of the region within the color texture the temporal scaler uses as its input.
- [var jitterOffsetX: Float](./jitteroffsetx.md)
  The horizontal component of the subpixel sampling coordinate you use to generate the color texture input.
- [var jitterOffsetY: Float](./jitteroffsety.md)
  The vertical component of the subpixel sampling coordinate you use to generate the color texture input.
- [var preExposure: Float](./preexposure.md)
  The exposure value that you’ve already applied to your color texture input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxtemporalscalerbase/exposuretexture)*