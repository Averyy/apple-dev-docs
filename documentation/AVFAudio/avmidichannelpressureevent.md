# AVMIDIChannelPressureEvent

**Framework**: AVFAudio  
**Kind**: class  
**Role**: Class

An object that represents a MIDI channel pressure message.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
class AVMIDIChannelPressureEvent
```

```objc
@interface AVMIDIChannelPressureEvent : AVMIDIChannelEvent
```

#### Overview

The effect of this message depends on the [`AVMusicTrack`](./avmusictrack.md) destination audio unit, and the capabilities of the destination’s loaded instrument.

## Topics

### Creating a pressure event
- [init(channel: UInt32, pressure: UInt32)](./avmidichannelpressureevent/init%28channel,pressure%29.md)
  Creates a pressure event with a channel and pressure value.
### Configuring a pressure event
- [var pressure: UInt32](./avmidichannelpressureevent/pressure.md)
  The MIDI channel pressure.

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
- [class AVMIDIProgramChangeEvent](./avmidiprogramchangeevent.md)
  An object that represents a MIDI program or patch change message.
- [class AVMIDIPolyPressureEvent](./avmidipolypressureevent.md)
  An object that represents a MIDI poly or key pressure event.
- [class AVMIDIPitchBendEvent](./avmidipitchbendevent.md)
  An object that represents a MIDI pitch bend message.
- [class AVMIDIControlChangeEvent](./avmidicontrolchangeevent.md)
  An object that represents a MIDI control change message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avmidichannelpressureevent)*