# isComplete

**Framework**: RealityKit  
**Kind**: property

A Boolean that indicates whether the animation has finished running.

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
@preconcurrency var isComplete: Bool { get }
```

#### Discussion

After an animation completes, the playback controller becomes invalid. To play the animation again, create a new controller with the same resource.

## See Also

- [var isPaused: Bool](animationplaybackcontroller/ispaused.md)
  A Boolean that indicates whether the animation is paused.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationplaybackcontroller/iscomplete)*