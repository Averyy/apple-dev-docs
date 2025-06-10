# endUpdate()

**Framework**: Compositor Services  
**Kind**: method

Notifies Compositor Services that you finished updating the app-specific content you need to render the frame.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 1.0+

## Declaration

```swift
func endUpdate()
```

## Mentions

- [Drawing fully immersive content using Metal](drawing-fully-immersive-content-using-metal.md)

#### Discussion

This function helps you optimize your app’s rendering efficiency. Before you render a frame, you might need to respond to interactions and update your app’s data structures before you render items in your scene. Call [`startUpdate()`](layerrenderer/frame/startupdate().md) immediately before you start that work, and call this function as soon as you finish. Compositor Services uses the frame update time to improve its predictions for when to start the frame encoding process.

Move as much work as possible into the update phase to minimize encoding time. Don’t do any work that relies on the current pose information during the update phase. Instead, make any pose-related changes during the submission phase.

## See Also

- [func startUpdate()](layerrenderer/frame/startupdate.md)
  Notifies Compositor Services that you started updating the app-specific content for the frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/frame/endupdate())*