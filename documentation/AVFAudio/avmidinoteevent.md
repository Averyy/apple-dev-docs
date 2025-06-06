# AVMIDINoteEvent

**Framework**: AVFAudio  
**Kind**: class

An object that represents MIDI note on or off messages.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
class AVMIDINoteEvent
```

## Topics

### Creating a MIDI Note Event
- [init(channel: UInt32, key: UInt32, velocity: UInt32, duration: AVMusicTimeStamp)](avmidinoteevent/init(channel:key:velocity:duration:).md)
  Creates an event with a MIDI channel, key number, velocity, and duration.
### Configuring a MIDI Note Event
- [var channel: UInt32](avmidinoteevent/channel.md)
  The MIDI channel.
- [var key: UInt32](avmidinoteevent/key.md)
  The MIDI key number.
- [var velocity: UInt32](avmidinoteevent/velocity.md)
  The MIDI velocity.
- [var duration: AVMusicTimeStamp](avmidinoteevent/duration.md)
  The duration for the note, in beats.

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

- [class AVMIDIMetaEvent](avmidimetaevent.md)
  An object that represents MIDI meta event messages.
- [class AVMIDISysexEvent](avmidisysexevent.md)
  An object that represents a MIDI system exclusive message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avmidinoteevent)*