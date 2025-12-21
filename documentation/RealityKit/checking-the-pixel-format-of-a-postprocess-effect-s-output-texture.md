# Checking the pixel format of a postprocess effect’s output texture

**Framework**: RealityKit

Make sure your postprocess effect works on all devices.

#### Overview

Some device GPUs require that the output texture for postprocess effects be in a specific format. If the current device doesn’t support [`MTLGPUFamily.apple2`](https://developer.apple.com/documentation/Metal/MTLGPUFamily/apple2), convert the output texture to [`MTLPixelFormat.bgra8Unorm`](https://developer.apple.com/documentation/Metal/MTLPixelFormat/bgra8Unorm) before encoding the processed framebuffer to it. An easy way to do that, is to add a derived property to [`ARView.PostProcessContext`](arview/postprocesscontext.md) using an extension:

```swift
extension RealityKit.ARView.PostProcessContext {
    // Returns the output texture, ensuring that the pixel format is 
    // appropriate for the current device's GPU.
    var compatibleTargetTexture: MTLTexture! {
        if self.device.supportsFamily(.apple2) {
            return targetColorTexture
        } else {
            return targetColorTexture.makeTextureView(pixelFormat: .bgra8Unorm)!
        }
    }
}
```

If you use this derived property instead of [`targetColorTexture`](arview/postprocesscontext/targetcolortexture.md) when encoding the results of a postprocess effect, it ensures the effect works on all devices.

## See Also

- [Using Metal performance shaders to create custom postprocess effects](using-metal-performance-shaders-to-create-custom-postprocess-effects.md)
  Leverage the Metal Performance Shaders framework to create special rendering effects for your RealityKit scenes.
- [Implementing special rendering effects with RealityKit postprocessing](implementing-special-rendering-effects-with-realitykit-postprocessing.md)
  Implement a variety of postprocessing techniques to alter RealityKit rendering.
- [Passing Structured Data to a Metal Compute Function](passing-structured-data-to-a-metal-compute-function.md)
  Send nontexture data from Swift to your Metal shaders using a shared header file.
- [Implementing postprocess effects using Metal compute functions](implementing-postprocess-effects-using-metal-compute-functions.md)
  Create custom shaders to implement postprocess effects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/checking-the-pixel-format-of-a-postprocess-effect-s-output-texture)*