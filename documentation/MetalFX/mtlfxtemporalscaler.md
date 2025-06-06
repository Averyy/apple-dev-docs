# MTLFXTemporalScaler

**Framework**: MetalFX  
**Kind**: protocol

An upscaling effect that generates a higher resolution texture in a render pass by analyzing multiple input textures over time.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+

## Declaration

```swift
protocol MTLFXTemporalScaler : NSObjectProtocol
```

#### Overview

The MetalFX temporal scaler increases the size of your input texture to a larger output texture. You can use the scaler to upscale every frame of your app’s scene or rendering in real time. With a scaler, you can draw more complicated scenes in less time by intentionally rendering to a lower resolution to save time before upscaling.

Create an [`MTLFXTemporalScaler`](mtlfxtemporalscaler.md) instance by following these steps:

1. Create and configure an [`MTLFXTemporalScalerDescriptor`](mtlfxtemporalscalerdescriptor.md) instance.
2. Call the descriptor’s [`makeTemporalScaler(device:)`](mtlfxtemporalscalerdescriptor/maketemporalscaler(device:).md) method.

Upscale a rendering by following these steps for every render pass:

1. Set the temporal scaler’s [`colorTexture`](mtlfxtemporalscaler/colortexture.md) property to the input texture.
2. Set the scaler’s [`inputContentWidth`](mtlfxtemporalscaler/inputcontentwidth.md) and [`inputContentHeight`](mtlfxtemporalscaler/inputcontentheight.md) properties.
3. Set the scaler’s [`outputTexture`](mtlfxtemporalscaler/outputtexture.md) property to your destination texture.
4. Encode the upscale commands to an [`MTLCommandBuffer`](https://developer.apple.com/documentation/Metal/MTLCommandBuffer) by calling the temporal scaler’s [`encode(commandBuffer:)`](mtlfxtemporalscaler/encode(commandbuffer:).md) method.

## Topics

### Configuring the image input
- [var colorTextureUsage: MTLTextureUsage](mtlfxtemporalscaler/colortextureusage.md)
  The minimal texture usage options that your app’s input color texture must set to apply the temporal scaler.
- [var colorTexture: (any MTLTexture)?](mtlfxtemporalscaler/colortexture.md)
  An input color texture you set for the temporal scaler that supports the correct color texture usage options.
- [var inputContentWidth: Int](mtlfxtemporalscaler/inputcontentwidth.md)
  The width, in pixels, of the region within the color texture the temporal scaler uses as its input.
- [var inputContentHeight: Int](mtlfxtemporalscaler/inputcontentheight.md)
  The height, in pixels, of the region within the color texture the temporal scaler uses as its input.
- [var jitterOffsetX: Float](mtlfxtemporalscaler/jitteroffsetx.md)
  The horizontal component of the subpixel sampling coordinate you use to generate the color texture input.
- [var jitterOffsetY: Float](mtlfxtemporalscaler/jitteroffsety.md)
  The vertical component of the subpixel sampling coordinate you use to generate the color texture input.
- [var exposureTexture: (any MTLTexture)?](mtlfxtemporalscaler/exposuretexture.md)
  A texture that sets the exposure level for the color texture input.
- [var preExposure: Float](mtlfxtemporalscaler/preexposure.md)
  The exposure value that you’ve already applied to your color texture input.
### Configuring the depth input
- [var depthTextureUsage: MTLTextureUsage](mtlfxtemporalscaler/depthtextureusage.md)
  The minimal texture usage options that your app’s input depth texture must set to apply the temporal scaler.
- [var depthTexture: (any MTLTexture)?](mtlfxtemporalscaler/depthtexture.md)
  An input depth texture you set for the temporal scaler that supports the correct depth texture usage options.
- [var isDepthReversed: Bool](mtlfxtemporalscaler/isdepthreversed.md)
  A Boolean value that indicates whether the depth texture uses zero to represent the farthest distance.
### Configuring the motion input
- [var motionTextureUsage: MTLTextureUsage](mtlfxtemporalscaler/motiontextureusage.md)
  The minimal texture usage options that your app’s input motion texture must set to apply the temporal scaler.
- [var motionTexture: (any MTLTexture)?](mtlfxtemporalscaler/motiontexture.md)
  An input motion texture you set for the temporal scaler that supports the correct motion texture usage options.
- [var motionVectorScaleX: Float](mtlfxtemporalscaler/motionvectorscalex.md)
  The horizontal scale factor the temporal scaler applies to the input motion texture.
- [var motionVectorScaleY: Float](mtlfxtemporalscaler/motionvectorscaley.md)
  The vertical scale factor the temporal scaler applies to the input motion texture.
### Configuring the reactive mask input
- [var reactiveTextureUsage: MTLTextureUsage](mtlfxtemporalscaler/reactivetextureusage.md)
  The minimal texture-usage options that your app’s reactive-mask texture input needs to have for the temporal scaler.
- [var reactiveMaskTexture: (any MTLTexture)?](mtlfxtemporalscaler/reactivemasktexture.md)
  A reactive-mask texture input you set for a temporal scaler that supports the correct usage options.
### Configuring the image output
- [var outputTextureUsage: MTLTextureUsage](mtlfxtemporalscaler/outputtextureusage.md)
  The minimal texture usage options that your app’s output texture must set to apply the temporal scaler.
- [var outputTexture: (any MTLTexture)?](mtlfxtemporalscaler/outputtexture.md)
  An output texture that supports the correct depth texture usage options.
### Synchronizing untracked resources
- [var fence: (any MTLFence)?](mtlfxtemporalscaler/fence.md)
  An optional fence instance that you provide to synchronize your app’s untracked resources.
### Encoding a temporal scaling effect
- [var reset: Bool](mtlfxtemporalscaler/reset.md)
  A Boolean that indicates whether the temporal scaler discards historical data from previous frames.
- [func encode(commandBuffer: any MTLCommandBuffer)](mtlfxtemporalscaler/encode(commandbuffer:).md)
  Adds the temporal scaling command to a render pass’s command buffer.
### Inspecting the fixed settings
- [var inputWidth: Int](mtlfxtemporalscaler/inputwidth.md)
  The width, in pixels, of the input color texture for the temporal scaler.
- [var inputHeight: Int](mtlfxtemporalscaler/inputheight.md)
  The height, in pixels, of the input color texture for the temporal scaler.
- [var inputContentMinScale: Float](mtlfxtemporalscaler/inputcontentminscale.md)
  The smallest scale factor the temporal scaler uses to generate output textures.
- [var inputContentMaxScale: Float](mtlfxtemporalscaler/inputcontentmaxscale.md)
  The largest scale factor the temporal scaler uses to generate output textures.
- [var colorTextureFormat: MTLPixelFormat](mtlfxtemporalscaler/colortextureformat.md)
  The pixel format of the input color texture for the temporal scaler.
- [var depthTextureFormat: MTLPixelFormat](mtlfxtemporalscaler/depthtextureformat.md)
  The pixel format of the input depth texture for the temporal scaler.
- [var motionTextureFormat: MTLPixelFormat](mtlfxtemporalscaler/motiontextureformat.md)
  The pixel format of the input motion texture for the temporal scaler.
- [var outputWidth: Int](mtlfxtemporalscaler/outputwidth.md)
  The width, in pixels, of the output color texture for the temporal scaler.
- [var outputHeight: Int](mtlfxtemporalscaler/outputheight.md)
  The height, in pixels, of the output color texture for the temporal scaler.
- [var outputTextureFormat: MTLPixelFormat](mtlfxtemporalscaler/outputtextureformat.md)
  The pixel format of the output color texture for the temporal scaler.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Applying temporal antialiasing and upscaling using MetalFX](applying-temporal-antialiasing-and-upscaling-using-metalfx.md)
  Reduce render workloads while increasing image detail with MetalFX.
- [class MTLFXTemporalScalerDescriptor](mtlfxtemporalscalerdescriptor.md)
  A set of properties that configure a temporal scaling effect, and a factory method that creates the effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxtemporalscaler)*