# AVExtendedTempoEvent

**Framework**: AVFAudio  
**Kind**: class  
**Role**: Class

An object that represents a tempo change to a specific beats-per-minute value.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
class AVExtendedTempoEvent
```

```objc
@interface AVExtendedTempoEvent : AVMusicEvent
```

## Topics

### Creating a tempo event
- [init(tempo: Double)](./avextendedtempoevent/init%28tempo%29.md)
  Creates an extended tempo event.
### Configuring a tempo event
- [var tempo: Double](./avextendedtempoevent/tempo.md)
  The tempo in beats per minute as a positive value.

## Relationships

### Inherits From
- [AVMusicEvent](./avmusicevent.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Handling music events
- [class AVMusicEvent](./avmusicevent.md)
  A base class for the events you associate with a music track.
- [class AVMusicUserEvent](./avmusicuserevent.md)
  An object that represents a custom user message.
- [class AVParameterEvent](./avparameterevent.md)
  An object that represents a parameter event on a music track’s destination.
- [class AVAUPresetEvent](./avaupresetevent.md)
  An object that represents a preset load and change on the music track’s destination audio unit.
- [class AVExtendedNoteOnEvent](./avextendednoteonevent.md)
  An object that represents a custom extension of a MIDI note on event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avextendedtempoevent)*