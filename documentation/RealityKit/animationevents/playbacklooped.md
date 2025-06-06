# AnimationEvents.PlaybackLooped

**Framework**: RealityKit  
**Kind**: struct

The event raised when an animation loops.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
struct PlaybackLooped
```

#### Overview

You loop animation playback by creating an [`AnimationResource`](animationresource.md) instance from an existing one with either the [`repeat(count:)`](animationresource/repeat(count:).md) or the [`repeat(duration:)`](animationresource/repeat(duration:).md) method.

## Topics

### Getting the controller
- [let playbackController: AnimationPlaybackController](animationevents/playbacklooped/playbackcontroller.md)
  The animation playback controller managing the animation that triggered the event.

## Relationships

### Conforms To
- [Event](event.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [AnimationEvents.PlaybackStarted](animationevents/playbackstarted.md)
  The event raised when an animation has been started.
- [AnimationEvents.PlaybackCompleted](animationevents/playbackcompleted.md)
  The event raised when an animation reaches the end of its duration.
- [AnimationEvents.PlaybackTerminated](animationevents/playbackterminated.md)
  The event raised when an animation has been terminated, regardless of whether it ran to completion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationevents/playbacklooped)*