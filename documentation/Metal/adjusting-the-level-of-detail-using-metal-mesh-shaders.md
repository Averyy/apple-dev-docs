# Adjusting the level of detail using Metal mesh shaders

**Framework**: Metal

Choose and render meshes with several levels of detail using object and mesh shaders.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 13.0+
- Xcode 14.0+

#### Overview

> **Note**: This sample code project is associated with WWDC22 session [`10162: Transform your geometry with Metal mesh shaders`](https://developer.apple.comhttps://developer.apple.com/wwdc22/10162/).

##### Configure the Sample Code Project

To run this sample, you need Xcode 14 or later, and a physical device that supports [`MTLGPUFamily.mac2`](mtlgpufamily/mac2.md) or [`MTLGPUFamily.apple7`](mtlgpufamily/apple7.md), such as:

- A Mac running macOS 13 or later
- An iOS device with an A15 chip or later running iOS 16 or later

This sample can only run on a physical device because it uses Metal’s mesh shader features, which Simulator doesn’t support.

## See Also

- [Using Metal to Draw a View’s Contents](using-metal-to-draw-a-view's-contents.md)
  Create a MetalKit view and a render pass to draw the view’s contents.
- [Using a Render Pipeline to Render Primitives](using-a-render-pipeline-to-render-primitives.md)
  Render a colorful, 2D triangle by running a draw command on the GPU.
- [Selecting Device Objects for Graphics Rendering](selecting-device-objects-for-graphics-rendering.md)
  Switch dynamically between multiple GPUs to efficiently render to a display.
- [Customizing Render Pass Setup](customizing-render-pass-setup.md)
  Render into an offscreen texture by creating a custom render pass.
- [Creating a Custom Metal View](creating-a-custom-metal-view.md)
  Implement a lightweight view for Metal rendering that’s customized to your app’s needs.
- [Calculating Primitive Visibility Using Depth Testing](calculating-primitive-visibility-using-depth-testing.md)
  Determine which pixels are visible in a scene by using a depth texture.
- [Encoding Indirect Command Buffers on the CPU](encoding-indirect-command-buffers-on-the-cpu.md)
  Reduce CPU overhead and simplify your command execution by reusing commands.
- [Implementing Order-Independent Transparency with Image Blocks](implementing-order-independent-transparency-with-image-blocks.md)
  Draw overlapping, transparent surfaces in any order by using tile shaders and image blocks.
- [Loading textures and models using Metal fast resource loading](loading-textures-and-models-using-metal-fast-resource-loading.md)
  Stream texture and buffer data directly from disk into Metal resources using fast resource loading.
- [Creating a 3D application with Hydra rendering](creating-a-3d-application-with-hydra-rendering.md)
  Build a 3D application that integrates with Hydra and USD.
- [Culling occluded geometry using the visibility result buffer](culling-occluded-geometry-using-the-visibility-result-buffer.md)
  Draw a scene without rendering hidden geometry by checking whether each object in the scene is visible.
- [Improving edge-rendering quality with multisample antialiasing (MSAA)](improving-edge-rendering-quality-with-multisample-antialiasing-msaa.md)
  Use Metal’s MSAA to enhance the rendering of edges with custom resolve options and immediate and tile-based resolve paths.
- [Achieving smooth frame rates with Metal’s display link](achieving-smooth-frame-rates-with-metal-s-display-link.md)
  Pace rendering with minimal input latency while providing essential information to the operating system for power-efficient rendering, thermal mitigation, and the scheduling of sustainable workloads.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/adjusting-the-level-of-detail-using-metal-mesh-shaders)*