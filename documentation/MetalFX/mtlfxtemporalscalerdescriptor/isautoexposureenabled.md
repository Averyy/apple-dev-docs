# isAutoExposureEnabled

**Framework**: MetalFX  
**Kind**: property

A Boolean value that indicates whether MetalFX calculates the exposure for each frame.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+

## Declaration

```swift
var isAutoExposureEnabled: Bool { get set }
```

#### Discussion

Set this property to [`true`](https://developer.apple.com/documentation/swift/true) to create a temporal scaler that automatically calculates the exposure level for each image it scales.

> **Note**: Temporal scaler instances that use auto exposure ignore its `MTLFXTemporalScaler/exposureTexture` property.

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
- [var requiresSynchronousInitialization: Bool](mtlfxtemporalscalerdescriptor/requiressynchronousinitialization.md)
  A Boolean value that indicates whether MetalFX compiles a temporal scaling effect’s underlying upscaler as it creates the instance.
- [var isReactiveMaskTextureEnabled: Bool](mtlfxtemporalscalerdescriptor/isreactivemasktextureenabled.md)
  A Boolean value that indicates whether a temporal scaler you create with the descriptor applies a reactive mask.
- [var reactiveMaskTextureFormat: MTLPixelFormat](mtlfxtemporalscalerdescriptor/reactivemasktextureformat.md)
  The pixel format of the reactive mask input texture for a temporal scaler you create with the descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxtemporalscalerdescriptor/isautoexposureenabled)*