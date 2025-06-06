# Core MIDI Functions

**Framework**: Core MIDI

## Topics

### Functions
- [func MIDI1UPChannelPressure(UInt8, UInt8, UInt8) -> MIDIMessage_32](midi1upchannelpressure(_:_:_:).md)
- [func MIDI1UPPolyPressure(UInt8, UInt8, UInt8, UInt8) -> MIDIMessage_32](midi1uppolypressure(_:_:_:_:).md)
- [func MIDI1UPProgramChange(UInt8, UInt8, UInt8) -> MIDIMessage_32](midi1upprogramchange(_:_:_:).md)
- [func MIDI1UPSysEx(UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8) -> MIDIMessage_64](midi1upsysex(_:_:_:_:_:_:_:_:_:).md)
- [func MIDI1UPSysExArray(UInt8, UInt8, UnsafePointer<UInt8>!, UnsafePointer<UInt8>!) -> MIDIMessage_64](midi1upsysexarray(_:_:_:_:).md)
- [func MIDI2EndOfClipMessage() -> MIDIMessage_128](midi2endofclipmessage().md)
- [func MIDI2EndpointDeviceIdentityNotificationMessage(MIDIUInteger7, MIDIUInteger7, MIDIUInteger7, MIDIUInteger14, MIDIUInteger14, MIDIUInteger28) -> MIDIMessage_128](midi2endpointdeviceidentitynotificationmessage(_:_:_:_:_:_:).md)
- [func MIDI2EndpointDiscoveryMessage(UInt8, UInt8, Bool, Bool, Bool, Bool, Bool) -> MIDIMessage_128](midi2endpointdiscoverymessage(_:_:_:_:_:_:_:).md)
- [func MIDI2EndpointInfoNotificationMessage(UInt8, UInt8, Bool, UInt8, Bool, Bool, Bool, Bool) -> MIDIMessage_128](midi2endpointinfonotificationmessage(_:_:_:_:_:_:_:_:).md)
- [func MIDI2EndpointNameNotificationMessage(UMPStreamMessageFormat, UnsafePointer<CChar>!, Int) -> MIDIMessage_128](midi2endpointnamenotificationmessage(_:_:_:).md)
- [func MIDI2EndpointProductInstanceIDNotificationMessage(UMPStreamMessageFormat, UnsafePointer<CChar>!, Int) -> MIDIMessage_128](midi2endpointproductinstanceidnotificationmessage(_:_:_:).md)
- [func MIDI2FlexDataMessage(MIDIUInteger4, MIDIUInteger2, MIDIUInteger2, MIDIUInteger4, UInt8, UInt8, UInt32, UInt32, UInt32) -> MIDIMessage_128](midi2flexdatamessage(_:_:_:_:_:_:_:_:_:).md)
- [func MIDI2FunctionBlockDiscoveryMessage(UInt8, Bool, Bool) -> MIDIMessage_128](midi2functionblockdiscoverymessage(_:_:_:).md)
- [func MIDI2FunctionBlockInfoNotificationMessage(Bool, MIDIUInteger7, MIDIUMPFunctionBlockUIHint, MIDIUMPFunctionBlockMIDI1Info, MIDIUMPFunctionBlockDirection, UInt8, UInt8, UInt8, UInt8) -> MIDIMessage_128](midi2functionblockinfonotificationmessage(_:_:_:_:_:_:_:_:_:).md)
- [func MIDI2FunctionBlockNameNotificationMessage(UMPStreamMessageFormat, UInt8, UnsafePointer<CChar>!, Int) -> MIDIMessage_128](midi2functionblocknamenotificationmessage(_:_:_:_:).md)
- [func MIDI2StartOfClipMessage() -> MIDIMessage_128](midi2startofclipmessage().md)
- [func MIDI2StreamConfigurationNotificationMessage(UInt8, Bool, Bool) -> MIDIMessage_128](midi2streamconfigurationnotificationmessage(_:_:_:).md)
- [func MIDI2StreamConfigurationRequestMessage(UInt8, Bool, Bool) -> MIDIMessage_128](midi2streamconfigurationrequestmessage(_:_:_:).md)
- [func MIDI2StreamMessage(UMPStreamMessageFormat, UMPStreamMessageStatus, UInt16, UInt32, UInt32, UInt32) -> MIDIMessage_128](midi2streammessage(_:_:_:_:_:_:).md)
- [func MIDI2StreamMessageFromData(UMPStreamMessageFormat, UMPStreamMessageStatus, UnsafePointer<UInt8>!, Int) -> MIDIMessage_128](midi2streammessagefromdata(_:_:_:_:).md)
- [func MIDIDeltaClockstampTicksPerQuarterNoteMessage(UInt16) -> MIDIMessage_32](midideltaclockstampticksperquarternotemessage(_:).md)
- [func MIDIDeviceAddEntity(MIDIDeviceRef, CFString, Bool, Int, Int, UnsafeMutablePointer<MIDIEntityRef>) -> OSStatus](midideviceaddentity(_:_:_:_:_:_:).md)
  Specifies one of the entities that make up a device.
- [func MIDIEventListForEachEvent(UnsafePointer<MIDIEventList>!, MIDIEventVisitor!, UnsafeMutableRawPointer!)](midieventlistforeachevent(_:_:_:).md)
- [func MIDIJitterReductionClockMessage(UInt16) -> MIDIMessage_32](midijitterreductionclockmessage(_:).md)
- [func MIDIJitterReductionTimestampMessage(UInt16) -> MIDIMessage_32](midijitterreductiontimestampmessage(_:).md)
- [func MIDINoOpMessage() -> MIDIMessage_32](midinoopmessage().md)
- [func MIDITicksSinceLastEventMessage(UInt32) -> MIDIMessage_32](miditickssincelasteventmessage(_:).md)

## See Also

- [Core MIDI Structures](core-midi-structures.md)
- [Core MIDI Enumerations](core-midi-enumerations.md)
- [Core MIDI Constants](core-midi-constants.md)
- [Core MIDI Data Types](core-midi-data-types.md)
- [Core MIDI Macros](coremidi-macros.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/core-midi-functions)*