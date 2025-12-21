# MTLFXTemporalDenoisedScalerDescriptor

**Framework**: MetalFX  
**Kind**: class

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 26.0+
- tvOS 18.0+

## Declaration

```swift
class MTLFXTemporalDenoisedScalerDescriptor
```

## Topics

### Instance Properties
- [var colorTextureFormat: MTLPixelFormat](mtlfxtemporaldenoisedscalerdescriptor/colortextureformat.md)
  The pixel format of the input color texture for the scaler you create with this descriptor.
- [var denoiseStrengthMaskTextureFormat: MTLPixelFormat](mtlfxtemporaldenoisedscalerdescriptor/denoisestrengthmasktextureformat.md)
  The pixel format of the input denoise strength mask texture for the scaler you create with this descriptor.
- [var depthTextureFormat: MTLPixelFormat](mtlfxtemporaldenoisedscalerdescriptor/depthtextureformat.md)
  The pixel format of the input depth texture for the scaler you create with this descriptor.
- [var diffuseAlbedoTextureFormat: MTLPixelFormat](mtlfxtemporaldenoisedscalerdescriptor/diffusealbedotextureformat.md)
  The pixel format of the input diffuse albedo texture for the scaler you create with this descriptor.
- [var inputHeight: Int](mtlfxtemporaldenoisedscalerdescriptor/inputheight.md)
  The height, in pixels, of the input color texture for the denoiser scaler.
- [var inputWidth: Int](mtlfxtemporaldenoisedscalerdescriptor/inputwidth.md)
  The width, in pixels, of the input color texture for the denoiser scaler.
- [var isAutoExposureEnabled: Bool](mtlfxtemporaldenoisedscalerdescriptor/isautoexposureenabled.md)
  A Boolean value that indicates whether MetalFX calculates the exposure for each frame.
- [var isDenoiseStrengthMaskTextureEnabled: Bool](mtlfxtemporaldenoisedscalerdescriptor/isdenoisestrengthmasktextureenabled.md)
  A Boolean value indicating whether the scaler evaluates a denoise strength mask texture as part of its operation.
- [var isReactiveMaskTextureEnabled: Bool](mtlfxtemporaldenoisedscalerdescriptor/isreactivemasktextureenabled.md)
  A Boolean value that indicates whether a scaler you create from this descriptor applies a reactive mask.
- [var isSpecularHitDistanceTextureEnabled: Bool](mtlfxtemporaldenoisedscalerdescriptor/isspecularhitdistancetextureenabled.md)
  A Boolean value indicating whether the scaler evaluates a specular hit distance texture as part of its operation.
- [var isTransparencyOverlayTextureEnabled: Bool](mtlfxtemporaldenoisedscalerdescriptor/istransparencyoverlaytextureenabled.md)
  A Boolean value indicating whether the scaler evaluates a transparency overlay texture as part of its operation.
- [var motionTextureFormat: MTLPixelFormat](mtlfxtemporaldenoisedscalerdescriptor/motiontextureformat.md)
  The pixel format of the input motion texture for the scaler you create with this descriptor.
- [var normalTextureFormat: MTLPixelFormat](mtlfxtemporaldenoisedscalerdescriptor/normaltextureformat.md)
  The pixel format of the input normal texture for the scaler you create with this descriptor.
- [var outputHeight: Int](mtlfxtemporaldenoisedscalerdescriptor/outputheight.md)
  The height, in pixels, of the input color texture for the denoiser scaler.
- [var outputTextureFormat: MTLPixelFormat](mtlfxtemporaldenoisedscalerdescriptor/outputtextureformat.md)
  The pixel format of the output color texture for the scaler you create with this descriptor.
- [var outputWidth: Int](mtlfxtemporaldenoisedscalerdescriptor/outputwidth.md)
  The width, in pixels, of the output color texture for the denoiser scaler.
- [var reactiveMaskTextureFormat: MTLPixelFormat](mtlfxtemporaldenoisedscalerdescriptor/reactivemasktextureformat.md)
  The pixel format of the reactive mask input texture for a scaler you create from this descriptor.
- [var requiresSynchronousInitialization: Bool](mtlfxtemporaldenoisedscalerdescriptor/requiressynchronousinitialization.md)
  A Boolean value that indicates whether MetalFX compiles a temporal scaling effect’s underlying upscaler as it creates the instance.
- [var roughnessTextureFormat: MTLPixelFormat](mtlfxtemporaldenoisedscalerdescriptor/roughnesstextureformat.md)
  The pixel format of the input roughness texture for the scaler you create with this descriptor.
- [var specularAlbedoTextureFormat: MTLPixelFormat](mtlfxtemporaldenoisedscalerdescriptor/specularalbedotextureformat.md)
  The pixel format of the input specular albedo texture for the scaler you create with this descriptor.
- [var specularHitDistanceTextureFormat: MTLPixelFormat](mtlfxtemporaldenoisedscalerdescriptor/specularhitdistancetextureformat.md)
  The pixel format of the input specular hit texture for the scaler you create with this descriptor.
- [var transparencyOverlayTextureFormat: MTLPixelFormat](mtlfxtemporaldenoisedscalerdescriptor/transparencyoverlaytextureformat.md)
  The pixel format of the input transparency overlay texture for the scaler you create with this descriptor.
### Instance Methods
- [func makeTemporalDenoisedScaler(device: any MTLDevice) -> (any MTLFXTemporalDenoisedScaler)?](mtlfxtemporaldenoisedscalerdescriptor/maketemporaldenoisedscaler(device:).md)
  Creates a denoiser scaler instance for a Metal device.
- [func makeTemporalDenoisedScaler(device: any MTLDevice, compiler: any MTL4Compiler) -> (any MTL4FXTemporalDenoisedScaler)?](mtlfxtemporaldenoisedscalerdescriptor/maketemporaldenoisedscaler(device:compiler:).md)
  Creates a denoiser scaler instance for a Metal device.
### Type Methods
- [class func supportedInputContentMaxScale(device: any MTLDevice) -> Float](mtlfxtemporaldenoisedscalerdescriptor/supportedinputcontentmaxscale(device:).md)
  Returns the largest temporal scaling factor the device supports as a floating-point value.
- [class func supportedInputContentMinScale(device: any MTLDevice) -> Float](mtlfxtemporaldenoisedscalerdescriptor/supportedinputcontentminscale(device:).md)
  Returns the smallest temporal scaling factor the device supports as a floating-point value.
- [class func supportsDevice(any MTLDevice) -> Bool](mtlfxtemporaldenoisedscalerdescriptor/supportsdevice(_:).md)
  Queries whether a Metal device supports denoising scaling.
- [class func supportsMetal4FX(any MTLDevice) -> Bool](mtlfxtemporaldenoisedscalerdescriptor/supportsmetal4fx(_:).md)
  Queries whether a Metal device supports denosing scaling compatible on Metal 4.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxtemporaldenoisedscalerdescriptor)*