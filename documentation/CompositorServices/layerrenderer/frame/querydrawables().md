# queryDrawables()

**Framework**: Compositor Services  
**Kind**: method  
**Role**: Instance Method

Returns the array of drawables expected to be used for the given frame. These drawables each have textures, transforms and timing information for drawing the frame.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func queryDrawables() -> [LayerRenderer.Drawable]
```

## Mentions

- [Drawing fully immersive content using Metal](../../drawing-fully-immersive-content-using-metal.md)

## Return Value

The drawable array, if the layer is in the `LayerRenderer.State.paused` or `LayerRenderer.State.invalidated` states the array will have a count of 0 and frame is invalid.

## Discussion

Call this function when you’re ready to encode the drawing commands for the frame. The `LayerRenderer.Drawable` type contains the textures and other information you need to set up your render descriptor in Metal.

## See Also

### Getting the drawable environment
- [func queryDrawable() -> LayerRenderer.Drawable?](./querydrawable%28%29.md)
  Retrieves the frame’s drawable, which contains the textures and drawing environment for the frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/frame/querydrawables())*