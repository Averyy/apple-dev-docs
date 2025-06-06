# AVMIDIPitchBendEvent

**Framework**: AVFAudio  
**Kind**: class

An object that represents a MIDI pitch bend message.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
class AVMIDIPitchBendEvent
```

## Topics

### Creating a Pitch Bend Event
- [init(channel: UInt32, value: UInt32)](avmidipitchbendevent/init(channel:value:).md)
  Creates an event with a channel and pitch bend value.
### Configuring a Pitch Bend Event
- [var value: UInt32](avmidipitchbendevent/value.md)
  The value of the pitch bend event.

## Relationships

### Inherits From
- [AVMIDIChannelEvent](avmidichannelevent.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class AVMIDIChannelEvent](avmidichannelevent.md)
  A base class for all MIDI messages that operate on a single MIDI channel.
- [class AVMIDIChannelPressureEvent](avmidichannelpressureevent.md)
  An object that represents a MIDI channel pressure message.
- [class AVMIDIProgramChangeEvent](avmidiprogramchangeevent.md)
  An object that represents a MIDI program or patch change message.
- [class AVMIDIPolyPressureEvent](avmidipolypressureevent.md)
  An object that represents a MIDI poly or key pressure event.
- [class AVMIDIControlChangeEvent](avmidicontrolchangeevent.md)
  An object that represents a MIDI control change message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avmidipitchbendevent)*