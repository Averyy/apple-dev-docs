# requiresSynchronousInitialization

**Framework**: MetalFX  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether MetalFX compiles a temporal scaling effect’s underlying upscaler as it creates the instance.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 27.1+

## Declaration

```swift
var requiresSynchronousInitialization: Bool { get set }
```

```objc
@property (nonatomic, readwrite) BOOL requiresSynchronousInitialization;
```

## Overview

This property gives you the option to decide when it’s better for your app to give MetalFX the time it needs to compile the underlying upscaler of the temporal scaling effect. The two choices are:

- As you create the effect
- After you create the effect, likely when your app needs to upscale the initial textures

You can create a `MFXTemporalScalingEffect` instance that can upscale textures at its best speed immediately after you create it by setting this property to [`true`](../../Swift/true.md) and then calling the [`makeTemporalScaler(device:)`](./maketemporalscaler%28device%29.md) method. However, it may take the framework more time for that method to return while the framework creates the temporal scaling effect and compiles its underlying scaler.

By default, the property is equal to [`false`](../../Swift/false.md), which tells MetalFX to quickly create and return the temporal scaling-effect instance, and then compile a faster upscaler in the background. However, this means the effect can take more time to upscale textures while the framework compiles the underlying upscaler. When the framework finishes compiling, the effect runs just as fast as if you set the property to `true`.

> **Note**: The image quality of the effect’s output texture is consistent, whether it’s using the slower interim upscaler or the final, faster upscaler.

## See Also

### Configuring a temporal effect’s input
- [var inputWidth: Int](./inputwidth.md)
  The width of the input color texture for the temporal scaler you create with this descriptor.
- [var inputHeight: Int](./inputheight.md)
  The height of the input color texture for the temporal scaler you create with this descriptor.
- [var isInputContentPropertiesEnabled: Bool](./isinputcontentpropertiesenabled.md)
  A Boolean value that indicates whether the temporal scaler you create with this descriptor uses dynamic resolution.
- [var inputContentMinScale: Float](./inputcontentminscale.md)
  The smallest scale factor the temporal scaler you create with this descriptor can use to generate output textures.
- [var inputContentMaxScale: Float](./inputcontentmaxscale.md)
  The largest scale factor the temporal scaler you create with this descriptor can use to generate output textures.
- [var colorTextureFormat: MTLPixelFormat](./colortextureformat.md)
  The pixel format of the input color texture for the temporal scaler you create with this descriptor.
- [var motionTextureFormat: MTLPixelFormat](./motiontextureformat.md)
  The pixel format of the input motion texture for the temporal scaler you create with this descriptor.
- [var depthTextureFormat: MTLPixelFormat](./depthtextureformat.md)
  The pixel format of the input depth texture for the temporal scaler you create with this descriptor.
- [var isAutoExposureEnabled: Bool](./isautoexposureenabled.md)
  A Boolean value that indicates whether MetalFX calculates the exposure for each frame.
- [var isReactiveMaskTextureEnabled: Bool](./isreactivemasktextureenabled.md)
  A Boolean value that indicates whether a temporal scaler you create with the descriptor applies a reactive mask.
- [var reactiveMaskTextureFormat: MTLPixelFormat](./reactivemasktextureformat.md)
  The pixel format of the reactive mask input texture for a temporal scaler you create with the descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxtemporalscalerdescriptor/requiressynchronousinitialization)*