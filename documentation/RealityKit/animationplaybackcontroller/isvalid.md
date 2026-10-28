# isValid

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the animation controller is functional.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS

## Declaration

```swift
@MainActor
@preconcurrency var isValid: Bool { get }
```

## Discussion

This function returns `false` for stopped animations.

## See Also

### Inspecting and controlling playback
- [func pause()](./pause%28%29.md)
  Pauses the animation.
- [func resume()](./resume%28%29.md)
  Resumes a paused animation.
- [func stop()](./stop%28%29.md)
  Stops an animation.
- [var isPlaying: Bool](./isplaying.md)
  A Boolean value that indicates whether the animation plays.
- [var isStopped: Bool](./isstopped.md)
  A Boolean value that indicates whether the animation stopped.
- [var blendFactor: Float](./blendfactor.md)
  The level of influence the controller gives to its animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationplaybackcontroller/isvalid)*