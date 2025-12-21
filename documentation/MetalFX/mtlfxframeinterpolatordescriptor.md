# MTLFXFrameInterpolatorDescriptor

**Framework**: MetalFX  
**Kind**: class

A set of properties that configure a frame interpolator, and a factory method that creates the effect.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
class MTLFXFrameInterpolatorDescriptor
```

#### Overview

A frame interpolator inspects two frames your game or app renders and, based on their properties, generates an extra frame at a fraction of the cost, helping you to increase your frame rate.

When you configure this descriptor, set the properties that determine the pixel format for each texture to the respective format of the texture you later assign to the scaler. For example, make sure that the format to which you set the [`colorTextureFormat`](mtlfxframeinterpolatordescriptor/colortextureformat.md) property matches the format of the texture you later assign to the interpolator’s `MTLFXFrameInterpolatorDescriptor/colorTexture` property.

## Topics

### Instance Properties
- [var colorTextureFormat: MTLPixelFormat](mtlfxframeinterpolatordescriptor/colortextureformat.md)
  The pixel format of the input color texture for the frame interpolator you create with this descriptor.
- [var depthTextureFormat: MTLPixelFormat](mtlfxframeinterpolatordescriptor/depthtextureformat.md)
  The pixel format of the input depth texture for the frame interpolator you create with this descriptor.
- [var inputHeight: Int](mtlfxframeinterpolatordescriptor/inputheight.md)
  The height, in pixels, of the input motion and depth texture for the frame interpolator.
- [var inputWidth: Int](mtlfxframeinterpolatordescriptor/inputwidth.md)
  The width, in pixels, of the input motion and depth texture for the frame interpolator.
- [var motionTextureFormat: MTLPixelFormat](mtlfxframeinterpolatordescriptor/motiontextureformat.md)
  The pixel format of the input motion texture for the frame interpolator you create with this descriptor.
- [var outputHeight: Int](mtlfxframeinterpolatordescriptor/outputheight.md)
  The height, in pixels, of the output color texture for the frame interpolator.
- [var outputTextureFormat: MTLPixelFormat](mtlfxframeinterpolatordescriptor/outputtextureformat.md)
  The pixel format of the output color texture for the frame interpolator you create with this descriptor.
- [var outputWidth: Int](mtlfxframeinterpolatordescriptor/outputwidth.md)
  The width, in pixels, of the output color texture for the frame interpolator.
- [var scaler: (any MTLFXFrameInterpolatableScaler)?](mtlfxframeinterpolatordescriptor/scaler.md)
- [var uiTextureFormat: MTLPixelFormat](mtlfxframeinterpolatordescriptor/uitextureformat.md)
  The pixel format for the frame interpolator of an input texture containing your game’s custom UI.
### Instance Methods
- [func makeFrameInterpolator(device: any MTLDevice) -> (any MTLFXFrameInterpolator)?](mtlfxframeinterpolatordescriptor/makeframeinterpolator(device:).md)
  Creates a frame interpolator instance for a Metal device.
- [func makeFrameInterpolator(device: any MTLDevice, compiler: any MTL4Compiler) -> (any MTL4FXFrameInterpolator)?](mtlfxframeinterpolatordescriptor/makeframeinterpolator(device:compiler:).md)
  Creates a frame interpolator instance for a Metal device.
### Type Methods
- [class func supportsDevice(any MTLDevice) -> Bool](mtlfxframeinterpolatordescriptor/supportsdevice(_:).md)
  Queries whether a Metal device supports frame interpolation.
- [class func supportsMetal4FX(any MTLDevice) -> Bool](mtlfxframeinterpolatordescriptor/supportsmetal4fx(_:).md)
  Queries whether a Metal device supports frame interpolation compatible with a Metal 4 command buffer.

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

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxframeinterpolatordescriptor)*