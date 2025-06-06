# MTLFXSpatialScalerDescriptor

**Framework**: MetalFX  
**Kind**: class

A set of properties that configure a spatial scaling effect, and a factory method that creates the effect.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
class MTLFXSpatialScalerDescriptor
```

## Topics

### Checking a GPU device’s scaling support
- [class func supportsDevice(any MTLDevice) -> Bool](mtlfxspatialscalerdescriptor/supportsdevice(_:).md)
  Returns a Boolean value that indicates whether the spatial scaler works with a GPU.
### Configuring a spatial scaler’s input
- [var inputWidth: Int](mtlfxspatialscalerdescriptor/inputwidth.md)
  The width of the input color texture for the spatial scaler you create with this descriptor.
- [var inputHeight: Int](mtlfxspatialscalerdescriptor/inputheight.md)
  The height of the input color texture for the spatial scaler you create with this descriptor.
- [var colorTextureFormat: MTLPixelFormat](mtlfxspatialscalerdescriptor/colortextureformat.md)
  The pixel format of the input color texture for the spatial scaler you create with this descriptor.
- [var colorProcessingMode: MTLFXSpatialScalerColorProcessingMode](mtlfxspatialscalerdescriptor/colorprocessingmode.md)
  The color space of the input color texture for the spatial scaler you create with this descriptor.
### Configuring a spatial scaler’s output
- [var outputWidth: Int](mtlfxspatialscalerdescriptor/outputwidth.md)
  The width of the output color texture for the spatial scaler you create with this descriptor.
- [var outputHeight: Int](mtlfxspatialscalerdescriptor/outputheight.md)
  The height of the output color texture for the spatial scaler you create with this descriptor.
- [var outputTextureFormat: MTLPixelFormat](mtlfxspatialscalerdescriptor/outputtextureformat.md)
  The pixel format of the output color texture for the spatial scaler you create with this descriptor.
### Creating spatial scaler instances
- [func makeSpatialScaler(device: any MTLDevice) -> (any MTLFXSpatialScaler)?](mtlfxspatialscalerdescriptor/makespatialscaler(device:).md)
  Creates a spatial scaler instance from this descriptor’s current property values.

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

## See Also

- [protocol MTLFXSpatialScaler](mtlfxspatialscaler.md)
  An upscaling effect that generates a higher resolution texture in a render pass by spatially analyzing an input texture.
- [enum MTLFXSpatialScalerColorProcessingMode](mtlfxspatialscalercolorprocessingmode.md)
  The color space modes for the input and output textures you use with a spatial scaling effect instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxspatialscalerdescriptor)*