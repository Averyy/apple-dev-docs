# addRenderContext()

**Framework**: Compositor Services  
**Kind**: method

Adds a render context to a drawable. This object will draw any content that the compositor needs to render in the application.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func addRenderContext() -> LayerRenderer.Drawable.RenderContext
```

#### Discussion

> **Note**: The render context can only be used when the layer renderer is using layered layout or in platforms that only render one view (ex: simulator)

> **Note**: The render context makes use of the device_anchor set in [`cp_drawable_set_device_anchor`](cp_drawable_set_device_anchor.md) the device_anchor should be set in the drawable before calling [`addRenderContext(commandBuffer:)`](layerrenderer/drawable/addrendercontext(commandbuffer:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/drawable/addrendercontext())*