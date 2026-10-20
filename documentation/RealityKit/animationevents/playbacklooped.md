# AnimationEvents.PlaybackLooped

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

The event raised when an animation loops.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS

## Declaration

```swift
struct PlaybackLooped
```

#### Overview

You loop animation playback by creating an [`AnimationResource`](../animationresource.md) instance from an existing one with either the [`repeat(count:)`](../animationresource/repeat%28count%29.md) or the [`repeat(duration:)`](../animationresource/repeat%28duration%29.md) method.

## Topics

### Instance Properties
- [let playbackController: AnimationPlaybackController](./playbacklooped/playbackcontroller.md)
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
- [AnimationEvents.PlaybackTerminated](./playbackterminated.md)
  The event raised when an animation has been terminated, regardless of whether it ran to completion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationevents/playbacklooped)*