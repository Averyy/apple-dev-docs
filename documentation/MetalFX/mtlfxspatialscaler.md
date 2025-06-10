# MTLFXSpatialScaler

**Framework**: MetalFX  
**Kind**: protocol

An upscaling effect that generates a higher resolution texture in a render pass by spatially analyzing an input texture.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
protocol MTLFXSpatialScaler : MTLFXSpatialScalerBase
```

#### Overview

The MetalFX spatial scaler increases the size of your input texture to a larger output texture. You can use the scaler to upscale every frame of your app’s scene or rendering in real time. With a scaler, you can draw more complicated scenes in less time by intentionally rendering to a lower resolution to save time before upscaling.

Create an [`MTLFXSpatialScaler`](mtlfxspatialscaler.md) instance following these steps:

1. Create and configure an [`MTLFXSpatialScalerDescriptor`](mtlfxspatialscalerdescriptor.md) instance.
2. Call the descriptor’s [`makeSpatialScaler(device:)`](mtlfxspatialscalerdescriptor/makespatialscaler(device:).md) method.

Upscale a rendering by following these steps for every render pass:

1. Set the spatial scaler’s `MTLFXSpatialScaler/colorTexture` property to the input texture.
2. Set the scaler’s `MTLFXSpatialScaler/inputContentWidth` and `MTLFXSpatialScaler/inputContentHeight` properties.
3. Set the scaler’s `MTLFXSpatialScaler/outputTexture` property to your destination texture.
4. Encode the upscale commands to an [`MTLCommandBuffer`](https://developer.apple.com/documentation/Metal/MTLCommandBuffer) by calling the spatial scaler’s [`encode(commandBuffer:)`](mtlfxspatialscaler/encode(commandbuffer:).md) method.

## Topics

### Encoding a spatial scaler
- [func encode(commandBuffer: any MTLCommandBuffer)](mtlfxspatialscaler/encode(commandbuffer:).md)
  Adds the spatial scaler to a render pass’s command buffer.

## Relationships

### Inherits From
- [MTLFXSpatialScalerBase](mtlfxspatialscalerbase.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MTLFXSpatialScalerDescriptor](mtlfxspatialscalerdescriptor.md)
  A set of properties that configure a spatial scaling effect, and a factory method that creates the effect.
- [enum MTLFXSpatialScalerColorProcessingMode](mtlfxspatialscalercolorprocessingmode.md)
  The color space modes for the input and output textures you use with a spatial scaling effect instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxspatialscaler)*