# isReactiveMaskTextureEnabled

**Framework**: MetalFX  
**Kind**: property

A Boolean value that indicates whether a temporal scaler you create with the descriptor applies a reactive mask.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.4+
- tvOS 17.4+

## Declaration

```swift
var isReactiveMaskTextureEnabled: Bool { get set }
```

## See Also

- [var inputWidth: Int](mtlfxtemporalscalerdescriptor/inputwidth.md)
  The width of the input color texture for the temporal scaler you create with this descriptor.
- [var inputHeight: Int](mtlfxtemporalscalerdescriptor/inputheight.md)
  The height of the input color texture for the temporal scaler you create with this descriptor.
- [var isInputContentPropertiesEnabled: Bool](mtlfxtemporalscalerdescriptor/isinputcontentpropertiesenabled.md)
  A Boolean value that indicates whether the temporal scaler you create with this descriptor uses dynamic resolution.
- [var inputContentMinScale: Float](mtlfxtemporalscalerdescriptor/inputcontentminscale.md)
  The smallest scale factor the temporal scaler you create with this descriptor can use to generate output textures.
- [var inputContentMaxScale: Float](mtlfxtemporalscalerdescriptor/inputcontentmaxscale.md)
  The largest scale factor the temporal scaler you create with this descriptor can use to generate output textures.
- [var colorTextureFormat: MTLPixelFormat](mtlfxtemporalscalerdescriptor/colortextureformat.md)
  The pixel format of the input color texture for the temporal scaler you create with this descriptor.
- [var motionTextureFormat: MTLPixelFormat](mtlfxtemporalscalerdescriptor/motiontextureformat.md)
  The pixel format of the input motion texture for the temporal scaler you create with this descriptor.
- [var depthTextureFormat: MTLPixelFormat](mtlfxtemporalscalerdescriptor/depthtextureformat.md)
  The pixel format of the input depth texture for the temporal scaler you create with this descriptor.
- [var isAutoExposureEnabled: Bool](mtlfxtemporalscalerdescriptor/isautoexposureenabled.md)
  A Boolean value that indicates whether MetalFX calculates the exposure for each frame.
- [var requiresSynchronousInitialization: Bool](mtlfxtemporalscalerdescriptor/requiressynchronousinitialization.md)
  A Boolean value that indicates whether MetalFX compiles a temporal scaling effect’s underlying upscaler as it creates the instance.
- [var reactiveMaskTextureFormat: MTLPixelFormat](mtlfxtemporalscalerdescriptor/reactivemasktextureformat.md)
  The pixel format of the reactive mask input texture for a temporal scaler you create with the descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxtemporalscalerdescriptor/isreactivemasktextureenabled)*