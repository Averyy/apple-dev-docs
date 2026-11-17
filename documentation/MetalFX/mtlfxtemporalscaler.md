# MTLFXTemporalScaler

**Framework**: MetalFX  
**Kind**: protocol  
**Role**: Protocol

An upscaling effect that generates a higher resolution texture in a render pass by analyzing multiple input textures over time.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 27.2+

## Declaration

```swift
protocol MTLFXTemporalScaler : MTLFXTemporalScalerBase
```

```objc
@protocol MTLFXTemporalScaler <MTLFXTemporalScalerBase>
```

## Overview

The MetalFX temporal scaler increases the size of your input texture to a larger output texture. You can use the scaler to upscale every frame of your app’s scene or rendering in real time. With a scaler, you can draw more complicated scenes in less time by intentionally rendering to a lower resolution to save time before upscaling.

Create an [`MTLFXTemporalScaler`](./mtlfxtemporalscaler.md) instance by following these steps:

1. Create and configure an [`MTLFXTemporalScalerDescriptor`](./mtlfxtemporalscalerdescriptor.md) instance.
2. Call the descriptor’s [`makeTemporalScaler(device:)`](./mtlfxtemporalscalerdescriptor/maketemporalscaler%28device%29.md) method.

Upscale a rendering by following these steps for every render pass:

1. Set the temporal scaler’s [`colorTexture`](./mtlfxtemporalscalerbase/colortexture.md) property to the input texture.
2. Set the scaler’s [`inputContentWidth`](./mtlfxtemporalscalerbase/inputcontentwidth.md) and [`inputContentHeight`](./mtlfxtemporalscalerbase/inputcontentheight.md) properties.
3. Set the scaler’s [`outputTexture`](./mtlfxtemporalscalerbase/outputtexture.md) property to your destination texture.
4. Encode the upscale commands to an [`MTLCommandBuffer`](../Metal/mtlcommandbuffer.md) by calling the temporal scaler’s [`encode(commandBuffer:)`](./mtlfxtemporalscaler/encode%28commandbuffer%29.md) method.

## Topics

### Configuring the image input
- [var colorTextureUsage: MTLTextureUsage](./mtlfxtemporalscalerbase/colortextureusage.md)
  The minimal texture usage options that your app’s input color texture must set to apply the temporal scaler.
- [var colorTexture: (any MTLTexture)?](./mtlfxtemporalscalerbase/colortexture.md)
  An input color texture you set for the temporal scaler that supports the correct color texture usage options.
- [var inputContentWidth: Int](./mtlfxtemporalscalerbase/inputcontentwidth.md)
  The width, in pixels, of the region within the color texture the temporal scaler uses as its input.
- [var inputContentHeight: Int](./mtlfxtemporalscalerbase/inputcontentheight.md)
  The height, in pixels, of the region within the color texture the temporal scaler uses as its input.
- [var jitterOffsetX: Float](./mtlfxtemporalscalerbase/jitteroffsetx.md)
  The horizontal component of the subpixel sampling coordinate you use to generate the color texture input.
- [var jitterOffsetY: Float](./mtlfxtemporalscalerbase/jitteroffsety.md)
  The vertical component of the subpixel sampling coordinate you use to generate the color texture input.
- [var exposureTexture: (any MTLTexture)?](./mtlfxtemporalscalerbase/exposuretexture.md)
  A texture that sets the exposure level for the color texture input.
- [var preExposure: Float](./mtlfxtemporalscalerbase/preexposure.md)
  The exposure value that you’ve already applied to your color texture input.
### Configuring the depth input
- [var depthTextureUsage: MTLTextureUsage](./mtlfxtemporalscalerbase/depthtextureusage.md)
  The minimal texture usage options that your app’s input depth texture must set to apply the temporal scaler.
- [var depthTexture: (any MTLTexture)?](./mtlfxtemporalscalerbase/depthtexture.md)
  An input depth texture you set for the temporal scaler that supports the correct depth texture usage options.
- [var isDepthReversed: Bool](./mtlfxtemporalscalerbase/isdepthreversed.md)
  A Boolean value that indicates whether the depth texture uses zero to represent the farthest distance.
### Configuring the motion input
- [var motionTextureUsage: MTLTextureUsage](./mtlfxtemporalscalerbase/motiontextureusage.md)
  The minimal texture usage options that your app’s input motion texture must set to apply the temporal scaler.
