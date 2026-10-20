# AVMIDIChannelEvent

**Framework**: AVFAudio  
**Kind**: class  
**Role**: Class

A base class for all MIDI messages that operate on a single MIDI channel.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
class AVMIDIChannelEvent
```

```objc
@interface AVMIDIChannelEvent : AVMusicEvent
```

## Topics

### Configuring a channel event
- [var channel: UInt32](./avmidichannelevent/channel.md)
  The MIDI channel.

## Relationships

### Inherits From
- [AVMusicEvent](./avmusicevent.md)
### Inherited By
- [AVMIDIChannelPressureEvent](./avmidichannelpressureevent.md)
- [AVMIDIControlChangeEvent](./avmidicontrolchangeevent.md)
- [AVMIDIPitchBendEvent](./avmidipitchbendevent.md)
- [AVMIDIPolyPressureEvent](./avmidipolypressureevent.md)
- [AVMIDIProgramChangeEvent](./avmidiprogramchangeevent.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Handling MIDI channel events
- [class AVMIDIChannelPressureEvent](./avmidichannelpressureevent.md)
  An object that represents a MIDI channel pressure message.
- [class AVMIDIProgramChangeEvent](./avmidiprogramchangeevent.md)
  An object that represents a MIDI program or patch change message.
- [class AVMIDIPolyPressureEvent](./avmidipolypressureevent.md)
  An object that represents a MIDI poly or key pressure event.
- [class AVMIDIPitchBendEvent](./avmidipitchbendevent.md)
  An object that represents a MIDI pitch bend message.
- [class AVMIDIControlChangeEvent](./avmidicontrolchangeevent.md)
  An object that represents a MIDI control change message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avmidichannelevent)*