# resume()

**Framework**: RealityKit  
**Kind**: method

Resumes a paused animation.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency func resume()
```

#### Discussion

Call this method to resume an animation that you paused with the [`pause()`](animationplaybackcontroller/pause().md) method. You can’t resume an animation that has finished naturally, or that you stopped by calling the [`stop()`](animationplaybackcontroller/stop().md) method.

This method has no effect on an animation that isn’t paused.

## See Also

- [func pause()](animationplaybackcontroller/pause.md)
  Pauses the animation.
- [func stop()](animationplaybackcontroller/stop.md)
  Stops an animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationplaybackcontroller/resume())*