# isStopped

**Framework**: RealityKit  
**Kind**: property

A Boolean value that indicates whether the animation stopped.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency var isStopped: Bool { get }
```

#### Discussion

This function returns `true` for stopped animations.

## See Also

- [func pause()](animationplaybackcontroller/pause.md)
  Pauses the animation.
- [func resume()](animationplaybackcontroller/resume.md)
  Resumes a paused animation.
- [func stop()](animationplaybackcontroller/stop.md)
  Stops an animation.
- [var isPlaying: Bool](animationplaybackcontroller/isplaying.md)
  A Boolean value that indicates whether the animation plays.
- [var isValid: Bool](animationplaybackcontroller/isvalid.md)
  A Boolean value that indicates whether the animation controller is functional.
- [var blendFactor: Float](animationplaybackcontroller/blendfactor.md)
  The level of influence the controller gives to its animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationplaybackcontroller/isstopped)*