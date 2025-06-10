# Metal Sample Code Library

**Framework**: Metal

Explore the complete set of Metal samples.

#### Overview

Browse the topics below to find samples relevant to a concept you want to learn more about, starting with the basic computation and render workflows. The samples in the lighting and multiple technique sections demonstrate how to take advantage of the unique GPU architecture of Apple silicon.

## Topics

### Compute Workflows
- [Performing Calculations on a GPU](performing-calculations-on-a-gpu.md)
  Use Metal to find GPUs and perform calculations on them.
- [Selecting Device Objects for Compute Processing](selecting-device-objects-for-compute-processing.md)
  Switch dynamically between multiple GPUs to efficiently execute a compute-intensive simulation.
- [Customizing a TensorFlow operation](customizing-a-tensorflow-operation.md)
  Implement a custom operation that uses Metal kernels to accelerate neural-network training performance.
- [Customizing a PyTorch operation](customizing-a-pytorch-operation.md)
  Implement a custom operation in PyTorch that uses Metal kernels to improve performance.
### Render Workflows
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
- [Adjusting the level of detail using Metal mesh shaders](adjusting-the-level-of-detail-using-metal-mesh-shaders.md)
  Choose and render meshes with several levels of detail using object and mesh shaders.
- [Creating a 3D application with Hydra rendering](creating-a-3d-application-with-hydra-rendering.md)
  Build a 3D application that integrates with Hydra and USD.
- [Culling occluded geometry using the visibility result buffer](culling-occluded-geometry-using-the-visibility-result-buffer.md)
  Draw a scene without rendering hidden geometry by checking whether each object in the scene is visible.
- [Improving edge-rendering quality with multisample antialiasing (MSAA)](improving-edge-rendering-quality-with-multisample-antialiasing-msaa.md)
  Use Metal’s MSAA to enhance the rendering of edges with custom resolve options and immediate and tile-based resolve paths.
- [Achieving smooth frame rates with Metal’s display link](achieving-smooth-frame-rates-with-metal-s-display-link.md)
  Pace rendering with minimal input latency while providing essential information to the operating system for power-efficient rendering, thermal mitigation, and the scheduling of sustainable workloads.
### Textures
- [Processing a texture in a compute function](processing-a-texture-in-a-compute-function.md)
  Create textures by running copy and dispatch commands in a compute pass on a GPU.
- [Reading Pixel Data from a Drawable Texture](reading-pixel-data-from-a-drawable-texture.md)
  Access texture data from the CPU by copying it to a buffer.
- [Creating and Sampling Textures](creating-and-sampling-textures.md)
  Load image data into a texture and apply it to a quadrangle.
- [Streaming large images with Metal sparse textures](streaming-large-images-with-metal-sparse-textures.md)
  Limit texture memory usage for large textures by loading or unloading image detail on the basis of MIP and tile region.
### Argument Buffers
- [Managing groups of resources with argument buffers](managing-groups-of-resources-with-argument-buffers.md)
  Create argument buffers to organize related resources.
- [Using Argument Buffers with Resource Heaps](using-argument-buffers-with-resource-heaps.md)
  Reduce CPU overhead by using arrays inside argument buffers and combining them with resource heaps.
- [Encoding Argument Buffers on the GPU](encoding-argument-buffers-on-the-gpu.md)
  Use a compute pass to encode an argument buffer and access its arguments in a subsequent render pass.
- [Rendering Terrain Dynamically with Argument Buffers](rendering-terrain-dynamically-with-argument-buffers.md)
  Use argument buffers to render terrain in real time with a GPU-driven pipeline.
### Shaders
- [Creating a Metal Dynamic Library](creating-a-metal-dynamic-library.md)
  Compile a library of shaders and write it to a file as a dynamically linked library.
- [Using Function Specialization to Build Pipeline Variants](using-function-specialization-to-build-pipeline-variants.md)
  Create pipelines for different levels of detail from a common shader source.
### Synchronization
- [Synchronizing CPU and GPU Work](synchronizing-cpu-and-gpu-work.md)
  Avoid stalls between CPU and GPU work by using multiple instances of a resource.
- [Implementing a Multistage Image Filter Using Heaps and Events](implementing-a-multistage-image-filter-using-heaps-and-events.md)
  Use events to synchronize access to resources allocated on a heap.
- [Implementing a Multistage Image Filter Using Heaps and Fences](implementing-a-multistage-image-filter-using-heaps-and-fences.md)
  Use fences to synchronize access to resources allocated on a heap.
### Lighting Techniques
- [Rendering a Scene with Forward Plus Lighting Using Tile Shaders](rendering-a-scene-with-forward-plus-lighting-using-tile-shaders.md)
  Implement a forward plus renderer using the latest features on Apple GPUs.
- [Rendering a Scene with Deferred Lighting in Objective-C](rendering-a-scene-with-deferred-lighting-in-objective-c.md)
  Avoid expensive lighting calculations by implementing a deferred lighting renderer optimized for immediate mode and tile-based deferred renderer GPUs.
- [Rendering a Scene with Deferred Lighting in Swift](rendering-a-scene-with-deferred-lighting-in-swift.md)
  Avoid expensive lighting calculations by implementing a deferred lighting renderer optimized for immediate mode and tile-based deferred renderer GPUs.
- [Rendering a Scene with Deferred Lighting in C++](rendering-a-scene-with-deferred-lighting-in-c++.md)
  Avoid expensive lighting calculations by implementing a deferred lighting renderer optimized for immediate mode and tile-based deferred renderer GPUs.
- [Rendering Reflections with Fewer Render Passes](rendering-reflections-with-fewer-render-passes.md)
  Use layer selection to reduce the number of render passes needed to generate an environment map.
### Multiple Techniques
- [Modern Rendering with Metal](modern-rendering-with-metal.md)
  Use advanced Metal features such as indirect command buffers, sparse textures, and variable rate rasterization to implement complex rendering techniques.
- [Encoding Indirect Command Buffers on the GPU](encoding-indirect-command-buffers-on-the-gpu.md)
  Maximize CPU to GPU parallelization by generating render commands on the GPU.
### Ray Tracing
- [Rendering reflections in real time using ray tracing](rendering-reflections-in-real-time-using-ray-tracing.md)
  Implement realistic real-time lighting by dynamically generating reflection maps by encoding a ray-tracing compute pass.
- [Accelerating ray tracing using Metal](accelerating-ray-tracing-using-metal.md)
  Implement ray-traced rendering using GPU-based parallel processing.
- [Control the Ray Tracing Process Using Intersection Queries](control-the-ray-tracing-process-using-intersection-queries.md)
  Explicitly enumerate a ray’s intersections with acceleration structures by creating an intersection query object.
- [Accelerating ray tracing and motion blur using Metal](accelerating-ray-tracing-and-motion-blur-using-metal.md)
  Generate ray-traced images with motion blur using GPU-based parallel processing.
- [Rendering a curve primitive in a ray tracing scene](rendering-a-curve-primitive-in-a-ray-tracing-scene.md)
  Implement ray traced rendering using GPU-based parallel processing.
### HDR
- [Processing HDR Images with Metal](processing-hdr-images-with-metal.md)
  Implement a post-processing pipeline using the latest features on Apple GPUs.
### OpenGL
- [Migrating OpenGL Code to Metal](migrating-opengl-code-to-metal.md)
  Replace your app’s deprecated OpenGL code with Metal.
- [Mixing Metal and OpenGL Rendering in a View](mixing-metal-and-opengl-rendering-in-a-view.md)
  Draw with Metal and OpenGL in the same view using an interoperable texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/metal-sample-code-library)*