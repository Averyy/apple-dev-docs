# pause()

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Pauses the animation.

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
@preconcurrency func pause()
```

## Discussion

Resume a paused animation by calling the [`resume()`](./resume%28%29.md) method.

This method has no effect if the animation is already paused or complete.

## See Also

### Inspecting and controlling playback
- [func resume()](./resume%28%29.md)
  Resumes a paused animation.
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

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationplaybackcontroller/pause())*