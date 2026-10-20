# queryDrawable()

**Framework**: Compositor Services  
**Kind**: method  
**Role**: Instance Method

Retrieves the frame’s drawable, which contains the textures and drawing environment for the frame.

**Availability**:
- visionOS 1.0+ - Deprecated in 26.0 (renamed: queryDrawables)

## Declaration

```swift
func queryDrawable() -> LayerRenderer.Drawable?
```

#### Return Value

The drawable type, or `nil` if the layer is in the [`LayerRenderer.State.paused`](../state-swift.enum/paused.md) or [`LayerRenderer.State.invalidated`](../state-swift.enum/invalidated.md) state.

#### Discussion

Fetch the drawable when you’re ready to encode the drawing commands for the frame. The [`LayerRenderer.Drawable`](../drawable.md) type contains the textures and other information you need to set up your render descriptor in Metal.

## See Also

### Getting the drawable environment
- [func queryDrawables() -> [LayerRenderer.Drawable]](./querydrawables%28%29.md)
  Returns the array of drawables expected to be used for the given frame. These drawables each have textures, transforms and timing information for drawing the frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/frame/querydrawable())*