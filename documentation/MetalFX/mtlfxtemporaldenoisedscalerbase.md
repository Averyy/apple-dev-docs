# MTLFXTemporalDenoisedScalerBase

**Framework**: MetalFX  
**Kind**: protocol

A common abstraction to all denoiser scalers.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
protocol MTLFXTemporalDenoisedScalerBase : NSObjectProtocol
```

#### Overview

This protocol defines properties common to all denoiser scalers. You access these properties through any denoiser scaler instance you create by calling construction methods such as [`newTemporalDenoisedScaler(with:)`](mtlfxtemporaldenoisedscalerdescriptor/newtemporaldenoisedscaler(with:).md).

##### Conforming to Texture Usage Requirements

Denoiser scaler instances expose properties, such as [`colorTextureUsage`](mtlfxtemporaldenoisedscalerbase/colortextureusage.md), that indicate requirements for your textures to be compatible with it. These properties indicate the minimum set of `MTLTextureUsage` bits that you are responsible for setting in your texture descriptors for this denoise scaler to use them.

Your game or app can set extra usage bits on your textures without losing compatibility, as long at its maintains the minimum set the denoiser scaler requests.

##### Assigning Input and Output Textures

When you use an instance of a class that conforms to this protocol, you typically set its input and output textures, as well as other properties, and then encode its work to a command buffer.

MetalFX doesn’t track that you assign the same texture instances to each property across different batches of work, the only requirement is that you provide textures that match the pixel formats and dimensions you specify in the [`MTLFXTemporalDenoisedScalerDescriptor`](mtlfxtemporaldenoisedscalerdescriptor.md) descriptor instance that creates the scaler instance.

##### Encoding Work

Once you configure all properties for the current frame of your game or app, you indicate to the scaler instance into which command buffer it encodes its work. You achieve this by calling, for example, [`encode(to:)`](mtlfxtemporaldenoisedscaler/encode(to:).md).

## Topics

### Instance Properties
- [var colorTexture: (any MTLTexture)?](mtlfxtemporaldenoisedscalerbase/colortexture.md)
  Assigns the color texture this scaler evaluates.
- [var colorTextureFormat: MTLPixelFormat](mtlfxtemporaldenoisedscalerbase/colortextureformat.md)
  The pixel format of the input color texture for this denoiser scaler.
- [var colorTextureUsage: MTLTextureUsage](mtlfxtemporaldenoisedscalerbase/colortextureusage.md)
  The minimal texture usage options that your app’s input color texture needs in order to support this denoiser scaler.
- [var denoiseStrengthMaskTexture: (any MTLTexture)?](mtlfxtemporaldenoisedscalerbase/denoisestrengthmasktexture.md)
  The denoise strength mask texture this scaler evaluates.
- [var denoiseStrengthMaskTextureFormat: MTLPixelFormat](mtlfxtemporaldenoisedscalerbase/denoisestrengthmasktextureformat.md)
  The pixel format of the input denoise strength mask texture for this denoiser scaler.
- [var denoiseStrengthMaskTextureUsage: MTLTextureUsage](mtlfxtemporaldenoisedscalerbase/denoisestrengthmasktextureusage.md)
  The minimal texture usage options that your app’s input denoise strength texture needs in order to support this denoiser scaler.
- [var depthTexture: (any MTLTexture)?](mtlfxtemporaldenoisedscalerbase/depthtexture.md)
  The depth texture this scaler evaluates.
- [var depthTextureFormat: MTLPixelFormat](mtlfxtemporaldenoisedscalerbase/depthtextureformat.md)
  The pixel format of the input depth texture for this denoiser scaler.
- [var depthTextureUsage: MTLTextureUsage](mtlfxtemporaldenoisedscalerbase/depthtextureusage.md)
  The minimal texture usage options that your app’s input depth texture needs in order to support this denoiser scaler.
- [var diffuseAlbedoTexture: (any MTLTexture)?](mtlfxtemporaldenoisedscalerbase/diffusealbedotexture.md)
  The diffuse albedo texture this scaler evaluates.
- [var diffuseAlbedoTextureFormat: MTLPixelFormat](mtlfxtemporaldenoisedscalerbase/diffusealbedotextureformat.md)
  The pixel format of the input diffuse albedo texture for this denoiser scaler.
- [var diffuseAlbedoTextureUsage: MTLTextureUsage](mtlfxtemporaldenoisedscalerbase/diffusealbedotextureusage.md)
  The minimal texture usage options that your app’s input diffuse albedo texture needs in order to support this denoiser scaler.
- [var exposureTexture: (any MTLTexture)?](mtlfxtemporaldenoisedscalerbase/exposuretexture.md)
  An exposure texture that this denoiser scaler evaluates.
- [var fence: (any MTLFence)?](mtlfxtemporaldenoisedscalerbase/fence.md)
  An optional fence that this denoiser scaler waits for and updates.
- [var inputContentMaxScale: Float](mtlfxtemporaldenoisedscalerbase/inputcontentmaxscale.md)
  The maximum input content scale this scaler supports.
- [var inputContentMinScale: Float](mtlfxtemporaldenoisedscalerbase/inputcontentminscale.md)
  The minimum input content scale this scaler supports.
- [var inputHeight: Int](mtlfxtemporaldenoisedscalerbase/inputheight.md)
  The height, in pixels, of the input color texture for the scaler.
- [var inputWidth: Int](mtlfxtemporaldenoisedscalerbase/inputwidth.md)
  The width, in pixels, of the input color texture for the scaler.
- [var isDepthReversed: Bool](mtlfxtemporaldenoisedscalerbase/isdepthreversed.md)
  A Boolean value that indicates whether the depth texture uses zero to represent the farthest distance.
- [var jitterOffsetX: Float](mtlfxtemporaldenoisedscalerbase/jitteroffsetx.md)
  The horizontal component of the subpixel sampling coordinate you use to generate the color texture input.
- [var jitterOffsetY: Float](mtlfxtemporaldenoisedscalerbase/jitteroffsety.md)
  The vertical component of the subpixel sampling coordinate you use to generate the color texture input.
- [var motionTexture: (any MTLTexture)?](mtlfxtemporaldenoisedscalerbase/motiontexture.md)
  The motion texture this scaler evaluates.
- [var motionTextureFormat: MTLPixelFormat](mtlfxtemporaldenoisedscalerbase/motiontextureformat.md)
  The pixel format of the input motion texture for this denoiser scaler.
- [var motionTextureUsage: MTLTextureUsage](mtlfxtemporaldenoisedscalerbase/motiontextureusage.md)
  The minimal texture usage options that your app’s input motion texture needs in order to support this denoiser scaler.
- [var motionVectorScaleX: Float](mtlfxtemporaldenoisedscalerbase/motionvectorscalex.md)
  The horizontal scale factor the denoiser scaler applies to the input motion texture.
- [var motionVectorScaleY: Float](mtlfxtemporaldenoisedscalerbase/motionvectorscaley.md)
  The vertical scale factor the denoiser scaler applies to the input motion texture.
- [var normalTexture: (any MTLTexture)?](mtlfxtemporaldenoisedscalerbase/normaltexture.md)
  The normal texture this scaler evaluates.
- [var normalTextureFormat: MTLPixelFormat](mtlfxtemporaldenoisedscalerbase/normaltextureformat.md)
  The pixel format of the input normal texture for this denoiser scaler.
- [var normalTextureUsage: MTLTextureUsage](mtlfxtemporaldenoisedscalerbase/normaltextureusage.md)
  The minimal texture usage options that your app’s input normal texture needs in order to support this denoiser scaler.
- [var outputHeight: Int](mtlfxtemporaldenoisedscalerbase/outputheight.md)
  The height, in pixels, of the output color texture for the scaler.
- [var outputTexture: (any MTLTexture)?](mtlfxtemporaldenoisedscalerbase/outputtexture.md)
  The output texture into which this denoiser scaler writes its output.
- [var outputTextureFormat: MTLPixelFormat](mtlfxtemporaldenoisedscalerbase/outputtextureformat.md)
  The pixel format of the output color texture for this denoiser scaler.
- [var outputTextureUsage: MTLTextureUsage](mtlfxtemporaldenoisedscalerbase/outputtextureusage.md)
  The minimal texture usage options that your app’s output texture needs in order to support this denoiser scaler.
- [var outputWidth: Int](mtlfxtemporaldenoisedscalerbase/outputwidth.md)
  The width, in pixels, of the output color texture for the scaler.
- [var preExposure: Float](mtlfxtemporaldenoisedscalerbase/preexposure.md)
  A pre-exposure value for this scaler to evaluate.
- [var reactiveMaskTexture: (any MTLTexture)?](mtlfxtemporaldenoisedscalerbase/reactivemasktexture.md)
  A reactive-mask texture input for this scaler to evaluate.
- [var reactiveMaskTextureFormat: MTLPixelFormat](mtlfxtemporaldenoisedscalerbase/reactivemasktextureformat.md)
  The pixel format of the input reactive mask texture for this denoiser scaler.
- [var reactiveTextureUsage: MTLTextureUsage](mtlfxtemporaldenoisedscalerbase/reactivetextureusage.md)
  The minimal texture usage options that your app’s input reactive texture needs in order to support this denoiser scaler.
- [var roughnessTexture: (any MTLTexture)?](mtlfxtemporaldenoisedscalerbase/roughnesstexture.md)
  The roughness texture this scaler evaluates.
- [var roughnessTextureFormat: MTLPixelFormat](mtlfxtemporaldenoisedscalerbase/roughnesstextureformat.md)
  The pixel format of the input normal texture for this denoiser scaler.
- [var roughnessTextureUsage: MTLTextureUsage](mtlfxtemporaldenoisedscalerbase/roughnesstextureusage.md)
  The minimal texture usage options that your app’s input roughness texture needs in order to support this denoiser scaler.
- [var shouldResetHistory: Bool](mtlfxtemporaldenoisedscalerbase/shouldresethistory.md)
  A Boolean property indicating whether to reset history.
- [var specularAlbedoTexture: (any MTLTexture)?](mtlfxtemporaldenoisedscalerbase/specularalbedotexture.md)
  The specular albedo texture this scaler evaluates.
- [var specularAlbedoTextureFormat: MTLPixelFormat](mtlfxtemporaldenoisedscalerbase/specularalbedotextureformat.md)
  The pixel format of the input specular albedo for this denoiser scaler.
- [var specularAlbedoTextureUsage: MTLTextureUsage](mtlfxtemporaldenoisedscalerbase/specularalbedotextureusage.md)
  The minimal texture usage options that your app’s input specular albedo texture needs in order to support this denoiser scaler.
- [var specularHitDistanceTexture: (any MTLTexture)?](mtlfxtemporaldenoisedscalerbase/specularhitdistancetexture.md)
  The specular hit texture this scaler evaluates.
- [var specularHitDistanceTextureFormat: MTLPixelFormat](mtlfxtemporaldenoisedscalerbase/specularhitdistancetextureformat.md)
  The pixel format of the input specular hit distance texture for this denoiser scaler.
- [var specularHitDistanceTextureUsage: MTLTextureUsage](mtlfxtemporaldenoisedscalerbase/specularhitdistancetextureusage.md)
  The minimal texture usage options that your app’s input specular hit texture needs in order to support this denoiser scaler.
- [var transparencyOverlayTexture: (any MTLTexture)?](mtlfxtemporaldenoisedscalerbase/transparencyoverlaytexture.md)
  The transparency overlay texture that this scaler evaluates.
- [var transparencyOverlayTextureFormat: MTLPixelFormat](mtlfxtemporaldenoisedscalerbase/transparencyoverlaytextureformat.md)
  The pixel format of the input transparency overlay texture for this denoiser scaler.
- [var transparencyOverlayTextureUsage: MTLTextureUsage](mtlfxtemporaldenoisedscalerbase/transparencyoverlaytextureusage.md)
  The minimal texture usage options that your app’s input transparency overlay texture needs in order to support this denoiser scaler.
- [var viewToClipMatrix: simd_float4x4](mtlfxtemporaldenoisedscalerbase/viewtoclipmatrix.md)
  The view-to-clip coordinates transformation matrix this scaler uses as part of its operation.
- [var worldToViewMatrix: simd_float4x4](mtlfxtemporaldenoisedscalerbase/worldtoviewmatrix.md)
  The world-to-view transformation matrix this scaler uses as part of its operation.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Inherited By
- [MTL4FXTemporalDenoisedScaler](mtl4fxtemporaldenoisedscaler.md)
- [MTLFXTemporalDenoisedScaler](mtlfxtemporaldenoisedscaler.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxtemporaldenoisedscalerbase)*