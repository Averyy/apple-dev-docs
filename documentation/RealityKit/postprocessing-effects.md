# Postprocessing effects

**Framework**: RealityKit

Create special rendering effects for your RealityKit scenes.

#### Overview

In iOS 15 and later, and macOS 12 and later, you can apply postprocess effects to a RealityKit scene after RealityKit renders it, but before RealityKit displays it. If you register a postprocess callback function, RealityKit passes that function the complete, rendered frame so you can modify it before the viewer sees it. You can use any image processing or drawing APIs on the rendered frame but, as a practical matter, only APIs that execute on the GPU are fast enough to use every frame and maintain a good framerate.

[`Core Image`](https://developer.apple.com/documentation/CoreImage), Metal kernal functions, [`Metal Performance Shaders`](https://developer.apple.com/documentation/MetalPerformanceShaders), and [`SpriteKit`](https://developer.apple.com/documentation/SpriteKit) all execute on the GPU and can be effectively used to implement postprocessing effects.

## Topics

### Core Image effects
- [Applying core image filters as a postprocess effect](applying-core-image-filters-as-a-postprocess-effect.md)
  Create special rendering effects for your RealityKit scenes using Core Image.
### Metal effects
- [Using Metal performance shaders to create custom postprocess effects](using-metal-performance-shaders-to-create-custom-postprocess-effects.md)
  Leverage the Metal Performance Shaders framework to create special rendering effects for your RealityKit scenes.
- [Implementing special rendering effects with RealityKit postprocessing](implementing-special-rendering-effects-with-realitykit-postprocessing.md)
  Implement a variety of postprocessing techniques to alter RealityKit rendering.
- [Checking the pixel format of a postprocess effect’s output texture](checking-the-pixel-format-of-a-postprocess-effect-s-output-texture.md)
  Make sure your postprocess effect works on all devices.
- [Passing Structured Data to a Metal Compute Function](passing-structured-data-to-a-metal-compute-function.md)
  Send nontexture data from Swift to your Metal shaders using a shared header file.
- [Implementing postprocess effects using Metal compute functions](implementing-postprocess-effects-using-metal-compute-functions.md)
  Create custom shaders to implement postprocess effects.
### Bloom and tone mapping
- [struct BloomComponent](bloomcomponent.md)
  The `BloomComponent` adds a luminous glow effect around bright objects in the scene by extracting and blurring the brightest parts of the image, then combining them back with the original rendering. If scope is set to `unbounded` Bloom will be computed on the entire screen. If scope is set to `hierarchical` multiple Bloom Components can be used to opt in only the regions around certain objects for blooming.
- [struct BloomOptionsComponent](bloomoptionscomponent.md)
  A component that sets the properties for the bloom post-processing effects.
- [struct ToneMappingComponent](tonemappingcomponent.md)

## See Also

- [Views and attachments](presentation-views-and-attachments.md)
  Bring RealityKit content into your app with views and renderers.
- [Presentation UI](presentation-user-interface.md)
  Control your app’s content and how people can interact with it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/postprocessing-effects)*