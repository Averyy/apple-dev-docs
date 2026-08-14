# Improving the Performance of a RealityKit App

**Framework**: RealityKit

Measure CPU and GPU utilization to find ways to improve your app’s performance.

#### Overview

You use the RealityKit framework to add 3D content to an [`ARKit`](https://developer.apple.com/documentation/arkit) app. The framework runs an entity component system (ECS) on the CPU to manage tasks like physics calculations, animations, audio processing, and network synchronization. It also relies on the [`Metal`](https://developer.apple.com/documentation/metal) framework and GPU hardware to perform multithreaded rendering.

![A diagram showing how your app runs on the CPU, supported by RealityKit, ARKit, and Metal, with Metal running vertex, compute, and fragment shaders on the GPU, resulting in your app’s content rendering on the display.](/images/com.apple.RealityKit/improving-the-performance-of-a-realitykit-app-1@2x.png)

Although RealityKit handles much of the complexity of this system for you, it’s still important to optimize your app for performance. Use debugging features built in to RealityKit — along with standard tools like Xcode and Instruments — to pinpoint the causes of reduced frame rate. Then make data-driven adjustments to your assets or to the way you use the framework to improve performance.

##### Locate Performance Bottlenecks

To address performance problems, you need data. RealityKit provides a debugging option to collect a basic set of statistics, like CPU utilization, ECS operations, and memory footprint. Add the [`showStatistics`](arview/debugoptions-swift.struct/showstatistics.md) option to the [`debugOptions`](arview/debugoptions-swift.property.md) option set of your [`ARView`](arview.md):

```swift
arView.debugOptions.insert(.showStatistics)
```

As a result, the view draws an overlay that displays statistics, updated in real time.

![A screenshot of a RealityKit app running on an iPad, showing statistics in the lower third of the display overlaid with partial transparency onto a scene with a virtual cube placed on a real wooden surface.](/images/com.apple.RealityKit/improving-the-performance-of-a-realitykit-app-2@2x.png)

RealityKit typically limits the refresh rate — the rate at which the framework renders updates for the screen — to 60 frames per second (fps). This rate limits each of the main and render threads, as well as the GPU, to 16.6 ms to complete all computations per rendered frame. The overlay reports the observed frame rate, as well as the measured main and render thread times. It also provides granular detail about time spent in the main thread, such as when performing tasks like ECS updates and physics calculations. For more information about the visible metrics, see [`showStatistics`](arview/debugoptions-swift.struct/showstatistics.md).

If the main thread consumes more than 16.6 ms, then the app is CPU limited. If not, but the frame rate remains consistently below 60 fps, then the app is probably GPU limited. Use this information and the other data in the overlay to drive changes in your app.

> 💡 **Tip**: If you need more detailed data, use tools like Xcode’s [`debug gauges`](https://developer.apple.comhttps://help.apple.com/xcode/mac/current/#/dev94c128b7b) and the [`Instruments`](https://developer.apple.comhttps://help.apple.com/instruments/mac/current/) app. Combined with OS signposts, available among the [`Logging`](https://developer.apple.com/documentation/os/logging) methods of the [`os`](https://developer.apple.com/documentation/os) framework, you can identify processor utilization with a great deal of precision, as described in [`Improving your app’s performance`](https://developer.apple.com/documentation/xcode/improving-your-app-s-performance).

##### Reduce Cpu Utilization

For an app that’s CPU limited, examine what RealityKit task or tasks — like rendering, ECS, physics, network, and so on — consume the most time during each frame. Also consider your app’s custom logic, which contributes to the main thread time. Then target the appropriate areas for optimization, as described in [`Reducing CPU Utilization in Your RealityKit App`](reducing-cpu-utilization-in-your-realitykit-app.md).

##### Reduce Gpu Utilization

If your app is GPU limited, look for ways to reduce render work. For example, you can reduce the complexity of your content, like textures, meshes, and materials. Alternatively, you can disable or scale back certain render features, like depth of field, shadows, and environmental texturing. For more information, see [`Reducing GPU Utilization in Your RealityKit App`](reducing-gpu-utilization-in-your-realitykit-app.md).

##### Make Runtime Adjustments for Older Devices

Be sure to test your app on all supported devices before shipping your app. If you find that older devices can’t achieve the full frame rate, experiment with complexity reductions that you can make dynamically. For example:

- Scale back effects, as described in [`Choose render effects carefully`](reducing-gpu-utilization-in-your-realitykit-app#Choose-render-effects-carefully.md). Depth of field and motion blur tend to be particularly expensive.
- Substitute simpler models with fewer polygons in place of your standard models.
- Reduce the rendering resolution by scaling the [`contentScaleFactor`](arview/contentscalefactor.md) property of the view, whose default value depends on the device:

```swift
// Capture the default value after you initialize the view.
let defaultScaleFactor = arView.contentScaleFactor

// Scale as needed. For example, here the scale factor is
// set to 75% of the default value.
arView.contentScaleFactor = 0.75 * defaultScaleFactor
```

Determine which adjustments you need for different kinds of hardware, and then choose different code paths based on the hardware you detect at runtime. To learn about identifying the available GPU hardware, see [`Detecting GPU features and Metal software versions`](https://developer.apple.com/documentation/metal/detecting-gpu-features-and-metal-software-versions).

## Topics

### Optimization targets
- [Reducing CPU Utilization in Your RealityKit App](reducing-cpu-utilization-in-your-realitykit-app.md)
  Target specific CPU metrics with adjustments to your app and its content.
- [Reducing GPU Utilization in Your RealityKit App](reducing-gpu-utilization-in-your-realitykit-app.md)
  Prevent the GPU from limiting your app’s frame rate by reducing the complexity of your render.
### Level of detail
- [struct LevelOfDetailComponent](levelofdetailcomponent.md)
  A component that enables Level of Detail (LOD) optimization for entities with multiple detail levels.

## See Also

- [Reducing GPU Utilization in Your RealityKit App](reducing-gpu-utilization-in-your-realitykit-app.md)
  Prevent the GPU from limiting your app’s frame rate by reducing the complexity of your render.
- [Reducing CPU Utilization in Your RealityKit App](reducing-cpu-utilization-in-your-realitykit-app.md)
  Target specific CPU metrics with adjustments to your app and its content.
- [Construct an immersive environment for visionOS](construct-an-immersive-environment-for-visionos.md)
  Build efficient custom worlds for your app.
- [Passing Metal command objects around your application](passing-metal-command-objects-around-your-application.md)
  Build a system that creates and passes Metal command objects to entities dispatching Metal compute shaders.
- [Low-level rendering](low-level-rendering.md)
  Drive the renderer directly to build custom drawing pipelines, meshes, buffers, and textures when higher-level rendering does not give you the control you need.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/improving-the-performance-of-a-realitykit-app)*