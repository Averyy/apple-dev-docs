# AVMusicUserEvent

**Framework**: AVFAudio  
**Kind**: class

An object that represents a custom user message.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
class AVMusicUserEvent
```

#### Overview

When playback of an [`AVMusicTrack`](avmusictrack.md) reaches this event, the system calls the track’s callback. You can’t modify the size and contents of an [`AVMusicUserEvent`](avmusicuserevent.md) once you create it.

## Topics

### Creating a User Event
- [init(data: Data)](avmusicuserevent/init(data:).md)
  Creates a user event with the data you specify.
### Inspecting a User Event
- [var sizeInBytes: UInt32](avmusicuserevent/sizeinbytes.md)
  The size of the data that the user event represents.

## Relationships

### Inherits From
- [AVMusicEvent](avmusicevent.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class AVMusicEvent](avmusicevent.md)
  A base class for the events you associate with a music track.
- [class AVParameterEvent](avparameterevent.md)
  An object that represents a parameter event on a music track’s destination.
- [class AVAUPresetEvent](avaupresetevent.md)
  An object that represents a preset load and change on the music track’s destination audio unit.
- [class AVExtendedTempoEvent](avextendedtempoevent.md)
  An object that represents a tempo change to a specific beats-per-minute value.
- [class AVExtendedNoteOnEvent](avextendednoteonevent.md)
  An object that represents a custom extension of a MIDI note on event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avmusicuserevent)*