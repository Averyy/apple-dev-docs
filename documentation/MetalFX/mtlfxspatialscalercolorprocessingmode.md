# MTLFXSpatialScalerColorProcessingMode

**Framework**: MetalFX  
**Kind**: enum  
**Role**: Enumeration

The color space modes for the input and output textures you use with a spatial scaling effect instance.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 27.1+
- visionOS 1.0+

## Declaration

```swift
enum MTLFXSpatialScalerColorProcessingMode
```

```c
enum MTLFXSpatialScalerColorProcessingMode : NSInteger;
```

## Topics

### Color space modes
- [MTLFXSpatialScalerColorProcessingMode.linear](./mtlfxspatialscalercolorprocessingmode/linear.md)
  Indicates your input and output textures use a linear color space.
- [MTLFXSpatialScalerColorProcessingMode.perceptual](./mtlfxspatialscalercolorprocessingmode/perceptual.md)
  Indicates your input and output textures use a perceptual color space.
- [MTLFXSpatialScalerColorProcessingMode.hdr](./mtlfxspatialscalercolorprocessingmode/hdr.md)
  Indicates your input and output textures use a high dynamic range color space.
### Initializers
- [init?(rawValue: Int)](./mtlfxspatialscalercolorprocessingmode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Spatial scaling
- [protocol MTLFXSpatialScaler](./mtlfxspatialscaler.md)
  An upscaling effect that generates a higher resolution texture in a render pass by spatially analyzing an input texture.
- [class MTLFXSpatialScalerDescriptor](./mtlfxspatialscalerdescriptor.md)
  A set of properties that configure a spatial scaling effect, and a factory method that creates the effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxspatialscalercolorprocessingmode)*