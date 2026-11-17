# outputTextureFormat

**Framework**: MetalFX  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The pixel format of the output color texture for the temporal scaler.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.11+
- tvOS 27.2+
- visionOS 1.0+

## Declaration

```swift
var outputTextureFormat: MTLPixelFormat { get }
```

```objc
@property (nonatomic, readonly) MTLPixelFormat outputTextureFormat;
```

## See Also

### Inspecting the fixed settings
- [var inputWidth: Int](./inputwidth.md)
  The width, in pixels, of the input color texture for the temporal scaler.
- [var inputHeight: Int](./inputheight.md)
  The height, in pixels, of the input color texture for the temporal scaler.
- [var inputContentMinScale: Float](./inputcontentminscale.md)
  The smallest scale factor the temporal scaler uses to generate output textures.
- [var inputContentMaxScale: Float](./inputcontentmaxscale.md)
  The largest scale factor the temporal scaler uses to generate output textures.
- [var colorTextureFormat: MTLPixelFormat](./colortextureformat.md)
  The pixel format of the input color texture for the temporal scaler.
- [var depthTextureFormat: MTLPixelFormat](./depthtextureformat.md)
  The pixel format of the input depth texture for the temporal scaler.
- [var motionTextureFormat: MTLPixelFormat](./motiontextureformat.md)
  The pixel format of the input motion texture for the temporal scaler.
- [var outputWidth: Int](./outputwidth.md)
  The width, in pixels, of the output color texture for the temporal scaler.
- [var outputHeight: Int](./outputheight.md)
  The height, in pixels, of the output color texture for the temporal scaler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxtemporalscalerbase/outputtextureformat)*