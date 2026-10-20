# resume()

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Resumes a paused animation.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS

## Declaration

```swift
@MainActor
@preconcurrency func resume()
```

#### Discussion

Call this method to resume an animation that you paused with the [`pause()`](./pause%28%29.md) method. You can’t resume an animation that has finished naturally, or that you stopped by calling the [`stop()`](./stop%28%29.md) method.

This method has no effect on an animation that isn’t paused.

## See Also

### Inspecting and controlling playback
- [func pause()](./pause%28%29.md)
  Pauses the animation.
- [func stop()](./stop%28%29.md)
  Stops an animation.
- [var isPlaying: Bool](./isplaying.md)
  A Boolean value that indicates whether the animation plays.
- [var isStopped: Bool](./isstopped.md)
  A Boolean value that indicates whether the animation stopped.
- [var isValid: Bool](./isvalid.md)
  A Boolean value that indicates whether the animation controller is functional.
- [var blendFactor: Float](./blendfactor.md)
  The level of influence the controller gives to its animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationplaybackcontroller/resume())*