# Using Metal performance shaders to create custom postprocess effects

**Framework**: Realitykit

Leverage the Metal Performance Shaders framework to create special rendering effects for your RealityKit scenes.

#### Overview

In iOS 15 and later, and macOS 12 and later, you can apply postprocess effects to a RealityKit scene after RealityKit renders it, but before RealityKit displays it. If you register a postprocess callback function, RealityKit passes that function the complete, rendered frame so you can modify it before the viewer sees it. You can use any image processing or drawing APIs on the rendered frame but, as a practical matter, only APIs that execute on the GPU are fast enough to use every frame and maintain a good framerate.

One way to implement postprocess effects is to apply filters from the [`Metal Performance Shaders`](https://developer.apple.com/documentation/metalperformanceshaders) framework to the rendered scene. You can use apply these filters to an image without writing any custom shader code. Because these filters run on the GPU and operate directly on Metal textures, they’re a good choice for postprocessing effects.

If the Metal Performance Shaders framework doesn’t provide an image filter that meets your needs, you can also use Core Image to postprocess frames. Core Image provides a greater selection of image filters, which also run on the GPU, but Core Image requires you to convert the rendered frame into a [`CIImage`](https://developer.apple.com/documentation/coreimage/ciimage). For more information, see [`Applying core image filters as a postprocess effect`](applying-core-image-filters-as-a-postprocess-effect.md).

If neither the Metal Performance Shaders framework nor Core Image provide the effect you need, you can also write custom compute functions to implement postprocess effects. For more information, see [`Implementing postprocess effects using Metal compute functions`](implementing-postprocess-effects-using-metal-compute-functions.md).

##### Check the Output Texture Pixel Format

Some device GPUs require that the output texture be in a specific pixel format. If the device your code is running on doesn’t support [`MTLGPUFamily.apple2`](https://developer.apple.com/documentation/Metal/MTLGPUFamily/apple2), convert the output texture to [`MTLPixelFormat.bgra8Unorm`](https://developer.apple.com/documentation/Metal/MTLPixelFormat/bgra8Unorm) before using it. For more information, see [`Checking the pixel format of a postprocess effect’s output texture`](checking-the-pixel-format-of-a-postprocess-effect-s-output-texture.md).

##### Create a Callback Function

To create postprocess effects using image filters from the Metal Performance Shaders framework, create a Swift function that takes a single [`ARView.PostProcessContext`](arview/postprocesscontext.md) parameter. In that method, create and configure an instance of the filter that you want to apply using the [`device`](arview/postprocesscontext/device.md) property from the context. Once you’ve created an instance of the shader, call its encode method, passing the command buffer, source color texture, and output texture from the context.

```swift
    func postEffectMPSGaussianBlur(context: ARView.PostProcessContext) {
        let gaussianBlur = MPSImageGaussianBlur(device: context.device, sigma: 4)
        gaussianBlur.encode(commandBuffer: context.commandBuffer,
                            sourceTexture: context.sourceColorTexture,
                            destinationTexture: context.compatibleTargetTexture)
```

> **Note**: The `compatibleTargetTexture` property referenced above is a derived property based on [`targetColorTexture`](arview/postprocesscontext/targetcolortexture.md). It ensures that the output texture uses the appropriate pixel format for the current device. For more information, see [`Checking the pixel format of a postprocess effect’s output texture`](checking-the-pixel-format-of-a-postprocess-effect-s-output-texture.md).

##### Register the Callback Function

To apply the effect, register the function as the [`postProcess`](arview/rendercallbacks-swift.struct/postprocess.md) render callback for the [`ARView`](arview.md).

```swift
arView.renderCallbacks.postProcess = postEffectMPSGaussianBlur
```

> **Note**: For more information on using Metal Performance Shader framework image filters to create postprocess effects, see the [`Implementing Special Rendering Effects with RealityKit Postprocessing`](implementing_special_rendering_effects_with_realitykit_postprocessing.md) sample code project.

## See Also

- [Implementing Special Rendering Effects with RealityKit Postprocessing](implementing_special_rendering_effects_with_realitykit_postprocessing.md)
  Implement a variety of postprocessing techniques to alter RealityKit rendering.
- [Checking the pixel format of a postprocess effect’s output texture](checking-the-pixel-format-of-a-postprocess-effect-s-output-texture.md)
  Make sure your postprocess effect works on all devices.
- [Passing Structured Data to a Metal Compute Function](passing-structured-data-to-a-metal-compute-function.md)
  Send nontexture data from Swift to your Metal shaders using a shared header file.
- [Implementing postprocess effects using Metal compute functions](implementing-postprocess-effects-using-metal-compute-functions.md)
  Create custom shaders to implement postprocess effects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/RealityKit/using-metal-performance-shaders-to-create-custom-postprocess-effects)*