# MTLFXSpatialScalerBase

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
protocol MTLFXSpatialScalerBase : NSObjectProtocol
```

```objc
@protocol MTLFXSpatialScalerBase <NSObject>
```

## Overview

The MetalFX spatial scaler increases the size of your input texture to a larger output texture. You can use the scaler to upscale every frame of your app’s scene or rendering in real time. With a scaler, you can draw more complicated scenes in less time by intentionally rendering to a lower resolution to save time before upscaling.

Create an [`MTLFXSpatialScaler`](./mtlfxspatialscaler.md) instance following these steps:

1. Create and configure an [`MTLFXSpatialScalerDescriptor`](./mtlfxspatialscalerdescriptor.md) instance.
2. Call the descriptor’s `newSpatialScalerWithDevice:` method.

Upscale a rendering by following these steps for every render pass:

1. Set the spatial scaler’s [`colorTexture`](./mtlfxspatialscalerbase/colortexture.md) property to the input texture.
2. Set the scaler’s [`inputContentWidth`](./mtlfxspatialscalerbase/inputcontentwidth.md) and [`inputContentHeight`](./mtlfxspatialscalerbase/inputcontentheight.md) properties.
3. Set the scaler’s [`outputTexture`](./mtlfxspatialscalerbase/outputtexture.md) property to your destination texture.

Encode the upscale commands to a command buffer by calling the spatial scaler’s `encodeToCommandBuffer:` method.

## Conforming to texture usage requirements

Spatial scalers expose properties, such as [`colorTextureUsage`](./mtlfxspatialscalerbase/colortextureusage.md), that indicate requirements for your textures to be compatible with it. These properties indicate the minimum set of `MTLTextureUsage` bits that you are responsible for setting in your texture descriptors for this spatial scaler to use them.

Your game or app can set extra usage bits on your textures without losing compatibility, as long at its maintains the minimum set the scaler requests.

## Assigning input and output textures

When you use an instance of a class that conforms to this protocol, you typically set its input and output textures, as well as other properties, and then encode its work to a command buffer.

MetalFX doesn’t track that you assign the same texture instances to each property across different batches of work, the only requirement is that you provide textures that match the pixel formats and dimensions you specify in the [`MTLFXSpatialScalerDescriptor`](./mtlfxspatialscalerdescriptor.md) descriptor instance that creates the scaler instance.

## Topics

### Instance Properties
- [var colorProcessingMode: MTLFXSpatialScalerColorProcessingMode](./mtlfxspatialscalerbase/colorprocessingmode.md)
  Reflects the color processing mode you set in this spatial scaler’s descriptor.
- [var colorTexture: (any MTLTexture)?](./mtlfxspatialscalerbase/colortexture.md)
  An input color texture you set for the spatial scaler that supports the correct color texture usage options.
- [var colorTextureFormat: MTLPixelFormat](./mtlfxspatialscalerbase/colortextureformat.md)
  The pixel format of the input color texture for the spatial scaler.
- [var colorTextureUsage: MTLTextureUsage](./mtlfxspatialscalerbase/colortextureusage.md)
  The minimal texture usage options that your app’s input color texture must set to apply the spatial scaler.
- [var fence: (any MTLFence)?](./mtlfxspatialscalerbase/fence.md)
  An optional fence instance that you provide to synchronize your app’s untracked resources.
- [var inputContentHeight: Int](./mtlfxspatialscalerbase/inputcontentheight.md)
  The height, in pixels, of the region within the color texture the spatial scaler uses as its input.
- [var inputContentWidth: Int](./mtlfxspatialscalerbase/inputcontentwidth.md)
  The width, in pixels, of the region within the color texture the spatial scaler uses as its input.
- [var inputHeight: Int](./mtlfxspatialscalerbase/inputheight.md)
  The height, in pixels, of the input color texture for the spatial scaler.
- [var inputWidth: Int](./mtlfxspatialscalerbase/inputwidth.md)
  The width, in pixels, of the input color texture for the spatial scaler.
- [var outputHeight: Int](./mtlfxspatialscalerbase/outputheight.md)
  The height, in pixels, of the output color texture for the spatial scaler.
- [var outputTexture: (any MTLTexture)?](./mtlfxspatialscalerbase/outputtexture.md)
  An output texture that supports the correct depth texture usage options.
- [var outputTextureFormat: MTLPixelFormat](./mtlfxspatialscalerbase/outputtextureformat.md)
  The pixel format of the output color texture for the spatial scaler.
- [var outputTextureUsage: MTLTextureUsage](./mtlfxspatialscalerbase/outputtextureusage.md)
  The minimal texture usage options that your app’s output texture must set to apply the spatial scaler.
- [var outputWidth: Int](./mtlfxspatialscalerbase/outputwidth.md)
  The width, in pixels, of the output color texture for the spatial scaler.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Inherited By
- [MTL4FXSpatialScaler](./mtl4fxspatialscaler.md)
- [MTLFXSpatialScaler](./mtlfxspatialscaler.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxspatialscalerbase)*