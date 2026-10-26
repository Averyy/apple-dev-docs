# MIDIProtocolID

**Framework**: Core MIDI  
**Kind**: enum  
**Role**: Enumeration

Specifies a MIDI protocol variant.

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
enum MIDIProtocolID
```

```c
enum MIDIProtocolID : SInt32;
```

## Topics

### Initializers
- [init?(rawValue: Int32)](./midiprotocolid/init%28rawvalue%29.md)
### Protocol Versions
- [kMIDIProtocol_1_0](./midiprotocolid/kmidiprotocol_1_0.md)
- [kMIDIProtocol_2_0](./midiprotocolid/kmidiprotocol_2_0.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Common
- [enum MIDICVStatus](./midicvstatus.md)
  MIDI status types.
- [enum MIDISysExStatus](./midisysexstatus.md)
  MIDI System Exclusive (SysEx) types.
- [enum MIDISystemStatus](./midisystemstatus.md)
  MIDI System status types.
- [struct MIDIMessage_128](./midimessage_128.md)
  A 128-bit MIDI message.
- [struct MIDIMessage_96](./midimessage_96.md)
  A 96-bit MIDI message.
- [struct MIDIMessage_64](./midimessage_64.md)
  A 64-bit MIDI message.
- [typealias MIDIMessage_32](./midimessage_32.md)
  A 32-bit MIDI message.
- [enum MIDIMessageType](./midimessagetype.md)
  Supported MIDI message types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midiprotocolid)*