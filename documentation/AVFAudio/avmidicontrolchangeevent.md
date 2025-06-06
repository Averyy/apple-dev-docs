# AVMIDIControlChangeEvent

**Framework**: AVFAudio  
**Kind**: class

An object that represents a MIDI control change message.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
class AVMIDIControlChangeEvent
```

## Topics

### Creating a Control Change Event
- [init(channel: UInt32, messageType: AVMIDIControlChangeEvent.MessageType, value: UInt32)](avmidicontrolchangeevent/init(channel:messagetype:value:).md)
  Creates an event with a channel, control change type, and a value.
### Inspecting a Control Change Event
- [var value: UInt32](avmidicontrolchangeevent/value.md)
  The value of the control change event.
- [var messageType: AVMIDIControlChangeEvent.MessageType](avmidicontrolchangeevent/messagetype-swift.property.md)
  The type of control change message.
- [AVMIDIControlChangeEvent.MessageType](avmidicontrolchangeevent/messagetype-swift.enum.md)
  Constants that represents control change event types.

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
- [class AVMIDIPitchBendEvent](avmidipitchbendevent.md)
  An object that represents a MIDI pitch bend message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avmidicontrolchangeevent)*