# Metal

**Framework**: Metal  
**Kind**: module

Render advanced 3D graphics and compute data in parallel with graphics processors.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

#### Overview

The Metal framework gives your app direct access to a device’s graphics processing unit (GPU). With Metal, apps can leverage a GPU to quickly render complex scenes and run computational tasks in parallel. For example, apps in these categories use Metal to maximize their performance:

- Games that render sophisticated 2D or 3D environments
- Video processing apps, like Final Cut Pro
- Scientific research apps that analyze and process large datasets
- Fully immersive visionOS apps

Metal works hand-in-hand with other frameworks that supplement its capability. For example, [`MetalFX`](https://developer.apple.com/documentation/MetalFX) upscales your renderings in less time than rendering them natively, and [`MetalKit`](https://developer.apple.com/documentation/MetalKit) simplifies the tasks that display your Metal content onscreen. The [`Metal Performance Shaders`](https://developer.apple.com/documentation/metalperformanceshaders) framework provides a large library of optimized compute and rendering shaders that take advantage of each GPU’s unique hardware. In visionOS, create fully immersive stereoscopic content with the help of the [`Compositor Services`](https://developer.apple.com/documentation/CompositorServices) framework.

Many high-level Apple frameworks leverage the performance of Metal, including [`RealityKit`](https://developer.apple.com/documentation/RealityKit), [`SceneKit`](https://developer.apple.com/documentation/SceneKit), [`SpriteKit`](https://developer.apple.com/documentation/SpriteKit), and [`Core Image`](https://developer.apple.com/documentation/coreimage). These high-level frameworks implement the GPU programming details for you. However, you can typically get better performance by writing your own custom Metal and shader code. See the [`Metal Shading Language Specification`](https://developer.apple.comhttps://developer.apple.com/metal/Metal-Shading-Language-Specification.pdf) for shader implementation details.

## Topics

### Essentials
- [Performing Calculations on a GPU](performing-calculations-on-a-gpu.md)
  Use Metal to find GPUs and perform calculations on them.
- [Using Metal to Draw a View’s Contents](using-metal-to-draw-a-view's-contents.md)
  Create a MetalKit view and a render pass to draw the view’s contents.
- [Using a Render Pipeline to Render Primitives](using-a-render-pipeline-to-render-primitives.md)
  Render a simple 2D triangle.
### Samples
- [Metal Sample Code Library](metal-sample-code-library.md)
  Explore the complete set of Metal samples.
### GPU Devices
- [GPU Devices and Work Submission](gpu-devices-and-work-submission.md)
  Find any available GPU, submit work to it with command buffers, suspend work, and coordinate between multiple GPUs.
### Command Encoders
- [Render Passes](render-passes.md)
  Encode a render pass to draw graphics into an image.
- [Compute Passes](compute-passes.md)
  Encode a compute pass that runs computations in parallel on a thread grid, processing and manipulating Metal resource data on multiple cores of a GPU.
- [Blit Passes](blit-passes.md)
  Encode a block information transfer pass to adjust and copy data to and from GPU resources, such as buffers and textures.
- [Indirect Command Encoding](indirect-command-encoding.md)
  Store draw commands in Metal buffers and run them at a later time on the GPU, either once or repeatedly.
- [Ray Tracing with Acceleration Structures](ray-tracing-with-acceleration-structures.md)
  Build a representation of your scene’s geometry using triangles and bounding volumes to quickly trace rays through the scene.
### Resources
- [Resource Fundamentals](resource-fundamentals.md)
  Learn the common attributes of all Metal memory resources, including buffers and textures, and how to manage the underlying memory.
- [Buffers](buffers.md)
  Create and manage untyped data your app uses to exchange information with its shader functions.
- [Textures](textures.md)
  Create and manage typed data your app uses to exchange information with its shader functions.
- [Memory Heaps](memory-heaps.md)
  Take control of your app’s GPU memory management by creating a large memory allocation for various buffers, textures, and other resources.
- [Resource Loading](resource-loading.md)
  Load assets in your games and apps quickly by running a dedicated input/output queue alongside your GPU tasks.
- [Resource Synchronization](resource-synchronization.md)
  Coordinate the contents of data buffers, textures, and other resources that CPUs and GPUs share access to.
### Shaders
- [Stepping through code and inspecting variables to isolate bugs](../Xcode/stepping-through-code-and-inspecting-variables-to-isolate-bugs.md)
  Find the cause of your bugs by watching variables change as you step through your source code in the debugger.
- [Optimizing GPU performance](../Xcode/Optimizing-GPU-performance.md)
  Find and address performance bottlenecks using the Metal debugger.
- [Logging shader debug messages](logging-shader-debug-messages.md)
  Print debugging messages that a shader generates using shader logging.
- [Using Function Specialization to Build Pipeline Variants](using-function-specialization-to-build-pipeline-variants.md)
  Create pipelines for different levels of detail from a common shader source.
- [Shader Libraries](shader-libraries.md)
  Manage and load your app’s Metal shaders.
### Presentation
- [Onscreen Presentation](onscreen-presentation.md)
  Show the output from a GPU’s rendering pass to the user in your app.
- [HDR Content](hdr-content.md)
  Take advantage of high dynamic range to present more vibrant colors in your apps and games.
### User Interface
- [Managing your game window for Metal in macOS](managing-your-game-window-for-metal-in-macos.md)
  Set up a window and view for optimally displaying your Metal content.
- [Adapting your game interface for smaller screens](adapting-your-game-interface-for-smaller-screens.md)
  Make text legible on all devices the player chooses to run your game on.
### Developer Tools
- [Metal developer workflows](../Xcode/Metal-developer-workflows.md)
  Locate and fix issues related to your app’s use of the Metal API and GPU functions.
- [Metal debugger](../Xcode/Metal-debugger.md)
  Debug and profile your Metal workload with a GPU trace.
- [Improving your game’s graphics performance and settings](improving-your-games-graphics-performance-and-settings.md)
  Fix performance glitches and develop default settings for smooth experiences on Apple platforms using the powerful suite of Metal development tools.
- [Capturing Metal Commands Programmatically](capturing-metal-commands-programmatically.md)
  Invoke Metal’s frame capture from your app, then save the resulting GPU trace to a file or view it in Xcode.
- [Supporting Simulator in a Metal app](supporting-simulator-in-a-metal-app.md)
  Configure alternative render paths in your Metal app to enable running your app in Simulator.
- [Analyzing the memory usage of your Metal app](../Xcode/Analyzing-the-memory-usage-of-your-Metal-app.md)
  Keep your app alive in the background by managing its memory footprint.
- [Analyzing the performance of your Metal app](../Xcode/Analyzing-the-performance-of-your-Metal-app.md)
  Ensure consistent, smooth rendering by profiling your app’s frame time.
- [Developing Metal apps that run in Simulator](developing-metal-apps-that-run-in-simulator.md)
  Prototype and test your Metal apps in Simulator.
- [GPU Counters and Counter Sample Buffers](gpu-counters-and-counter-sample-buffers.md)
  Retrieve runtime data from a GPU device by sampling one or more of its counters.
- [Metal Debugging Types](metal-debugging-types.md)
  Create capture managers and capture scopes, and review a GPU device’s log after it runs a command buffer.
### Apple Silicon
- [Porting your Metal code to Apple silicon](../Apple-Silicon/porting-your-metal-code-to-apple-silicon.md)
  Create a version of your Metal app that runs on both Apple silicon and Intel-based Mac computers.
- [Tailor Your Apps for Apple GPUs and Tile-Based Deferred Rendering](tailor-your-apps-for-apple-gpus-and-tile-based-deferred-rendering.md)
  Learn about characteristic Apple GPU features, including imageblocks, tile shaders, and raster order groups.
### Reference
- [Metal Structures](metal-structures.md)
- [Metal Enumerations](metal-enumerations.md)
- [Metal Constants](metal-constants.md)
- [Metal Data Types](metal-data-types.md)
- [Metal Variables](metal-variables.md)

## See Also

- [Metal Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Miscellaneous/Conceptual/MetalProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014221)
- [Metal Best Practices Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/3DDrawing/Conceptual/MTLBestPracticesGuide/index.html#//apple_ref/doc/uid/TP40016642)


---

*[View on Apple Developer](https://developer.apple.com/documentation/Metal)*