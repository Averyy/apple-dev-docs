# UIEvent.EventSubtype

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Constants that specify the subtype of the event in relation to its general type.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
enum EventSubtype
```

```c
enum UIEventSubtype : NSInteger;
```

## Overview

You can obtain the subtype of an event from the [`subtype`](./subtype.md) property.

## Topics

### Constants
- [UIEvent.EventSubtype.none](./eventsubtype/none.md)
  The event has no subtype.
- [UIEvent.EventSubtype.motionShake](./eventsubtype/motionshake.md)
  The event is related to a person shaking the device.
- [UIEvent.EventSubtype.remoteControlPlay](./eventsubtype/remotecontrolplay.md)
  A remote-control event for playing audio or video.
- [UIEvent.EventSubtype.remoteControlPause](./eventsubtype/remotecontrolpause.md)
  A remote-control event for pausing audio or video.
- [UIEvent.EventSubtype.remoteControlStop](./eventsubtype/remotecontrolstop.md)
  A remote-control event for stopping audio or video from playing.
- [UIEvent.EventSubtype.remoteControlTogglePlayPause](./eventsubtype/remotecontroltoggleplaypause.md)
  A remote-control event for toggling audio or video between play and pause.
- [UIEvent.EventSubtype.remoteControlNextTrack](./eventsubtype/remotecontrolnexttrack.md)
  A remote-control event for skipping to the next audio or video track.
- [UIEvent.EventSubtype.remoteControlPreviousTrack](./eventsubtype/remotecontrolprevioustrack.md)
  A remote-control event for skipping to the previous audio or video track.
- [UIEvent.EventSubtype.remoteControlBeginSeekingBackward](./eventsubtype/remotecontrolbeginseekingbackward.md)
  A remote-control event to start seeking backward through the audio or video medium.
- [UIEvent.EventSubtype.remoteControlEndSeekingBackward](./eventsubtype/remotecontrolendseekingbackward.md)
  A remote-control event to end seeking backward through the audio or video medium.
- [UIEvent.EventSubtype.remoteControlBeginSeekingForward](./eventsubtype/remotecontrolbeginseekingforward.md)
  A remote-control event to start seeking forward through the audio or video medium.
- [UIEvent.EventSubtype.remoteControlEndSeekingForward](./eventsubtype/remotecontrolendseekingforward.md)
  A remote-control event to end seeking forward through the audio or video medium.
### Initializers
- [init?(rawValue: Int)](./eventsubtype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting the event type
- [var type: UIEvent.EventType](./type.md)
  Returns the type of the event.
- [UIEvent.EventType](./eventtype.md)
  Constants that specify the general type of an event.
- [var subtype: UIEvent.EventSubtype](./subtype.md)
  Returns the subtype of the event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uievent/eventsubtype)*