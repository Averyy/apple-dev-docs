# AVMIDIProgramChangeEvent

**Framework**: AVFAudio  
**Kind**: class  
**Role**: Class

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

```objc
@interface AVMIDIProgramChangeEvent : AVMIDIChannelEvent
```

## Overview

The effect of this message depends on the [`AVMusicTrack`](./avmusictrack.md) destination audio unit.

## Topics

### Creating a program change event
- [init(channel: UInt32, programNumber: UInt32)](./avmidiprogramchangeevent/init%28channel,programnumber%29.md)
  Creates a program change event with a channel and program number.
### Configuring a program change event
- [var programNumber: UInt32](./avmidiprogramchangeevent/programnumber.md)
  The MIDI program number.

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
- [class AVMIDIPolyPressureEvent](./avmidipolypressureevent.md)
  An object that represents a MIDI poly or key pressure event.
- [class AVMIDIPitchBendEvent](./avmidipitchbendevent.md)
  An object that represents a MIDI pitch bend message.
- [class AVMIDIControlChangeEvent](./avmidicontrolchangeevent.md)
  An object that represents a MIDI control change message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avmidiprogramchangeevent)*