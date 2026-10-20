# AVMIDIPolyPressureEvent

**Framework**: AVFAudio  
**Kind**: class  
**Role**: Class

An object that represents a MIDI poly or key pressure event.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
class AVMIDIPolyPressureEvent
```

```objc
@interface AVMIDIPolyPressureEvent : AVMIDIChannelEvent
```

## Topics

### Creating a poly pressure event
- [init(channel: UInt32, key: UInt32, pressure: UInt32)](./avmidipolypressureevent/init%28channel,key,pressure%29.md)
  Creates an event with a channel, MIDI key number, and a key pressure value.
### Configuring a poly pressure event
- [var key: UInt32](./avmidipolypressureevent/key.md)
  The MIDI key number.
- [var pressure: UInt32](./avmidipolypressureevent/pressure.md)
  The poly pressure value for the requested key.

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
- [class AVMIDIPitchBendEvent](./avmidipitchbendevent.md)
  An object that represents a MIDI pitch bend message.
- [class AVMIDIControlChangeEvent](./avmidicontrolchangeevent.md)
  An object that represents a MIDI control change message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avmidipolypressureevent)*