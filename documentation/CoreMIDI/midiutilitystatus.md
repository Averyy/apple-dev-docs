# MIDIUtilityStatus

**Framework**: Core MIDI  
**Kind**: enum  
**Role**: Enumeration

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
enum MIDIUtilityStatus
```

```c
enum MIDIUtilityStatus : unsigned int;
```

## Topics

### Enumeration Cases
- [MIDIUtilityStatus.NOOP](./midiutilitystatus/noop.md)
- [MIDIUtilityStatus.deltaClockstampTicksPerQuarterNote](./midiutilitystatus/deltaclockstampticksperquarternote.md)
- [MIDIUtilityStatus.jitterReductionClock](./midiutilitystatus/jitterreductionclock.md)
- [MIDIUtilityStatus.jitterReductionTimestamp](./midiutilitystatus/jitterreductiontimestamp.md)
- [MIDIUtilityStatus.ticksSinceLastEvent](./midiutilitystatus/tickssincelastevent.md)
### Initializers
- [init?(rawValue: UInt32)](./midiutilitystatus/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Enumerations
- [var kMIDIInvalidUniqueID: MIDIUniqueID](./kmidiinvaliduniqueid.md)
  An invalid identifier.
- [struct MIDICICategoryOptions](./midicicategoryoptions.md)
- [enum MIDICIDeviceType](./midicidevicetype.md)
- [enum MIDICIManagementMessageType](./midicimanagementmessagetype.md)
- [enum MIDICIProcessInquiryMessageType](./midiciprocessinquirymessagetype.md)
- [enum MIDICIProfileMessageType](./midiciprofilemessagetype.md)
- [enum MIDICIProfileType](./midiciprofiletype.md)
- [enum MIDICIPropertyExchangeMessageType](./midicipropertyexchangemessagetype.md)
- [enum MIDINetworkConnectionPolicy](./midinetworkconnectionpolicy.md)
- [enum MIDINoteAttribute](./midinoteattribute.md)
- [struct MIDIPerNoteManagementOptions](./midipernotemanagementoptions.md)
- [struct MIDIProgramChangeOptions](./midiprogramchangeoptions.md)
- [enum MIDIUMPCIObjectBackingType](./midiumpciobjectbackingtype.md)
- [enum MIDIUMPFunctionBlockDirection](./midiumpfunctionblockdirection.md)
- [enum MIDIUMPFunctionBlockMIDI1Info](./midiumpfunctionblockmidi1info.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midiutilitystatus)*