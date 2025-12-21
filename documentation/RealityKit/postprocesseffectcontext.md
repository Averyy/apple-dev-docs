# PostProcessEffectContext

**Framework**: RealityKit  
**Kind**: struct

An object RealityKit passes data to a post process effect method.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
struct PostProcessEffectContext<CommandBuffer>
```

#### Overview

You can register a method that applies postprocessing effects to a scene RealityKit renders with a [`RealityView`](realityview.md). Once every frame, RealityKit calls that function before displaying the scene. You can use this to apply postprocess effects using any APIs that can modify an image texture. However, because RealityKit calls this method every frame, prioritize using APIs that execute on the GPU, such as Metal compute functions, [`Metal Performance Shaders`](https://developer.apple.com/documentation/MetalPerformanceShaders), or [`Core Image`](https://developer.apple.com/documentation/CoreImage). You can also render additional content on top of the frame buffer, such as a SpriteKit scene.

> **Note**: For more information on implementing postprocess effects, see [`Implementing special rendering effects with RealityKit postprocessing`](implementing-special-rendering-effects-with-realitykit-postprocessing.md), which demonstrates multiple postprocess techniques.

A postprocess method takes a single `PostProcessEffectContext` parameter, which contains data the callback method needs to modify the rendered scene, including the frame buffer, depth map, and a property for writing the image you modify. The postprocess method in your [`PostProcessEffect`](postprocesseffect.md) type needs to encode to the output texture, or the frame is never displayed.

A postprocess method looks like this:

```swift
func postProcess(context: borrowing PostProcessEffectContext<MTLCommandBuffer>) {
    // Handle postprocessing here.
}
```

To register a method as the postprocess render callback, add an implementation for [`postProcess(context:)`](postprocesseffect/postprocess(context:).md) in your type that conforms to [`PostProcessEffect`](postprocesseffect.md):

```swift
class LaplacianPostProcess: PostProcessEffect {
    // Post process callback.
    func postProcess(context: borrowing PostProcessEffectContext<MTLCommandBuffer>) {
        let filter = MPSImageLaplacian()
        filter.encode(commandBuffer: context.commandBuffer,
                    sourceTexture: context.sourceColorTexture,
                    destinationTexture: context.compatibleTargetTexture)
    }
}
```

To stop postprocessing, you can set the [`customPostProcessing`](realityviewrenderingeffects/custompostprocessing.md) property to [`none`](realityviewpostprocesseffect/none.md).

```swift
content.renderingEffects.customPostProcessing = .none
```

If your app turns postprocessing on and off frequently, another option for disabling postprocess effects is to keep your callbacks registered, but use an [`MTLBlitCommandEncoder`](https://developer.apple.com/documentation/Metal/MTLBlitCommandEncoder) to encode the unmodified frame buffer directly to the output texture whenever postprocess effects aren’t active.

```swift
var isEnabled: Binding<Bool>

func postProcess(context: borrowing PostProcessEffectContext<MTLCommandBuffer>) {
    if isEnabled.wrappedValue {
        let filter = MPSImageLaplacian()
        filter.encode(commandBuffer: context.commandBuffer,
                    sourceTexture: context.sourceColorTexture,
                    destinationTexture: context.compatibleTargetTexture)
    } else {
        // Remove processing effects.
        let blitEncoder = context.commandBuffer.makeBlitCommandEncoder()
        blitEncoder?.copy(from: context.sourceColorTexture, to: context.targetColorTexture)
        blitEncoder?.endEncoding()
    }
}
```

## Topics

### Instance Properties
- [var commandBuffer: CommandBuffer](postprocesseffectcontext/commandbuffer.md)
  The Metal command buffer for encoding the frame.
- [var device: any MTLDevice](postprocesseffectcontext/device.md)
  The Metal device where the scene renders.
- [var projection: float4x4](postprocesseffectcontext/projection.md)
  The projection matrix that renders the frame.
- [var sourceColorTexture: any MTLTexture](postprocesseffectcontext/sourcecolortexture.md)
  The rendered frame buffer.
- [var sourceDepthTexture: any MTLTexture](postprocesseffectcontext/sourcedepthtexture.md)
  The frame’s depth buffer.
- [var targetColorTexture: any MTLTexture](postprocesseffectcontext/targetcolortexture.md)
  The output texture where the postprocess callback writes the modified frame buffer.
- [var time: TimeInterval](postprocesseffectcontext/time.md)
  The scene’s elapsed time.

## See Also

- [struct RealityViewEnvironment](realityviewenvironment.md)
  A struct that determines the background and default lighting properties for a reality view.
- [struct RealityViewRenderingEffects](realityviewrenderingeffects.md)
  A struct for enabling and disabling rendering effects for RealityKit content.
- [struct RealityViewRenderingEffectMode](realityviewrenderingeffectmode.md)
  A mode that determines whether a rendering effect is enabled or disabled.
- [struct RealityViewDynamicRange](realityviewdynamicrange.md)
  Options that determine the state of high dynamic range rendering for virtual content.
- [enum AntialiasingMode](antialiasingmode.md)
  The rendering technique used to smooth edges of virtual content.
- [struct RealityViewPostProcessEffect](realityviewpostprocesseffect.md)
  A struct for enabling or disabling post processing effects for all content a reality view contains.
- [ARView.Environment](arview/environment-swift.struct.md)
  A description of background, lighting, and acoustic properties for a view’s content.
- [ARView.RenderOptions](arview/renderoptions-swift.struct.md)
  The available rendering options that you use to selectively disable certain rendering effects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/postprocesseffectcontext)*