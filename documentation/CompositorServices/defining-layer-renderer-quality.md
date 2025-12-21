# Defining layer renderer quality

**Framework**: Compositor Services

Declare the render quality of your textures to enable high-quality rendering.

#### Overview

When rendering with Metal in visionOS, you need to define the render quality that best fits your app’s content. Text and other UI elements require less graphics power and benefit from higher resolution. Complex 3D scenes that require more graphic power can benefit from rendering at a lower resolution with more compute power available for every pixel. This API allows you to dynamically change the quality based on what your application is rendering.

> ❗ **Important**: Increasing the rednering quality of textures in your app can have an impact on memory usage and performance. Be sure to measure the behavior of your app in various rendering scenarios to find the appropriate balance between quality and performance for your app’s content.

##### Identify the Default Render Quality

The [`defaultRenderQuality`](layerrenderer/capabilities/defaultrenderquality.md) property provides the default render quality. This value can vary on a system-by-system basis making it important to query the specific system value rather than expecting a constant value. Use the default render quality in your calculation of the maximum and preferred render quality when adopting higher-fidelity textures.

```swift
// Layer capabilities.
struct MyConfiguration: CompositorLayerConfiguration {
    func makeConfiguration(capabilities: LayerRenderer.Capabilities,
                           configuration: inout LayerRenderer.Configuration) {
        let defaultQuality = capabilities.defaultRenderQuality

        // Configure other aspects of LayerRenderer.
    }
}
```

##### Set the Maximum Render Quality

Set a maximum render quality for your app as the first step in adopting higher-fidelity textures. This sets the upper limit for your rendering assertion. Adjust the quality of your displayed content within the range you set. Set the [`maxRenderQuality`](layerrenderer/configuration-swift.struct/maxrenderquality.md) to the minium value for your content to avoid overusing computation resources.

The following code sample sets a maximum render quality of `0.8` in the [`LayerRenderer.Configuration`](layerrenderer/configuration-swift.struct.md). Modifying the render quality only makes sense in the presence of foveation, so the sample performs a check for [`isFoveationEnabled`](layerrenderer/configuration-swift.struct/isfoveationenabled.md) first.

```swift
// Layer configuration.
struct MyConfiguration: CompositorLayerConfiguration {
    func makeConfiguration(capabilities: LayerRenderer.Capabilities,
                           configuration: inout LayerRenderer.Configuration) {
        // Configure other aspects of LayerRenderer.

        if configuration.isFoveationEnabled {
            configuration.maxRenderQuality = LayerRenderer.RenderQuality(0.8)
        }
    }
}
```

##### Set the Desired Render Quality for a Scene

Similarly, you can set the desired render quality with the [`renderQuality`](layerrenderer/renderquality-swift.property.md) property. When loading a scene, set the desired render quality appropriate for that scene. The final visual product doesn’t immediately reflect the updated render quality. The system smooths the transition to the desired quality.

```swift
extension Renderer {
    func adjustRenderQuality(for scene: MyScene) {
        guard layerRenderer.configuration.isFoveationEnabled else {
            return
        }
        layerRenderer.renderQuality = scene.renderQuality
    }
}
```

For more information, see WWDC25 session 294 [`What’s new in Metal rendering for immersive apps`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2025/294).

## See Also

- [var renderQuality: LayerRenderer.RenderQuality](layerrenderer/renderquality-swift.property.md)
  Get the render quality to be used by the drawables.
- [var defaultRenderQuality: LayerRenderer.RenderQuality](layerrenderer/capabilities/defaultrenderquality.md)
  The default render quality used on this platform.
- [var maxRenderQuality: LayerRenderer.RenderQuality](layerrenderer/configuration-swift.struct/maxrenderquality.md)
  The max render quality the layer can use when drawing to the drawables.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/defining-layer-renderer-quality)*