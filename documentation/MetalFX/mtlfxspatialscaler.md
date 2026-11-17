# MTLFXSpatialScaler

**Framework**: MetalFX  
**Kind**: protocol  
**Role**: Protocol

An upscaling effect that generates a higher resolution texture in a render pass by spatially analyzing an input texture.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 27.2+
- visionOS 1.0+

## Declaration

```swift
protocol MTLFXSpatialScaler : MTLFXSpatialScalerBase
```

```objc
@protocol MTLFXSpatialScaler <MTLFXSpatialScalerBase>
```

## Overview

The MetalFX spatial scaler increases the size of your input texture to a larger output texture. You can use the scaler to upscale every frame of your app’s scene or rendering in real time. With a scaler, you can draw more complicated scenes in less time by intentionally rendering to a lower resolution to save time before upscaling.

Create an [`MTLFXSpatialScaler`](./mtlfxspatialscaler.md) instance following these steps:

1. Create and configure an [`MTLFXSpatialScalerDescriptor`](./mtlfxspatialscalerdescriptor.md) instance.
2. Call the descriptor’s [`makeSpatialScaler(device:)`](./mtlfxspatialscalerdescriptor/makespatialscaler%28device%29.md) method.

Upscale a rendering by following these steps for every render pass:

1. Set the spatial scaler’s [`colorTexture`](./mtlfxspatialscalerbase/colortexture.md) property to the input texture.
2. Set the scaler’s [`inputContentWidth`](./mtlfxspatialscalerbase/inputcontentwidth.md) and [`inputContentHeight`](./mtlfxspatialscalerbase/inputcontentheight.md) properties.
3. Set the scaler’s [`outputTexture`](./mtlfxspatialscalerbase/outputtexture.md) property to your destination texture.
4. Encode the upscale commands to an [`MTLCommandBuffer`](../Metal/mtlcommandbuffer.md) by calling the spatial scaler’s [`encode(commandBuffer:)`](./mtlfxspatialscaler/encode%28commandbuffer%29.md) method.

## Topics

### Configuring the image input
- [var colorTextureUsage: MTLTextureUsage](./mtlfxspatialscalerbase/colortextureusage.md)
  The minimal texture usage options that your app’s input color texture must set to apply the spatial scaler.
- [var colorTexture: (any MTLTexture)?](./mtlfxspatialscalerbase/colortexture.md)
  An input color texture you set for the spatial scaler that supports the correct color texture usage options.
- [var inputContentWidth: Int](./mtlfxspatialscalerbase/inputcontentwidth.md)
  The width, in pixels, of the region within the color texture the spatial scaler uses as its input.
- [var inputContentHeight: Int](./mtlfxspatialscalerbase/inputcontentheight.md)
  The height, in pixels, of the region within the color texture the spatial scaler uses as its input.
### Configuring the image output
- [var outputTextureUsage: MTLTextureUsage](./mtlfxspatialscalerbase/outputtextureusage.md)
  The minimal texture usage options that your app’s output texture must set to apply the spatial scaler.
- [var outputTexture: (any MTLTexture)?](./mtlfxspatialscalerbase/outputtexture.md)
  An output texture that supports the correct depth texture usage options.
### Synchronizing untracked resources
- [var fence: (any MTLFence)?](./mtlfxspatialscalerbase/fence.md)
  An optional fence instance that you provide to synchronize your app’s untracked resources.
### Encoding a spatial scaler
- [func encode(commandBuffer: any MTLCommandBuffer)](./mtlfxspatialscaler/encode%28commandbuffer%29.md)
  Adds the spatial scaler to a render pass’s command buffer.
### Inspecting the fixed settings
- [var inputWidth: Int](./mtlfxspatialscalerbase/inputwidth.md)
  The width, in pixels, of the input color texture for the spatial scaler.
- [var inputHeight: Int](./mtlfxspatialscalerbase/inputheight.md)
  The height, in pixels, of the input color texture for the spatial scaler.
- [var colorTextureFormat: MTLPixelFormat](./mtlfxspatialscalerbase/colortextureformat.md)
  The pixel format of the input color texture for the spatial scaler.
- [var colorProcessingMode: MTLFXSpatialScalerColorProcessingMode](./mtlfxspatialscalerbase/colorprocessingmode.md)
  Reflects the color processing mode you set in this spatial scaler’s descriptor.
- [var outputWidth: Int](./mtlfxspatialscalerbase/outputwidth.md)
  The width, in pixels, of the output color texture for the spatial scaler.
- [var outputHeight: Int](./mtlfxspatialscalerbase/outputheight.md)
  The height, in pixels, of the output color texture for the spatial scaler.
- [var outputTextureFormat: MTLPixelFormat](./mtlfxspatialscalerbase/outputtextureformat.md)
  The pixel format of the output color texture for the spatial scaler.

## Relationships

### Inherits From
- [MTLFXSpatialScalerBase](./mtlfxspatialscalerbase.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Spatial scaling
- [class MTLFXSpatialScalerDescriptor](./mtlfxspatialscalerdescriptor.md)
  A set of properties that configure a spatial scaling effect, and a factory method that creates the effect.
- [enum MTLFXSpatialScalerColorProcessingMode](./mtlfxspatialscalercolorprocessingmode.md)
  The color space modes for the input and output textures you use with a spatial scaling effect instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxspatialscaler)*