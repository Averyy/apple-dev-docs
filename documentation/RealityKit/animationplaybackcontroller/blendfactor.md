# blendFactor

**Framework**: RealityKit  
**Kind**: property

The level of influence the controller gives to its animation.

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
@preconcurrency var blendFactor: Float { get set }
```

#### Discussion

You can run multiple animations on the same property, for example, walking and jumping animations that affect the same joint transforms. When multiple animations adjust the same property at runtime, the framework applies this blend factor on the animations’ respective controllers to calculate a middle ground value that displays at runtime.

## See Also

- [func pause()](animationplaybackcontroller/pause.md)
  Pauses the animation.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationplaybackcontroller/blendfactor)*