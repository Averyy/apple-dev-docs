# Achieving smooth frame rates with a Metal display link

**Framework**: Metal

Pace rendering with minimal input latency while providing essential information to the operating system for power-efficient rendering, thermal mitigation, and the scheduling of sustainable workloads.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- tvOS 17.0+
- Xcode 15.3+

#### Overview

> **Note**: This sample code project is associated with WWDC23 session 10123: [`Bring your game to Mac: Make a game plan`](https://developer.apple.comhttps://developer.apple.com/wwdc23/10123/).

## See Also

- [Using Metal to draw a view’s contents](using-metal-to-draw-a-view's-contents.md)
  Create a MetalKit view and a render pass to draw the view’s contents.
- [Drawing a triangle with Metal 4](drawing-a-triangle-with-metal-4.md)
  Render a colorful, rotating 2D triangle by running draw commands with a render pipeline on a GPU.
- [Selecting device objects for graphics rendering](selecting-device-objects-for-graphics-rendering.md)
  Switch dynamically between multiple GPUs to efficiently render to a display.
- [Customizing render pass setup](customizing-render-pass-setup.md)
  Render into an offscreen texture by creating a custom render pass.
- [Creating a custom Metal view](creating-a-custom-metal-view.md)
  Implement a lightweight view for Metal rendering that’s customized to your app’s needs.
- [Calculating primitive visibility using depth testing](calculating-primitive-visibility-using-depth-testing.md)
  Determine which pixels are visible in a scene by using a depth texture.
- [Encoding indirect command buffers on the CPU](encoding-indirect-command-buffers-on-the-cpu.md)
  Reduce CPU overhead and simplify your command execution by reusing commands.
- [Implementing order-independent transparency with image blocks](implementing-order-independent-transparency-with-image-blocks.md)
  Draw overlapping, transparent surfaces in any order by using tile shaders and image blocks.
- [Loading textures and models using Metal fast resource loading](loading-textures-and-models-using-metal-fast-resource-loading.md)
  Stream texture and buffer data directly from disk into Metal resources using fast resource loading.
- [Adjusting the level of detail using Metal mesh shaders](adjusting-the-level-of-detail-using-metal-mesh-shaders.md)
  Choose and render meshes with several levels of detail using object and mesh shaders.
- [Creating a 3D application with hydra rendering](creating-a-3d-application-with-hydra-rendering.md)
  Build a 3D application that integrates with Hydra and USD.
- [Culling occluded geometry using the visibility result buffer](culling-occluded-geometry-using-the-visibility-result-buffer.md)
  Draw a scene without rendering hidden geometry by checking whether each object in the scene is visible.
- [Improving edge-rendering quality with multisample antialiasing (MSAA)](improving-edge-rendering-quality-with-multisample-antialiasing-msaa.md)
  Apply MSAA to enhance the rendering of edges with custom resolve options and immediate and tile-based resolve paths.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/achieving-smooth-frame-rates-with-a-metal-display-link)*