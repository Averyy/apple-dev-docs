# queryDrawable()

**Framework**: Compositor Services  
**Kind**: method

Retrieves the frame’s drawable, which contains the textures and drawing environment for the frame.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
func queryDrawable() -> LayerRenderer.Drawable?
```

#### Return Value

The drawable type, or `nil` if the layer is in the [`LayerRenderer.State.paused`](layerrenderer/state-swift.enum/paused.md) or [`LayerRenderer.State.invalidated`](layerrenderer/state-swift.enum/invalidated.md) state.

#### Discussion

Fetch the drawable when you’re ready to encode the drawing commands for the frame. The [`LayerRenderer.Drawable`](layerrenderer/drawable.md) type contains the textures and other information you need to set up your render descriptor in Metal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/frame/querydrawable())*