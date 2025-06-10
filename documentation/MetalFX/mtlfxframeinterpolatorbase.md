# MTLFXFrameInterpolatorBase

**Framework**: MetalFX  
**Kind**: protocol

A common abstraction to all frame interpolators.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
protocol MTLFXFrameInterpolatorBase : NSObjectProtocol
```

#### Overview

This protocol defines properties common to all frame interpolators. You access these properties through any frame interpolator instance you create by calling construction methods such as [`newFrameInterpolator(with:)`](mtlfxframeinterpolatordescriptor/newframeinterpolator(with:).md).

#### Conforming to Texture Usage Requirements

Frame interpolator instances expose properties, such as [`colorTextureUsage`](mtlfxframeinterpolatorbase/colortextureusage.md), that indicate requirements for your textures to be compatible with it. These properties indicate the minimum set of `MTLTextureUsage` bits that you are responsible for setting in your texture descriptors for this frame interpolator to use them.

Your game or app can set extra usage bits on your textures without losing compatibility, as long at its maintains the minimum set the interpolator requests.

#### Assigning Input and Output Textures

When you use an instance of a class that conforms to this protocol, you typically set its input and output textures, as well as other properties, and then encode its work to a command buffer.

MetalFX doesn’t track that you assign the same texture instances to each property across different batches of work, the only requirement is that you provide textures that match the pixel formats and dimensions you specify in the [`MTLFXFrameInterpolatorDescriptor`](mtlfxframeinterpolatordescriptor.md) descriptor instance that creates the scaler instance.

#### Encoding Work

Once you configure all properties for the current frame of your game or app, you indicate to the scaler instance into which command buffer it encodes its work. You achieve this by calling, for example, [`encode(to:)`](mtlfxframeinterpolator/encode(to:).md).

## Topics

### Instance Properties
- [var aspectRatio: Float](mtlfxframeinterpolatorbase/aspectratio.md)
  The ratio between width and height of the screen.
- [var colorTexture: (any MTLTexture)?](mtlfxframeinterpolatorbase/colortexture.md)
  The color texture that this frame interpolator evaluates.
- [var colorTextureFormat: MTLPixelFormat](mtlfxframeinterpolatorbase/colortextureformat.md)
  The pixel format of the input color texture for this frame interpolator.
- [var colorTextureUsage: MTLTextureUsage](mtlfxframeinterpolatorbase/colortextureusage.md)
  The minimal texture usage options that your app’s input color texture needs in order to support this frame interpolator.
- [var deltaTime: Float](mtlfxframeinterpolatorbase/deltatime.md)
  The length of the time interval, in seconds, between time of current and previous frame.
- [var depthTexture: (any MTLTexture)?](mtlfxframeinterpolatorbase/depthtexture.md)
  The depth texture this frame interpolator evaluates.
- [var depthTextureFormat: MTLPixelFormat](mtlfxframeinterpolatorbase/depthtextureformat.md)
  The pixel format of the input depth texture for this frame interpolator.
- [var depthTextureUsage: MTLTextureUsage](mtlfxframeinterpolatorbase/depthtextureusage.md)
  The minimal texture usage options that your app’s input depth texture needs in order to support this frame interpolator.
- [var farPlane: Float](mtlfxframeinterpolatorbase/farplane.md)
  The far plane distance that corresponds to the frustrum that renders the scene into the color buffer.
- [var fence: (any MTLFence)?](mtlfxframeinterpolatorbase/fence.md)
  An optional fence that this frame interpolator waits for and updates.
- [var fieldOfView: Float](mtlfxframeinterpolatorbase/fieldofview.md)
  The vertical field of view angle, in degrees, of the camera that renders the scene into the color buffer.
- [var inputHeight: Int](mtlfxframeinterpolatorbase/inputheight.md)
  The height, in pixels, of the input color texture for the frame interpolator.
- [var inputWidth: Int](mtlfxframeinterpolatorbase/inputwidth.md)
  The width, in pixels, of the input color texture for the frame interpolator.
- [var isDepthReversed: Bool](mtlfxframeinterpolatorbase/isdepthreversed.md)
  A Boolean value that indicates whether the depth texture uses zero to represent the farthest distance.
- [var isUITextureComposited: Bool](mtlfxframeinterpolatorbase/isuitexturecomposited.md)
  A Boolean value that controls whether this frame interpolator interprets the color texture to include your game’s custom UI.
- [var jitterOffsetX: Float](mtlfxframeinterpolatorbase/jitteroffsetx.md)
  The horizontal component of the subpixel sampling coordinate you use to generate the color texture input.
- [var jitterOffsetY: Float](mtlfxframeinterpolatorbase/jitteroffsety.md)
  The vertical component of the subpixel sampling coordinate you use to generate the color texture input.
- [var motionTexture: (any MTLTexture)?](mtlfxframeinterpolatorbase/motiontexture.md)
  The motion texture this frame interpolator evaluates.
- [var motionTextureFormat: MTLPixelFormat](mtlfxframeinterpolatorbase/motiontextureformat.md)
  The pixel format of the input motion texture for this frame interpolator.
- [var motionTextureUsage: MTLTextureUsage](mtlfxframeinterpolatorbase/motiontextureusage.md)
  The minimal texture usage options that your app’s input motion texture needs in order to support this frame interpolator.
- [var motionVectorScaleX: Float](mtlfxframeinterpolatorbase/motionvectorscalex.md)
  The horizontal scale factor the frame interpolator applies to the input motion texture.
- [var motionVectorScaleY: Float](mtlfxframeinterpolatorbase/motionvectorscaley.md)
  The vertical scale factor the frame interpolator applies to the input motion texture.
- [var nearPlane: Float](mtlfxframeinterpolatorbase/nearplane.md)
  The near plane distance that corresponds to the frustrum that renders the scene into the color buffer.
- [var outputHeight: Int](mtlfxframeinterpolatorbase/outputheight.md)
  The height, in pixels, of the output color texture for the frame interpolator.
- [var outputTexture: (any MTLTexture)?](mtlfxframeinterpolatorbase/outputtexture.md)
  The output texture into which this frame interpolator writes its output.
- [var outputTextureFormat: MTLPixelFormat](mtlfxframeinterpolatorbase/outputtextureformat.md)
  The pixel format of the output color texture for this frame interpolator.
- [var outputTextureUsage: MTLTextureUsage](mtlfxframeinterpolatorbase/outputtextureusage.md)
  The minimal texture usage options that your app’s output color texture needs in order to support this frame interpolator.
- [var outputWidth: Int](mtlfxframeinterpolatorbase/outputwidth.md)
  The width, in pixels, of the output color texture for the frame interpolator.
- [var prevColorTexture: (any MTLTexture)?](mtlfxframeinterpolatorbase/prevcolortexture.md)
  The previous color texture for this frame interpolator during the last call to encode work into a command buffer.
- [var shouldResetHistory: Bool](mtlfxframeinterpolatorbase/shouldresethistory.md)
  A Boolean property indicating whether to reset history.
- [var uiTexture: (any MTLTexture)?](mtlfxframeinterpolatorbase/uitexture.md)
  An optional texture containing your game’s custom UI that this frame interpolator evaluates.
- [var uiTextureFormat: MTLPixelFormat](mtlfxframeinterpolatorbase/uitextureformat.md)
  The pixel format of the input UI texture for the frame interpolator.
- [var uiTextureUsage: MTLTextureUsage](mtlfxframeinterpolatorbase/uitextureusage.md)
  The minimal texture usage options that your app’s input UI texture needs in order to support this frame interpolator.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Inherited By
- [MTL4FXFrameInterpolator](mtl4fxframeinterpolator.md)
- [MTLFXFrameInterpolator](mtlfxframeinterpolator.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxframeinterpolatorbase)*