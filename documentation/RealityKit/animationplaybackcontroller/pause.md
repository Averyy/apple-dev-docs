# pause()

**Framework**: RealityKit  
**Kind**: method

Pauses the animation.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency func pause()
```

#### Discussion

Resume a paused animation by calling the [`resume()`](animationplaybackcontroller/resume().md) method.

This method has no effect if the animation is already paused or complete.

## See Also

- [func resume()](animationplaybackcontroller/resume.md)
  Resumes a paused animation.
- [func stop()](animationplaybackcontroller/stop.md)
  Stops an animation.
- [var isPlaying: Bool](animationplaybackcontroller/isplaying.md)
  A Boolean value that indicates whether the animation plays.
- [var isStopped: Bool](animationplaybackcontroller/isstopped.md)
  A Boolean value that indicates whether the animation stopped.
- [var isValid: Bool](animationplaybackcontroller/isvalid.md)
  A Boolean value that indicates whether the animation controller is functional.
- [var blendFactor: Float](animationplaybackcontroller/blendfactor.md)
  The level of influence the controller gives to its animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationplaybackcontroller/pause())*