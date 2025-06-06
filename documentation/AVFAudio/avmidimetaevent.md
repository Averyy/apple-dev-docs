# AVMIDIMetaEvent

**Framework**: AVFAudio  
**Kind**: class

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

#### Overview

You can’t modify the size and contents of this event once you create it. This doesn’t verify that the content matches the MIDI specification.

You can only add [`AVMIDIMetaEvent.EventType.tempo`](avmidimetaevent/eventtype/tempo.md), [`AVMIDIMetaEvent.EventType.smpteOffset`](avmidimetaevent/eventtype/smpteoffset.md), or [`AVMIDIMetaEvent.EventType.timeSignature`](avmidimetaevent/eventtype/timesignature.md) to a sequence’s tempo track.

## Topics

### Creating a Meta Event
- [init(type: AVMIDIMetaEvent.EventType, data: Data)](avmidimetaevent/init(type:data:).md)
  Creates an event with a MIDI meta event type and data.
### Getting the Meta Event Type
- [var type: AVMIDIMetaEvent.EventType](avmidimetaevent/type.md)
  The type of meta event.
- [AVMIDIMetaEvent.EventType](avmidimetaevent/eventtype.md)
  Constants that represent the types of meta events.

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

- [class AVMIDINoteEvent](avmidinoteevent.md)
  An object that represents MIDI note on or off messages.
- [class AVMIDISysexEvent](avmidisysexevent.md)
  An object that represents a MIDI system exclusive message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avmidimetaevent)*