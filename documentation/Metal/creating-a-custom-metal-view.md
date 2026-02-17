# Creating a custom Metal view

**Framework**: Metal

Implement a lightweight view for Metal rendering that’s customized to your app’s needs.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 12.0+
- macOS 10.13+
- tvOS 12.0+
- Xcode 12.0+

#### Overview

While MetalKit’s [`MTKView`](https://developer.apple.com/documentation/MetalKit/MTKView) provides significant functionality, allowing you to quickly get started writing Metal code, sometimes you want more control over how your Metal content is rendered. This sample app demonstrates how to create a simple Metal view derived directly from an [`NSView`](https://developer.apple.com/documentation/AppKit/NSView) or [`UIView`](https://developer.apple.com/documentation/UIKit/UIView). It uses a [`CAMetalLayer`](https://developer.apple.com/documentation/QuartzCore/CAMetalLayer) object to hold the view’s contents.

##### Configure the Sample Code Project

This sample has targets for iOS, tvOS, and macOS. There are significant differences between apps that use UIKit and AppKit. Because of these differences, this sample creates two different classes. The iOS and tvOS versions of the sample use the `AAPLUIView` class, and the macOS version uses the `AAPLNSView` class. Both are derived from a common `AAPLView` class.

This sample provides a number of options you can enable when building the app, such as whether to animate the view’s contents or handle updates through system events. You control these options by changing the preprocessor definitions in the `AAPLConfig.h` file.

##### Configure the View with a Metal Layer

For Metal to render to the view, the view needs to be backed by a [`CAMetalLayer`](https://developer.apple.com/documentation/QuartzCore/CAMetalLayer).

All views in UIKit are layer backed. To indicate the type of layer backing, the view implements the `layerClass` class method.  To indicate that your view should be backed by a `CAMetalLayer`, you need to return the `CAMetalLayer` class type.

In AppKit, you make the view layer backed by setting the view’s `wantsLayer` property.

This triggers a call to the view’s  `makeBackingLayer` method, which returns a CAMetalLayer object.

##### Render to the View

To render to the view, create an [`MTLRenderPassDescriptor`](mtlrenderpassdescriptor.md) object that targets a texture provided by the layer. The `AAPLRenderer` class stores the render pass descriptor in the `_drawableRenderPassDescriptor` instance variable. Most of the properties of this descriptor are set up automatically when you initialize the renderer. The code configures the render pass to clear the contents of the texture, and to store any rendered contents to the texture when the render pass completes.

You also need to set the texture that the render pass renders into. Each time the app renders a frame, the renderer obtains a [`CAMetalDrawable`](https://developer.apple.com/documentation/QuartzCore/CAMetalDrawable) from the Metal layer. The drawable provides a texture for Core Animation to present onscreen. The renderer updates the render pass descriptor to render to this texture:

The rest of the rendering code is similar to that found in other Metal samples. For an explanation of a typical rendering path, see [`Drawing a triangle with Metal 4`](drawing-a-triangle-with-metal-4.md).

##### Implement a Render Loop

To animate the view, the sample sets up a display link. The display link calls the view at the specified interval, synchronizing updates to the display’s refresh interval. The view calls the renderer object to render a new frame of animation.

`AAPLUIView` creates a [`CADisplayLink`](https://developer.apple.com/documentation/QuartzCore/CADisplayLink) in the `setupCADisplayLinkForScreen` method. Because you need to know which screen the window is on before creating the display link, you call this method when UIKit calls your view’s [`didMoveToWindow()`](https://developer.apple.com/documentation/UIKit/UIView/didMoveToWindow()) method. UIKit calls this method the first time the view is added to a window and when the view is moved to another screen. The code below stops the render loop and initializes a new display link.

`AAPLNSView` uses a [`CVDisplayLink`](https://developer.apple.com/documentation/CoreVideo/cvdisplaylink-k0k) instead of a `CADisplayLink` because `CADisplayLink` is not available on macOS. `CVDisplayLink` and `CADisplayLink` API look different, but, in principle, have the same goal, which is to allow callbacks in sync with the display. `AAPLNSView` creates a `CVDisplayLink` in the `setupCVDisplayLinkForScreen` method.  The `setupCVDisplayLinkForScreen` method is called from [`viewDidMoveToWindow()`](https://developer.apple.com/documentation/AppKit/NSView/viewDidMoveToWindow()), which AppKit calls immediately after loading the view. If the view is moved to another screen, AppKit also calls `viewDidMoveToWindow`, and like the previous code for UIKit, the AppKit view needs to recreate the display link for the new screen.

The macOS version of this code performs a few additional steps. After creating the display link, it sets the callback and a parameter to pass to the callback. If you want rendering to happen on the main thread, it passes a dispatch source object; otherwise, it passes a reference to the view itself. Finally, it tells the display link which display the window is located on, and sets a notification to be called when the window is closed.

## See Also

- [Using Metal to draw a view’s contents](using-metal-to-draw-a-view's-contents.md)
  Create a MetalKit view and a render pass to draw the view’s contents.
- [Drawing a triangle with Metal 4](drawing-a-triangle-with-metal-4.md)
  Render a colorful, rotating 2D triangle by running draw commands with a render pipeline on a GPU.
- [Selecting device objects for graphics rendering](selecting-device-objects-for-graphics-rendering.md)
  Switch dynamically between multiple GPUs to efficiently render to a display.
- [Customizing render pass setup](customizing-render-pass-setup.md)
  Render into an offscreen texture by creating a custom render pass.
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
- [Achieving smooth frame rates with a Metal display link](achieving-smooth-frame-rates-with-a-metal-display-link.md)
  Pace rendering with minimal input latency while providing essential information to the operating system for power-efficient rendering, thermal mitigation, and the scheduling of sustainable workloads.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/creating-a-custom-metal-view)*