# motionTextureFormat

**Framework**: MetalFX  
**Kind**: property  
**Required**: Yes

The pixel format of the input motion texture for the temporal scaler.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+

## Declaration

```swift
var motionTextureFormat: MTLPixelFormat { get }
```

## See Also

- [var inputWidth: Int](mtlfxtemporalscaler/inputwidth.md)
  The width, in pixels, of the input color texture for the temporal scaler.
- [var inputHeight: Int](mtlfxtemporalscaler/inputheight.md)
  The height, in pixels, of the input color texture for the temporal scaler.
- [var inputContentMinScale: Float](mtlfxtemporalscaler/inputcontentminscale.md)
  The smallest scale factor the temporal scaler uses to generate output textures.
- [var inputContentMaxScale: Float](mtlfxtemporalscaler/inputcontentmaxscale.md)
  The largest scale factor the temporal scaler uses to generate output textures.
- [var colorTextureFormat: MTLPixelFormat](mtlfxtemporalscaler/colortextureformat.md)
  The pixel format of the input color texture for the temporal scaler.
- [var depthTextureFormat: MTLPixelFormat](mtlfxtemporalscaler/depthtextureformat.md)
  The pixel format of the input depth texture for the temporal scaler.
- [var outputWidth: Int](mtlfxtemporalscaler/outputwidth.md)
  The width, in pixels, of the output color texture for the temporal scaler.
- [var outputHeight: Int](mtlfxtemporalscaler/outputheight.md)
  The height, in pixels, of the output color texture for the temporal scaler.
- [var outputTextureFormat: MTLPixelFormat](mtlfxtemporalscaler/outputtextureformat.md)
  The pixel format of the output color texture for the temporal scaler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxtemporalscaler/motiontextureformat)*