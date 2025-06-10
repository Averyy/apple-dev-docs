# pause()

**Framework**: RealityKit  
**Kind**: method

Pauses the animation.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationplaybackcontroller/pause())*