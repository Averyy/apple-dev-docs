# UIEvent.EventSubtype

**Framework**: UIKit  
**Kind**: enum

Constants that specify the subtype of the event in relation to its general type.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
enum EventSubtype
```

#### Overview

You can obtain the subtype of an event from the [`subtype`](uievent/subtype.md) property.

## Topics

### Constants
- [UIEvent.EventSubtype.none](uievent/eventsubtype/none.md)
  The event has no subtype.
- [UIEvent.EventSubtype.motionShake](uievent/eventsubtype/motionshake.md)
  The event is related to a person shaking the device.
- [UIEvent.EventSubtype.remoteControlPlay](uievent/eventsubtype/remotecontrolplay.md)
  A remote-control event for playing audio or video.
- [UIEvent.EventSubtype.remoteControlPause](uievent/eventsubtype/remotecontrolpause.md)
  A remote-control event for pausing audio or video.
- [UIEvent.EventSubtype.remoteControlStop](uievent/eventsubtype/remotecontrolstop.md)
  A remote-control event for stopping audio or video from playing.
- [UIEvent.EventSubtype.remoteControlTogglePlayPause](uievent/eventsubtype/remotecontroltoggleplaypause.md)
  A remote-control event for toggling audio or video between play and pause.
- [UIEvent.EventSubtype.remoteControlNextTrack](uievent/eventsubtype/remotecontrolnexttrack.md)
  A remote-control event for skipping to the next audio or video track.
- [UIEvent.EventSubtype.remoteControlPreviousTrack](uievent/eventsubtype/remotecontrolprevioustrack.md)
  A remote-control event for skipping to the previous audio or video track.
- [UIEvent.EventSubtype.remoteControlBeginSeekingBackward](uievent/eventsubtype/remotecontrolbeginseekingbackward.md)
  A remote-control event to start seeking backward through the audio or video medium.
- [UIEvent.EventSubtype.remoteControlEndSeekingBackward](uievent/eventsubtype/remotecontrolendseekingbackward.md)
  A remote-control event to end seeking backward through the audio or video medium.
- [UIEvent.EventSubtype.remoteControlBeginSeekingForward](uievent/eventsubtype/remotecontrolbeginseekingforward.md)
  A remote-control event to start seeking forward through the audio or video medium.
- [UIEvent.EventSubtype.remoteControlEndSeekingForward](uievent/eventsubtype/remotecontrolendseekingforward.md)
  A remote-control event to end seeking forward through the audio or video medium.
### Initializers
- [init?(rawValue: Int)](uievent/eventsubtype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var type: UIEvent.EventType](uievent/type.md)
  Returns the type of the event.
- [UIEvent.EventType](uievent/eventtype.md)
  Constants that specify the general type of an event.
- [var subtype: UIEvent.EventSubtype](uievent/subtype.md)
  Returns the subtype of the event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uievent/eventsubtype)*