# MTLFXTemporalScalerDescriptor

**Framework**: MetalFX  
**Kind**: class  
**Role**: Class

A set of properties that configure a temporal scaling effect, and a factory method that creates the effect.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 27.1+

## Declaration

```swift
class MTLFXTemporalScalerDescriptor
```

```objc
@interface MTLFXTemporalScalerDescriptor : NSObject
```

## Topics

### Checking a GPU device’s scaling support
- [class func supportsDevice(any MTLDevice) -> Bool](./mtlfxtemporalscalerdescriptor/supportsdevice%28_%29.md)
  Returns a Boolean value that indicates whether the temporal scaler works with a GPU.
- [class func supportedInputContentMinScale(device: any MTLDevice) -> Float](./mtlfxtemporalscalerdescriptor/supportedinputcontentminscale%28device%29.md)
  Returns the smallest temporal scaling factor the device supports as a floating-point value.
- [class func supportedInputContentMaxScale(device: any MTLDevice) -> Float](./mtlfxtemporalscalerdescriptor/supportedinputcontentmaxscale%28device%29.md)
  Returns the largest temporal scaling factor the device supports as a floating-point value.
### Configuring a temporal effect’s input
- [var inputWidth: Int](./mtlfxtemporalscalerdescriptor/inputwidth.md)
  The width of the input color texture for the temporal scaler you create with this descriptor.
- [var inputHeight: Int](./mtlfxtemporalscalerdescriptor/inputheight.md)
  The height of the input color texture for the temporal scaler you create with this descriptor.
- [var isInputContentPropertiesEnabled: Bool](./mtlfxtemporalscalerdescriptor/isinputcontentpropertiesenabled.md)
  A Boolean value that indicates whether the temporal scaler you create with this descriptor uses dynamic resolution.
- [var inputContentMinScale: Float](./mtlfxtemporalscalerdescriptor/inputcontentminscale.md)
  The smallest scale factor the temporal scaler you create with this descriptor can use to generate output textures.
- [var inputContentMaxScale: Float](./mtlfxtemporalscalerdescriptor/inputcontentmaxscale.md)
  The largest scale factor the temporal scaler you create with this descriptor can use to generate output textures.
- [var colorTextureFormat: MTLPixelFormat](./mtlfxtemporalscalerdescriptor/colortextureformat.md)
  The pixel format of the input color texture for the temporal scaler you create with this descriptor.
- [var motionTextureFormat: MTLPixelFormat](./mtlfxtemporalscalerdescriptor/motiontextureformat.md)
  The pixel format of the input motion texture for the temporal scaler you create with this descriptor.
- [var depthTextureFormat: MTLPixelFormat](./mtlfxtemporalscalerdescriptor/depthtextureformat.md)
  The pixel format of the input depth texture for the temporal scaler you create with this descriptor.
- [var isAutoExposureEnabled: Bool](./mtlfxtemporalscalerdescriptor/isautoexposureenabled.md)
  A Boolean value that indicates whether MetalFX calculates the exposure for each frame.
- [var requiresSynchronousInitialization: Bool](./mtlfxtemporalscalerdescriptor/requiressynchronousinitialization.md)
  A Boolean value that indicates whether MetalFX compiles a temporal scaling effect’s underlying upscaler as it creates the instance.
- [var isReactiveMaskTextureEnabled: Bool](./mtlfxtemporalscalerdescriptor/isreactivemasktextureenabled.md)
  A Boolean value that indicates whether a temporal scaler you create with the descriptor applies a reactive mask.
- [var reactiveMaskTextureFormat: MTLPixelFormat](./mtlfxtemporalscalerdescriptor/reactivemasktextureformat.md)
  The pixel format of the reactive mask input texture for a temporal scaler you create with the descriptor.
### Configuring a temporal effect’s output
- [var outputWidth: Int](./mtlfxtemporalscalerdescriptor/outputwidth.md)
  The width of the output color texture for the temporal scaler you create with this descriptor.
- [var outputHeight: Int](./mtlfxtemporalscalerdescriptor/outputheight.md)
  The height of the output color texture for the temporal scaler you create with this descriptor.
- [var outputTextureFormat: MTLPixelFormat](./mtlfxtemporalscalerdescriptor/outputtextureformat.md)
  The pixel format of the output color texture for the temporal scaler you create with this descriptor.
### Creating temporal scaling effect instances
- [func makeTemporalScaler(device: any MTLDevice) -> (any MTLFXTemporalScaler)?](./mtlfxtemporalscalerdescriptor/maketemporalscaler%28device%29.md)
  Creates a temporal scaler instance from this descriptor’s current property values.
### Instance Properties
- [var isJitteredMotionVectorsEnabled: Bool](./mtlfxtemporalscalerdescriptor/isjitteredmotionvectorsenabled.md)
  A Boolean value that indicates whether the motion vectors include the jittering pattern.
- [var isOutputResolutionMotionVectorsEnabled: Bool](./mtlfxtemporalscalerdescriptor/isoutputresolutionmotionvectorsenabled.md)
  A Boolean value that indicates whether the scaler expects motion vectors at output resolution.
### Instance Methods
- [func makeTemporalScaler(device: any MTLDevice, compiler: any MTL4Compiler) -> (any MTL4FXTemporalScaler)?](./mtlfxtemporalscalerdescriptor/maketemporalscaler%28device,compiler%29.md)
  Creates a temporal scaler instance for a Metal device.
### Type Methods
- [class func supportsMetal4FX(any MTLDevice) -> Bool](./mtlfxtemporalscalerdescriptor/supportsmetal4fx%28_%29.md)
  Queries whether a Metal device supports temporal scaling compatible with Metal 4.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Temporal scaling
- [Applying temporal antialiasing and upscaling using MetalFX](./applying-temporal-antialiasing-and-upscaling-using-metalfx.md)
  Reduce render workloads while increasing image detail with MetalFX.
- [protocol MTLFXTemporalScaler](./mtlfxtemporalscaler.md)
  An upscaling effect that generates a higher resolution texture in a render pass by analyzing multiple input textures over time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxtemporalscalerdescriptor)*