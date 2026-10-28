# AVMIDIMetaEvent

**Framework**: AVFAudio  
**Kind**: class  
**Role**: Class

An object that represents MIDI meta event messages.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
class AVMIDIMetaEvent
```

```objc
@interface AVMIDIMetaEvent : AVMusicEvent
```

## Overview

You can’t modify the size and contents of this event once you create it. This doesn’t verify that the content matches the MIDI specification.

You can only add [`AVMIDIMetaEvent.EventType.tempo`](./avmidimetaevent/eventtype/tempo.md), [`AVMIDIMetaEvent.EventType.smpteOffset`](./avmidimetaevent/eventtype/smpteoffset.md), or [`AVMIDIMetaEvent.EventType.timeSignature`](./avmidimetaevent/eventtype/timesignature.md) to a sequence’s tempo track.

## Topics

### Creating a meta event
- [init(type: AVMIDIMetaEvent.EventType, data: Data)](./avmidimetaevent/init%28type,data%29.md)
  Creates an event with a MIDI meta event type and data.
### Getting the meta event type
- [var type: AVMIDIMetaEvent.EventType](./avmidimetaevent/type.md)
  The type of meta event.
- [AVMIDIMetaEvent.EventType](./avmidimetaevent/eventtype.md)
  Constants that represent the types of meta events.

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

### Handling MIDI events
- [class AVMIDINoteEvent](./avmidinoteevent.md)
  An object that represents MIDI note on or off messages.
- [class AVMIDISysexEvent](./avmidisysexevent.md)
  An object that represents a MIDI system exclusive message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avmidimetaevent)*