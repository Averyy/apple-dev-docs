# AnimationEvents.PlaybackTerminated

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

The event raised when an animation has been terminated, regardless of whether it ran to completion.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS

## Declaration

```swift
struct PlaybackTerminated
```

## Topics

### Instance Properties
- [let playbackController: AnimationPlaybackController](./playbackterminated/playbackcontroller.md)
  The animation playback controller managing the animation that triggered the event.

## Relationships

### Conforms To
- [Event](../event.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Recognizing animation events
- [AnimationEvents.PlaybackStarted](./playbackstarted.md)
  The event raised when an animation has been started.
- [AnimationEvents.PlaybackCompleted](./playbackcompleted.md)
  The event raised when an animation reaches the end of its duration.
- [AnimationEvents.PlaybackLooped](./playbacklooped.md)
  The event raised when an animation loops.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationevents/playbackterminated)*