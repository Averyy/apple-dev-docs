# exposureTexture

**Framework**: MetalFX  
**Kind**: property  
**Required**: Yes

A texture that sets the exposure level for the color texture input.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+

## Declaration

```swift
var exposureTexture: (any MTLTexture)? { get set }
```

#### Discussion

The property is a texture (unlike [`preExposure`](mtlfxtemporalscaler/preexposure.md)) so that the GPU can directly modify the exposure level for each frame at runtime.

> 💡 **Tip**: For best results, set this property to a texture with a single [`MTLPixelFormat.r16Float`](https://developer.apple.com/documentation/Metal/MTLPixelFormat/r16Float) element.

For best results, set this property to a texture with a single [`MTLPixelFormat.r16Float`](https://developer.apple.com/documentation/Metal/MTLPixelFormat/r16Float) element.

The temporal scaler uses only the red component of the texture’s first value, at location (0, 0), as the exposure factor. If the property is `nil`, the default exposure factor is `1.0`.

> **Note**: The temporal scaler ignores this property if you create it with a descriptor that has its [`isAutoExposureEnabled`](mtlfxtemporalscalerdescriptor/isautoexposureenabled.md) property set to [`true`](https://developer.apple.com/documentation/swift/true).

The temporal scaler ignores this property if you create it with a descriptor that has its [`isAutoExposureEnabled`](mtlfxtemporalscalerdescriptor/isautoexposureenabled.md) property set to [`true`](https://developer.apple.com/documentation/swift/true).

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
- [var preExposure: Float](mtlfxtemporalscaler/preexposure.md)
  The exposure value that you’ve already applied to your color texture input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxtemporalscaler/exposuretexture)*