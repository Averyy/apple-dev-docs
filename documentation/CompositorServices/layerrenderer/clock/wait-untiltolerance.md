# wait(until:tolerance:)

**Framework**: Compositor Services  
**Kind**: method

Blocks the current thread until the specified time.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
func wait(until deadline: LayerRenderer.Clock.Instant, tolerance: Duration? = nil)
```

## Mentions

- [Drawing fully immersive content using Metal](drawing-fully-immersive-content-using-metal.md)

#### Discussion

Use this function to block your render loop while waiting for critical time events. For example, use it to block the thread prior to starting the submission phase for a given frame.

## Parameters

- `deadline`: The Mach absolute time at which to wake up the thread. Typically, you supply one of the predicted times associated with the current frame, such as the optimal input time.
- `tolerance`: The amount of time before or after the deadline to allow the system to wake up the thread. Specifying a non-zero value lets the system shift the actual deadline to coalesce other work and achieve greater power savings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/clock/wait(until:tolerance:))*