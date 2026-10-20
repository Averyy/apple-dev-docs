# AVMIDIPitchBendEvent

**Framework**: AVFAudio  
**Kind**: class  
**Role**: Class

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

```objc
@interface AVMIDIPitchBendEvent : AVMIDIChannelEvent
```

## Topics

### Creating a pitch bend event
- [init(channel: UInt32, value: UInt32)](./avmidipitchbendevent/init%28channel,value%29.md)
  Creates an event with a channel and pitch bend value.
### Configuring a pitch bend event
- [var value: UInt32](./avmidipitchbendevent/value.md)
  The value of the pitch bend event.

## Relationships

### Inherits From
- [AVMIDIChannelEvent](./avmidichannelevent.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Handling MIDI channel events
- [class AVMIDIChannelEvent](./avmidichannelevent.md)
  A base class for all MIDI messages that operate on a single MIDI channel.
- [class AVMIDIChannelPressureEvent](./avmidichannelpressureevent.md)
  An object that represents a MIDI channel pressure message.
- [class AVMIDIProgramChangeEvent](./avmidiprogramchangeevent.md)
  An object that represents a MIDI program or patch change message.
- [class AVMIDIPolyPressureEvent](./avmidipolypressureevent.md)
  An object that represents a MIDI poly or key pressure event.
- [class AVMIDIControlChangeEvent](./avmidicontrolchangeevent.md)
  An object that represents a MIDI control change message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avmidipitchbendevent)*