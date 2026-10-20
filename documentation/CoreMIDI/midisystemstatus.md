# MIDISystemStatus

**Framework**: Core MIDI  
**Kind**: enum  
**Role**: Enumeration

MIDI System status types.

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
enum MIDISystemStatus
```

```c
enum MIDISystemStatus : unsigned int;
```

## Topics

### Status Types
- [MIDISystemStatus.statusActiveSending](./midisystemstatus/statusactivesending.md)
- [MIDISystemStatus.statusContinue](./midisystemstatus/statuscontinue.md)
- [MIDISystemStatus.statusEndOfExclusive](./midisystemstatus/statusendofexclusive.md)
- [MIDISystemStatus.statusMTC](./midisystemstatus/statusmtc.md)
- [MIDISystemStatus.statusSongPosPointer](./midisystemstatus/statussongpospointer.md)
- [MIDISystemStatus.statusSongSelect](./midisystemstatus/statussongselect.md)
- [MIDISystemStatus.statusStart](./midisystemstatus/statusstart.md)
- [MIDISystemStatus.statusStartOfExclusive](./midisystemstatus/statusstartofexclusive.md)
- [MIDISystemStatus.statusStop](./midisystemstatus/statusstop.md)
- [MIDISystemStatus.statusSystemReset](./midisystemstatus/statussystemreset.md)
- [MIDISystemStatus.statusTimingClock](./midisystemstatus/statustimingclock.md)
- [MIDISystemStatus.statusTuneRequest](./midisystemstatus/statustunerequest.md)
### Initializers
- [init?(rawValue: UInt32)](./midisystemstatus/init%28rawvalue%29.md)
### Type Properties
- [static var statusActiveSensing: MIDISystemStatus](./midisystemstatus/statusactivesensing.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midisystemstatus)*