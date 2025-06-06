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
protocol MTLFXSpatialScaler : NSObjectProtocol
```

#### Overview

The MetalFX spatial scaler increases the size of your input texture to a larger output texture. You can use the scaler to upscale every frame of your app’s scene or rendering in real time. With a scaler, you can draw more complicated scenes in less time by intentionally rendering to a lower resolution to save time before upscaling.

Create an [`MTLFXSpatialScaler`](mtlfxspatialscaler.md) instance following these steps:

1. Create and configure an [`MTLFXSpatialScalerDescriptor`](mtlfxspatialscalerdescriptor.md) instance.
2. Call the descriptor’s [`makeSpatialScaler(device:)`](mtlfxspatialscalerdescriptor/makespatialscaler(device:).md) method.

Upscale a rendering by following these steps for every render pass:

1. Set the spatial scaler’s [`colorTexture`](mtlfxspatialscaler/colortexture.md) property to the input texture.
2. Set the scaler’s [`inputContentWidth`](mtlfxspatialscaler/inputcontentwidth.md) and [`inputContentHeight`](mtlfxspatialscaler/inputcontentheight.md) properties.
3. Set the scaler’s [`outputTexture`](mtlfxspatialscaler/outputtexture.md) property to your destination texture.
4. Encode the upscale commands to an [`MTLCommandBuffer`](https://developer.apple.com/documentation/Metal/MTLCommandBuffer) by calling the spatial scaler’s [`encode(commandBuffer:)`](mtlfxspatialscaler/encode(commandbuffer:).md) method.

## Topics

### Configuring the image input
- [var colorTextureUsage: MTLTextureUsage](mtlfxspatialscaler/colortextureusage.md)
  The minimal texture usage options that your app’s input color texture must set to apply the spatial scaler.
- [var colorTexture: (any MTLTexture)?](mtlfxspatialscaler/colortexture.md)
  An input color texture you set for the spatial scaler that supports the correct color texture usage options.
- [var inputContentWidth: Int](mtlfxspatialscaler/inputcontentwidth.md)
  The width, in pixels, of the region within the color texture the spatial scaler uses as its input.
- [var inputContentHeight: Int](mtlfxspatialscaler/inputcontentheight.md)
  The height, in pixels, of the region within the color texture the spatial scaler uses as its input.
### Configuring the image output
- [var outputTextureUsage: MTLTextureUsage](mtlfxspatialscaler/outputtextureusage.md)
  The minimal texture usage options that your app’s output texture must set to apply the spatial scaler.
- [var outputTexture: (any MTLTexture)?](mtlfxspatialscaler/outputtexture.md)
  An output texture that supports the correct depth texture usage options.
### Synchronizing untracked resources
- [var fence: (any MTLFence)?](mtlfxspatialscaler/fence.md)
  An optional fence instance that you provide to synchronize your app’s untracked resources.
### Encoding a spatial scaler
- [func encode(commandBuffer: any MTLCommandBuffer)](mtlfxspatialscaler/encode(commandbuffer:).md)
  Adds the spatial scaler to a render pass’s command buffer.
### Inspecting the fixed settings
- [var inputWidth: Int](mtlfxspatialscaler/inputwidth.md)
  The width, in pixels, of the input color texture for the spatial scaler.
- [var inputHeight: Int](mtlfxspatialscaler/inputheight.md)
  The height, in pixels, of the input color texture for the spatial scaler.
- [var colorTextureFormat: MTLPixelFormat](mtlfxspatialscaler/colortextureformat.md)
  The pixel format of the input color texture for the spatial scaler.
- [var colorProcessingMode: MTLFXSpatialScalerColorProcessingMode](mtlfxspatialscaler/colorprocessingmode.md)
  Reflects the color processing mode you set in this spatial scaler’s descriptor.
- [var outputWidth: Int](mtlfxspatialscaler/outputwidth.md)
  The width, in pixels, of the output color texture for the spatial scaler.
- [var outputHeight: Int](mtlfxspatialscaler/outputheight.md)
  The height, in pixels, of the output color texture for the spatial scaler.
- [var outputTextureFormat: MTLPixelFormat](mtlfxspatialscaler/outputtextureformat.md)
  The pixel format of the output color texture for the spatial scaler.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MTLFXSpatialScalerDescriptor](mtlfxspatialscalerdescriptor.md)
  A set of properties that configure a spatial scaling effect, and a factory method that creates the effect.
- [enum MTLFXSpatialScalerColorProcessingMode](mtlfxspatialscalercolorprocessingmode.md)
  The color space modes for the input and output textures you use with a spatial scaling effect instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxspatialscaler)*