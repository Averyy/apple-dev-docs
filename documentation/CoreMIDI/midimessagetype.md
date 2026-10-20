# MIDIMessageType

**Framework**: Core MIDI  
**Kind**: enum  
**Role**: Enumeration

Supported MIDI message types.

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
enum MIDIMessageType
```

```c
enum MIDIMessageType : unsigned int;
```

## Topics

### Message Types
- [MIDIMessageType.channelVoice1](./midimessagetype/channelvoice1.md)
- [MIDIMessageType.channelVoice2](./midimessagetype/channelvoice2.md)
- [MIDIMessageType.data128](./midimessagetype/data128.md)
- [MIDIMessageType.sysEx](./midimessagetype/sysex.md)
- [MIDIMessageType.system](./midimessagetype/system.md)
- [MIDIMessageType.utility](./midimessagetype/utility.md)
### Enumeration Cases
- [MIDIMessageType.flexData](./midimessagetype/flexdata.md)
- [MIDIMessageType.invalid](./midimessagetype/invalid.md)
- [MIDIMessageType.unknownF](./midimessagetype/unknownf.md)
### Initializers
- [init?(rawValue: UInt32)](./midimessagetype/init%28rawvalue%29.md)
### Type Properties
- [static var stream: MIDIMessageType](./midimessagetype/stream.md)

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
- [enum MIDIProtocolID](./midiprotocolid.md)
  Specifies a MIDI protocol variant.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midimessagetype)*