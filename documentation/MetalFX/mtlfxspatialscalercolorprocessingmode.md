# MTLFXSpatialScalerColorProcessingMode

**Framework**: MetalFX  
**Kind**: enum

The color space modes for the input and output textures you use with a spatial scaling effect instance.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
enum MTLFXSpatialScalerColorProcessingMode
```

## Topics

### Color space modes
- [MTLFXSpatialScalerColorProcessingMode.linear](mtlfxspatialscalercolorprocessingmode/linear.md)
  Indicates your input and output textures use a linear color space.
- [MTLFXSpatialScalerColorProcessingMode.perceptual](mtlfxspatialscalercolorprocessingmode/perceptual.md)
  Indicates your input and output textures use a perceptual color space.
- [MTLFXSpatialScalerColorProcessingMode.hdr](mtlfxspatialscalercolorprocessingmode/hdr.md)
  Indicates your input and output textures use a high dynamic range color space.
### Initializers
- [init?(rawValue: Int)](mtlfxspatialscalercolorprocessingmode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [protocol MTLFXSpatialScaler](mtlfxspatialscaler.md)
  An upscaling effect that generates a higher resolution texture in a render pass by spatially analyzing an input texture.
- [class MTLFXSpatialScalerDescriptor](mtlfxspatialscalerdescriptor.md)
  A set of properties that configure a spatial scaling effect, and a factory method that creates the effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxspatialscalercolorprocessingmode)*