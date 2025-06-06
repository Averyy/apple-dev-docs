# AnimationEvents.PlaybackCompleted

**Framework**: RealityKit  
**Kind**: struct

The event raised when an animation reaches the end of its duration.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
struct PlaybackCompleted
```

#### Overview

This event isn’t triggered if you call the [`stop()`](animationplaybackcontroller/stop().md) method on a playback controller.

## Topics

### Getting the controller
- [let playbackController: AnimationPlaybackController](animationevents/playbackcompleted/playbackcontroller.md)
  The animation playback controller managing the animation that triggered the event.

## Relationships

### Conforms To
- [Event](event.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [AnimationEvents.PlaybackStarted](animationevents/playbackstarted.md)
  The event raised when an animation has been started.
- [AnimationEvents.PlaybackLooped](animationevents/playbacklooped.md)
  The event raised when an animation loops.
- [AnimationEvents.PlaybackTerminated](animationevents/playbackterminated.md)
  The event raised when an animation has been terminated, regardless of whether it ran to completion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationevents/playbackcompleted)*