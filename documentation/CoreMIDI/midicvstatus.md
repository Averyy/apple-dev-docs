# MIDICVStatus

**Framework**: Core MIDI  
**Kind**: enum

MIDI status types.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
enum MIDICVStatus
```

## Topics

### MIDI 1.0
- [MIDICVStatus.noteOff](midicvstatus/noteoff.md)
- [MIDICVStatus.noteOn](midicvstatus/noteon.md)
- [MIDICVStatus.polyPressure](midicvstatus/polypressure.md)
- [MIDICVStatus.controlChange](midicvstatus/controlchange.md)
- [MIDICVStatus.programChange](midicvstatus/programchange.md)
- [MIDICVStatus.channelPressure](midicvstatus/channelpressure.md)
- [MIDICVStatus.pitchBend](midicvstatus/pitchbend.md)
### MIDI 2.0
- [MIDICVStatus.registeredPNC](midicvstatus/registeredpnc.md)
- [MIDICVStatus.assignablePNC](midicvstatus/assignablepnc.md)
- [MIDICVStatus.registeredControl](midicvstatus/registeredcontrol.md)
- [MIDICVStatus.assignableControl](midicvstatus/assignablecontrol.md)
- [MIDICVStatus.relRegisteredControl](midicvstatus/relregisteredcontrol.md)
- [MIDICVStatus.relAssignableControl](midicvstatus/relassignablecontrol.md)
- [MIDICVStatus.perNotePitchBend](midicvstatus/pernotepitchbend.md)
- [MIDICVStatus.perNoteMgmt](midicvstatus/pernotemgmt.md)
### Initializers
- [init?(rawValue: UInt32)](midicvstatus/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [enum MIDIProtocolID](midiprotocolid.md)
  Specifies a MIDI protocol variant.
- [enum MIDISysExStatus](midisysexstatus.md)
  MIDI System Exclusive (SysEx) types.
- [enum MIDISystemStatus](midisystemstatus.md)
  MIDI System status types.
- [struct MIDIMessage_128](midimessage_128.md)
  A 128-bit MIDI message.
- [struct MIDIMessage_96](midimessage_96.md)
  A 96-bit MIDI message.
- [struct MIDIMessage_64](midimessage_64.md)
  A 64-bit MIDI message.
- [typealias MIDIMessage_32](midimessage_32.md)
  A 32-bit MIDI message.
- [enum MIDIMessageType](midimessagetype.md)
  Supported MIDI message types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midicvstatus)*