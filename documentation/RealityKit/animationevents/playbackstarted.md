# AnimationEvents.PlaybackStarted

**Framework**: RealityKit  
**Kind**: struct

The event raised when an animation has been started.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 1.0+

## Declaration

```swift
struct PlaybackStarted
```

## Topics

### Instance Properties
- [let playbackController: AnimationPlaybackController](animationevents/playbackstarted/playbackcontroller.md)
  The animation playback controller managing the animation that triggered the event.

## Relationships

### Conforms To
- [Event](event.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [AnimationEvents.PlaybackCompleted](animationevents/playbackcompleted.md)
  The event raised when an animation reaches the end of its duration.
- [AnimationEvents.PlaybackLooped](animationevents/playbacklooped.md)
  The event raised when an animation loops.
- [AnimationEvents.PlaybackTerminated](animationevents/playbackterminated.md)
  The event raised when an animation has been terminated, regardless of whether it ran to completion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationevents/playbackstarted)*