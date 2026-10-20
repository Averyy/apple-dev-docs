# MIDIMessage_96

**Framework**: Core MIDI  
**Kind**: struct  
**Role**: Structure

A 96-bit MIDI message.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
struct MIDIMessage_96
```

```c
typedef struct MIDIMessage_96 { ... } MIDIMessage_96;
```

## Topics

### Words
- [var word0: UInt32](./midimessage_96/word0.md)
- [var word1: UInt32](./midimessage_96/word1.md)
- [var word2: UInt32](./midimessage_96/word2.md)
### Initializers
- [init()](./midimessage_96/init%28%29.md)
- [init(word0: UInt32, word1: UInt32, word2: UInt32)](./midimessage_96/init%28word0,word1,word2%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Common
- [enum MIDICVStatus](./midicvstatus.md)
  MIDI status types.
- [enum MIDIProtocolID](./midiprotocolid.md)
  Specifies a MIDI protocol variant.
- [enum MIDISysExStatus](./midisysexstatus.md)
  MIDI System Exclusive (SysEx) types.
- [enum MIDISystemStatus](./midisystemstatus.md)
  MIDI System status types.
- [struct MIDIMessage_128](./midimessage_128.md)
  A 128-bit MIDI message.
- [struct MIDIMessage_64](./midimessage_64.md)
  A 64-bit MIDI message.
- [typealias MIDIMessage_32](./midimessage_32.md)
  A 32-bit MIDI message.
- [enum MIDIMessageType](./midimessagetype.md)
  Supported MIDI message types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midimessage_96)*