# presentationTime

**Framework**: Compositor Services  
**Kind**: property

The time at which the system displays the frame onscreen.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```swift
var presentationTime: LayerRenderer.Clock.Instant { get }
```

#### Discussion

You can use the presentation time as a synchronization point for other parts of your app. For example, if you play an audio clip when the frame appears, configure your code to start playing the clip at the specified time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/frame/timing/presentationtime)*