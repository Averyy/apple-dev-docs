# startUpdate()

**Framework**: Compositor Services  
**Kind**: method

Notifies Compositor Services that you started updating the app-specific content for the frame.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```swift
func startUpdate()
```

## Mentions

- [Drawing fully immersive content using Metal](drawing-fully-immersive-content-using-metal.md)

#### Discussion

This function helps you optimize your app’s rendering efficiency. Before you render a frame, you might need to respond to interactions with your content and update your app’s data structures before you render items in your scene. Call this function immediately before you start that work, and call [`endUpdate()`](layerrenderer/frame/endupdate().md)  as soon as you finish. Compositor Services uses the time difference to improve its predictions for when to start the frame encoding process.

Move as much work as possible into the update phase to minimize encoding time. Don’t do any work that relies on the current pose information during the update phase. Instead, make any pose-related changes during the submission phase.

## See Also

- [func endUpdate()](layerrenderer/frame/endupdate.md)
  Notifies Compositor Services that you finished updating the app-specific content you need to render the frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/frame/startupdate())*