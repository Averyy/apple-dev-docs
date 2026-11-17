# inputContentMinScale

**Framework**: MetalFX  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The smallest scale factor the temporal scaler uses to generate output textures.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 27.2+
- visionOS 1.0+

## Declaration

```swift
var inputContentMinScale: Float { get }
```

```objc
@property (nonatomic, readonly) float inputContentMinScale;
```

## See Also

### Inspecting the fixed settings
- [var inputWidth: Int](./inputwidth.md)
  The width, in pixels, of the input color texture for the temporal scaler.
- [var inputHeight: Int](./inputheight.md)
  The height, in pixels, of the input color texture for the temporal scaler.
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
- [var outputTextureFormat: MTLPixelFormat](./outputtextureformat.md)
  The pixel format of the output color texture for the temporal scaler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxtemporalscalerbase/inputcontentminscale)*