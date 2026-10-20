# AVMIDISysexEvent

**Framework**: AVFAudio  
**Kind**: class  
**Role**: Class

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

```objc
@interface AVMIDISysexEvent : AVMusicEvent
```

#### Overview

You can’t modify the size and contents of this event once you create it.

## Topics

### Creating a system exclusive event
- [init(data: Data)](./avmidisysexevent/init%28data%29.md)
  Creates a system event with the data you specify.
### Getting the event size
- [var sizeInBytes: UInt32](./avmidisysexevent/sizeinbytes.md)
  The size of the data that this event contains.

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
- [class AVMIDIMetaEvent](./avmidimetaevent.md)
  An object that represents MIDI meta event messages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avmidisysexevent)*