# AVMIDIProgramChangeEvent

**Framework**: AVFAudio  
**Kind**: class

An object that represents a MIDI program or patch change message.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
class AVMIDIProgramChangeEvent
```

#### Overview

The effect of this message depends on the [`AVMusicTrack`](avmusictrack.md) destination audio unit.

## Topics

### Creating a Program Change Event
- [init(channel: UInt32, programNumber: UInt32)](avmidiprogramchangeevent/init(channel:programnumber:).md)
  Creates a program change event with a channel and program number.
### Configuring a Program Change Event
- [var programNumber: UInt32](avmidiprogramchangeevent/programnumber.md)
  The MIDI program number.

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
- [class AVMIDIPolyPressureEvent](avmidipolypressureevent.md)
  An object that represents a MIDI poly or key pressure event.
- [class AVMIDIPitchBendEvent](avmidipitchbendevent.md)
  An object that represents a MIDI pitch bend message.
- [class AVMIDIControlChangeEvent](avmidicontrolchangeevent.md)
  An object that represents a MIDI control change message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avmidiprogramchangeevent)*