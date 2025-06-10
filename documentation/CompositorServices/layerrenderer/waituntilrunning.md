# waitUntilRunning()

**Framework**: Compositor Services  
**Kind**: method

Stops further execution of your code until the layer renderer leaves the paused state.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 1.0+

## Declaration

```swift
func waitUntilRunning()
```

#### Discussion

Call this function to let the system handle events while you wait for the layer to become ready. The function services incoming layer-related events until the layer exits the paused state.

## See Also

- [var state: LayerRenderer.State](layerrenderer/state-swift.property.md)
  A value that indicates whether the layer renderer is currently visible and ready for you to draw content.
- [LayerRenderer.State](layerrenderer/state-swift.enum.md)
  The states of the layer renderer, which tell you how to proceed with drawing operations.
- [LayerRenderer.Clock](layerrenderer/clock.md)
  A type that supports operations that require a precise time measurement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/waituntilrunning())*