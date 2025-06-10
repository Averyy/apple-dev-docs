# queryDrawables()

**Framework**: Compositor Services  
**Kind**: method

Returns the array of drawables expected to be used for the given frame. These drawables each have textures, transforms and timing information for drawing the frame.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func queryDrawables() -> [LayerRenderer.Drawable]
```

#### Return Value

The drawable array, if the layer is in the `LayerRenderer.State.paused` or `LayerRenderer.State.invalidated` states the array will have a count of 0 and frame is invalid.

#### Discussion

Call this function when you’re ready to encode the drawing commands for the frame. The `LayerRenderer.Drawable` type contains the textures and other information you need to set up your render descriptor in Metal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/frame/querydrawables())*