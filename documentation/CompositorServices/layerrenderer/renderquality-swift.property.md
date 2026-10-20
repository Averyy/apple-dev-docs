# renderQuality

**Framework**: Compositor Services  
**Kind**: property

Get the render quality to be used by the drawables.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var renderQuality: LayerRenderer.RenderQuality { get set }
```

## Mentions

- [Defining layer renderer quality](defining-layer-renderer-quality.md)

#### Discussion

The render quality will increase the resolution at which rendering happens. This value cannot exceed the quality specified on the layer renderer configuration see [`cp_layer_renderer_configuration_set_max_render_quality`](cp_layer_renderer_configuration_set_max_render_quality.md). The quality will be changed to the target render quality over a set duration to hide the transition of quality from the user.

The renderer should monitor its frame rate to determine whether its making the frames on time. If it is unable to maintain proper frame rate, the app should reduce the render quality, reduce the scene complexity, or increase the frame repeat count see [`cp_layer_renderer_set_minimum_frame_repeat_count`](cp_layer_renderer_set_minimum_frame_repeat_count.md). It is generally preferable to reduce anything else before increasing the frame repeat count.

## See Also

- [var defaultRenderQuality: LayerRenderer.RenderQuality](layerrenderer/capabilities/defaultrenderquality.md)
  The default render quality used on this platform.
- [var maxRenderQuality: LayerRenderer.RenderQuality](layerrenderer/configuration-swift.struct/maxrenderquality.md)
  The max render quality the layer can use when drawing to the drawables.
- [Defining layer renderer quality](defining-layer-renderer-quality.md)
  Declare the render quality of your textures to enable high-quality rendering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/renderquality-swift.property)*