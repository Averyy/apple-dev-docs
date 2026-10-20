# blendFactor

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

The level of influence the controller gives to its animation.

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
@preconcurrency var blendFactor: Float { get set }
```

#### Discussion

You can run multiple animations on the same property, for example, walking and jumping animations that affect the same joint transforms. When multiple animations adjust the same property at runtime, the framework applies this blend factor on the animations’ respective controllers to calculate a middle ground value that displays at runtime.

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
- [var isValid: Bool](./isvalid.md)
  A Boolean value that indicates whether the animation controller is functional.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationplaybackcontroller/blendfactor)*