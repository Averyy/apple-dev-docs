# MTLFXTemporalScalerBase

**Framework**: MetalFX  
**Kind**: protocol

An upscaling effect that generates a higher resolution texture in a render pass by analyzing multiple input textures over time.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
protocol MTLFXTemporalScalerBase : NSObjectProtocol
```

#### Overview

The MetalFX temporal scaler increases the size of your input texture to a larger output texture. You can use the scaler to upscale every frame of your app’s scene or rendering in real time. With a scaler, you can draw more complicated scenes in less time by intentionally rendering to a lower resolution to save time before upscaling.

Create an [`MTLFXTemporalScaler`](mtlfxtemporalscaler.md) instance by following these steps:

1. Create and configure an [`MTLFXTemporalScalerDescriptor`](mtlfxtemporalscalerdescriptor.md) instance.
2. Call the descriptor’s `newTemporalScalerWithDevice:` method.

Upscale a rendering by following these steps for every render pass:

1. Set the temporal scaler’s [`colorTexture`](mtlfxtemporalscalerbase/colortexture.md) property to the input texture.
2. Set the scaler’s [`inputContentWidth`](mtlfxtemporalscalerbase/inputcontentwidth.md) and [`inputContentHeight`](mtlfxtemporalscalerbase/inputcontentheight.md) properties.
3. Set the scaler’s [`outputTexture`](mtlfxtemporalscalerbase/outputtexture.md) property to your destination texture.
4. Encode the upscale commands to a command buffer by calling the temporal scaler’s [`encode(commandBuffer:)`](mtlfxtemporalscaler/encode(commandbuffer:).md) method.

#### Conforming to Texture Usage Requirements

Temporal scalers expose properties, such as [`colorTextureUsage`](mtlfxtemporalscalerbase/colortextureusage.md), that indicate requirements for your textures to be compatible with it. These properties indicate the minimum set of `MTLTextureUsage` bits that you are responsible for setting in your texture descriptors for this spatial scaler to use them.

Your game or app can set extra usage bits on your textures without losing compatibility, as long at its maintains the minimum set the scaler requests.

#### Assigning Input and Output Textures

When you use an instance of a class that conforms to this protocol, you typically set its input and output textures, as well as other properties, and then encode its work to a command buffer.

MetalFX doesn’t track that you assign the same texture instances to each property across different batches of work, the only requirement is that you provide textures that match the pixel formats and dimensions you specify in the [`MTLFXTemporalScalerDescriptor`](mtlfxtemporalscalerdescriptor.md) descriptor instance that creates the scaler instance.

## Topics

### Instance Properties
- [var colorTexture: (any MTLTexture)?](mtlfxtemporalscalerbase/colortexture.md)
  An input color texture you set for the scaler that supports the correct color texture usage options.
- [var colorTextureFormat: MTLPixelFormat](mtlfxtemporalscalerbase/colortextureformat.md)
  The pixel format of the input color texture for this this scaler.
- [var colorTextureUsage: MTLTextureUsage](mtlfxtemporalscalerbase/colortextureusage.md)
  The minimal texture usage options that your app’s input color texture needs in order to support this scaler.
- [var depthTexture: (any MTLTexture)?](mtlfxtemporalscalerbase/depthtexture.md)
  An input depth texture you set for the scaler that supports the correct color texture usage options.
- [var depthTextureFormat: MTLPixelFormat](mtlfxtemporalscalerbase/depthtextureformat.md)
  The pixel format of the input depth texture for this this scaler.
- [var depthTextureUsage: MTLTextureUsage](mtlfxtemporalscalerbase/depthtextureusage.md)
  The minimal texture usage options that your app’s input depth texture needs in order to support this scaler.
- [var exposureTexture: (any MTLTexture)?](mtlfxtemporalscalerbase/exposuretexture.md)
  The exposure texture this scaler uses.
- [var fence: (any MTLFence)?](mtlfxtemporalscalerbase/fence.md)
  An optional fence that you provide to synchronize your app’s untracked resources.
- [var inputContentHeight: Int](mtlfxtemporalscalerbase/inputcontentheight.md)
  The height, in pixels, of the region within the color texture the scaler uses as its input.
- [var inputContentMaxScale: Float](mtlfxtemporalscalerbase/inputcontentmaxscale.md)
  The largest scale factor the temporal scaler can use to generate output textures.
- [var inputContentMinScale: Float](mtlfxtemporalscalerbase/inputcontentminscale.md)
  The smallest scale factor the temporal scaler can use to generate output textures.
- [var inputContentWidth: Int](mtlfxtemporalscalerbase/inputcontentwidth.md)
  The width, in pixels, of the region within the color texture the scaler uses as its input.
- [var inputHeight: Int](mtlfxtemporalscalerbase/inputheight.md)
  The height, in pixels, of the input color texture for this scaler.
- [var inputWidth: Int](mtlfxtemporalscalerbase/inputwidth.md)
  The width, in pixels, of the input color texture for this scaler.
- [var isDepthReversed: Bool](mtlfxtemporalscalerbase/isdepthreversed.md)
  A Boolean value that indicates whether the depth texture uses zero to represent the farthest distance.
- [var jitterOffsetX: Float](mtlfxtemporalscalerbase/jitteroffsetx.md)
  The horizontal component of the subpixel sampling coordinate you use to generate the color texture input.
- [var jitterOffsetY: Float](mtlfxtemporalscalerbase/jitteroffsety.md)
  The vertical component of the subpixel sampling coordinate you use to generate the color texture input.
- [var motionTexture: (any MTLTexture)?](mtlfxtemporalscalerbase/motiontexture.md)
  An input motion texture you set for the scaler that supports the correct color texture usage options.
- [var motionTextureFormat: MTLPixelFormat](mtlfxtemporalscalerbase/motiontextureformat.md)
  The pixel format of the input motion texture for this this scaler.
- [var motionTextureUsage: MTLTextureUsage](mtlfxtemporalscalerbase/motiontextureusage.md)
  The minimal texture usage options that your app’s motion texture needs in order to support this scaler.
- [var motionVectorScaleX: Float](mtlfxtemporalscalerbase/motionvectorscalex.md)
  The horizontal scale factor the scaler applies to the input motion texture.
- [var motionVectorScaleY: Float](mtlfxtemporalscalerbase/motionvectorscaley.md)
  The vertical scale factor the scaler applies to the input motion texture.
- [var outputHeight: Int](mtlfxtemporalscalerbase/outputheight.md)
  The height, in pixels, of the output color texture for this scaler.
- [var outputTexture: (any MTLTexture)?](mtlfxtemporalscalerbase/outputtexture.md)
  The output texture into which this scaler writes its output.
- [var outputTextureFormat: MTLPixelFormat](mtlfxtemporalscalerbase/outputtextureformat.md)
  The pixel format of the output color texture for this this scaler.
- [var outputTextureUsage: MTLTextureUsage](mtlfxtemporalscalerbase/outputtextureusage.md)
  The minimal texture usage options that your output texture needs in order to support this scaler.
- [var outputWidth: Int](mtlfxtemporalscalerbase/outputwidth.md)
  The width, in pixels, of the output color texture for this scaler.
- [var preExposure: Float](mtlfxtemporalscalerbase/preexposure.md)
  A pre-exposure value this scaler evaluates.
- [var reactiveMaskTexture: (any MTLTexture)?](mtlfxtemporalscalerbase/reactivemasktexture.md)
  The reactive-mask texture input this scaler uses.
- [var reactiveMaskTextureFormat: MTLPixelFormat](mtlfxtemporalscalerbase/reactivemasktextureformat.md)
  The pixel format of the input reactive mask texture for this this scaler.
- [var reactiveTextureUsage: MTLTextureUsage](mtlfxtemporalscalerbase/reactivetextureusage.md)
  The minimal texture usage options that your app’s reactive texture needs in order to support this scaler.
- [var reset: Bool](mtlfxtemporalscalerbase/reset.md)
  A Boolean that indicates whether the temporal scaler discards historical data from previous frames.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Inherited By
- [MTL4FXTemporalScaler](mtl4fxtemporalscaler.md)
- [MTLFXTemporalScaler](mtlfxtemporalscaler.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxtemporalscalerbase)*