- [var motionTexture: (any MTLTexture)?](./mtlfxtemporalscalerbase/motiontexture.md)
  An input motion texture you set for the temporal scaler that supports the correct motion texture usage options.
- [var motionVectorScaleX: Float](./mtlfxtemporalscalerbase/motionvectorscalex.md)
  The horizontal scale factor the temporal scaler applies to the input motion texture.
- [var motionVectorScaleY: Float](./mtlfxtemporalscalerbase/motionvectorscaley.md)
  The vertical scale factor the temporal scaler applies to the input motion texture.
### Configuring the reactive mask input
- [var reactiveTextureUsage: MTLTextureUsage](./mtlfxtemporalscalerbase/reactivetextureusage.md)
  The minimal texture-usage options that your app’s reactive-mask texture input needs to have for the temporal scaler.
- [var reactiveMaskTexture: (any MTLTexture)?](./mtlfxtemporalscalerbase/reactivemasktexture.md)
  A reactive-mask texture input you set for a temporal scaler that supports the correct usage options.
### Configuring the image output
- [var outputTextureUsage: MTLTextureUsage](./mtlfxtemporalscalerbase/outputtextureusage.md)
  The minimal texture usage options that your app’s output texture must set to apply the temporal scaler.
- [var outputTexture: (any MTLTexture)?](./mtlfxtemporalscalerbase/outputtexture.md)
  An output texture that supports the correct depth texture usage options.
### Synchronizing untracked resources
- [var fence: (any MTLFence)?](./mtlfxtemporalscalerbase/fence.md)
  An optional fence instance that you provide to synchronize your app’s untracked resources.
### Encoding a temporal scaling effect
- [var reset: Bool](./mtlfxtemporalscalerbase/reset.md)
  A Boolean that indicates whether the temporal scaler discards historical data from previous frames.
- [func encode(commandBuffer: any MTLCommandBuffer)](./mtlfxtemporalscaler/encode%28commandbuffer%29.md)
  Adds the temporal scaling command to a render pass’s command buffer.
### Inspecting the fixed settings
- [var inputWidth: Int](./mtlfxtemporalscalerbase/inputwidth.md)
  The width, in pixels, of the input color texture for the temporal scaler.
- [var inputHeight: Int](./mtlfxtemporalscalerbase/inputheight.md)
  The height, in pixels, of the input color texture for the temporal scaler.
- [var inputContentMinScale: Float](./mtlfxtemporalscalerbase/inputcontentminscale.md)
  The smallest scale factor the temporal scaler uses to generate output textures.
- [var inputContentMaxScale: Float](./mtlfxtemporalscalerbase/inputcontentmaxscale.md)
  The largest scale factor the temporal scaler uses to generate output textures.
- [var colorTextureFormat: MTLPixelFormat](./mtlfxtemporalscalerbase/colortextureformat.md)
  The pixel format of the input color texture for the temporal scaler.
- [var depthTextureFormat: MTLPixelFormat](./mtlfxtemporalscalerbase/depthtextureformat.md)
  The pixel format of the input depth texture for the temporal scaler.
- [var motionTextureFormat: MTLPixelFormat](./mtlfxtemporalscalerbase/motiontextureformat.md)
  The pixel format of the input motion texture for the temporal scaler.
- [var outputWidth: Int](./mtlfxtemporalscalerbase/outputwidth.md)
  The width, in pixels, of the output color texture for the temporal scaler.
- [var outputHeight: Int](./mtlfxtemporalscalerbase/outputheight.md)
  The height, in pixels, of the output color texture for the temporal scaler.
- [var outputTextureFormat: MTLPixelFormat](./mtlfxtemporalscalerbase/outputtextureformat.md)
  The pixel format of the output color texture for the temporal scaler.

## Relationships

### Inherits From
- [MTLFXFrameInterpolatableScaler](./mtlfxframeinterpolatablescaler.md)
- [MTLFXTemporalScalerBase](./mtlfxtemporalscalerbase.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Temporal scaling
- [Applying temporal antialiasing and upscaling using MetalFX](./applying-temporal-antialiasing-and-upscaling-using-metalfx.md)
  Reduce render workloads while increasing image detail with MetalFX.
- [class MTLFXTemporalScalerDescriptor](./mtlfxtemporalscalerdescriptor.md)
  A set of properties that configure a temporal scaling effect, and a factory method that creates the effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxtemporalscaler)*