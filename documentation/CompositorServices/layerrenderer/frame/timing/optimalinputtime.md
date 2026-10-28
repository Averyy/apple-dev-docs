# optimalInputTime

**Framework**: Compositor Services  
**Kind**: property  
**Role**: Instance Property

The optimal time to start the frame submission process.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```swift
var optimalInputTime: LayerRenderer.Clock.Instant { get }
```

## Discussion

The optimal input time is the time at which to call the [`startSubmission()`](../startsubmission%28%29.md) function and begin encoding your Metal command buffers. Use the time before the input time to update your app’s data structures and prepare for rendering. Call [`wait(until:tolerance:)`](../../clock/wait%28until,tolerance%29.md) to suspend your app until the optimal time arrives. When it does, fetch the current device pose and finish rendering and the frame and commit your Metal command buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/frame/timing/optimalinputtime)*