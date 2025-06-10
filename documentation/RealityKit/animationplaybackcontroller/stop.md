# stop()

**Framework**: RealityKit  
**Kind**: method

Stops an animation.

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
@preconcurrency func stop()
```

#### Discussion

This method has no effect if the animation is complete. After you stop the animation, the playback controller becomes invalid. Create a new one with the same resource to play the animation again.

## See Also

- [func pause()](animationplaybackcontroller/pause.md)
  Pauses the animation.
- [func resume()](animationplaybackcontroller/resume.md)
  Resumes a paused animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationplaybackcontroller/stop())*