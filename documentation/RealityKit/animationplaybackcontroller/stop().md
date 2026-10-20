# stop()

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Stops an animation.

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
@preconcurrency func stop()
```

#### Discussion

This method has no effect if the animation is complete. After you stop the animation, the playback controller becomes invalid. Create a new one with the same resource to play the animation again.

## See Also

### Inspecting and controlling playback
- [func pause()](./pause%28%29.md)
  Pauses the animation.
- [func resume()](./resume%28%29.md)
  Resumes a paused animation.
- [var isPlaying: Bool](./isplaying.md)
  A Boolean value that indicates whether the animation plays.
- [var isStopped: Bool](./isstopped.md)
  A Boolean value that indicates whether the animation stopped.
- [var isValid: Bool](./isvalid.md)
  A Boolean value that indicates whether the animation controller is functional.
- [var blendFactor: Float](./blendfactor.md)
  The level of influence the controller gives to its animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationplaybackcontroller/stop())*