# AVMIDISysexEvent

**Framework**: AVFAudio  
**Kind**: class

An object that represents a MIDI system exclusive message.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
class AVMIDISysexEvent
```

#### Overview

You can’t modify the size and contents of this event once you create it.

## Topics

### Creates a System Event
- [init(data: Data)](avmidisysexevent/init(data:).md)
  Creates a system event with the data you specify.
### Getting the Size of the Event
- [var sizeInBytes: UInt32](avmidisysexevent/sizeinbytes.md)
  The size of the data that this event contains.

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
- [class AVMIDIMetaEvent](avmidimetaevent.md)
  An object that represents MIDI meta event messages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avmidisysexevent)*