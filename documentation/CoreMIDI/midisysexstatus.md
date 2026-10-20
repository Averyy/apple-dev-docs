# MIDISysExStatus

**Framework**: Core MIDI  
**Kind**: enum  
**Role**: Enumeration

MIDI System Exclusive (SysEx) types.

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
enum MIDISysExStatus
```

```c
enum MIDISysExStatus : unsigned int;
```

## Topics

### Status Types
- [MIDISysExStatus.complete](./midisysexstatus/complete.md)
- [MIDISysExStatus.start](./midisysexstatus/start.md)
- [MIDISysExStatus.continue](./midisysexstatus/continue.md)
- [MIDISysExStatus.end](./midisysexstatus/end.md)
### Enumeration Cases
- [MIDISysExStatus.mixedDataSetHeader](./midisysexstatus/mixeddatasetheader.md)
- [MIDISysExStatus.mixedDataSetPayload](./midisysexstatus/mixeddatasetpayload.md)
### Initializers
- [init?(rawValue: UInt32)](./midisysexstatus/init%28rawvalue%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midisysexstatus)*