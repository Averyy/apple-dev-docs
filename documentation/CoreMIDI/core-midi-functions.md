# Core MIDI Functions

**Framework**: Core MIDI  
**Role**: API Collection

## Topics

### Functions
- [func MIDI1UPChannelPressure(UInt8, UInt8, UInt8) -> MIDIMessage_32](./midi1upchannelpressure%28_,_,_%29.md)
- [func MIDI1UPPolyPressure(UInt8, UInt8, UInt8, UInt8) -> MIDIMessage_32](./midi1uppolypressure%28_,_,_,_%29.md)
- [func MIDI1UPProgramChange(UInt8, UInt8, UInt8) -> MIDIMessage_32](./midi1upprogramchange%28_,_,_%29.md)
- [func MIDI1UPSysEx(UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8) -> MIDIMessage_64](./midi1upsysex%28_,_,_,_,_,_,_,_,_%29.md)
- [func MIDI1UPSysExArray(UInt8, UInt8, UnsafePointer<UInt8>!, UnsafePointer<UInt8>!) -> MIDIMessage_64](./midi1upsysexarray%28_,_,_,_%29.md)
- [func MIDI2EndOfClipMessage() -> MIDIMessage_128](./midi2endofclipmessage%28%29.md)
- [func MIDI2EndpointDeviceIdentityNotificationMessage(MIDIUInteger7, MIDIUInteger7, MIDIUInteger7, MIDIUInteger14, MIDIUInteger14, MIDIUInteger28) -> MIDIMessage_128](./midi2endpointdeviceidentitynotificationmessage%28_,_,_,_,_,_%29.md)
- [func MIDI2EndpointDiscoveryMessage(UInt8, UInt8, Bool, Bool, Bool, Bool, Bool) -> MIDIMessage_128](./midi2endpointdiscoverymessage%28_,_,_,_,_,_,_%29.md)
- [func MIDI2EndpointInfoNotificationMessage(UInt8, UInt8, Bool, UInt8, Bool, Bool, Bool, Bool) -> MIDIMessage_128](./midi2endpointinfonotificationmessage%28_,_,_,_,_,_,_,_%29.md)
- [func MIDI2EndpointNameNotificationMessage(UMPStreamMessageFormat, UnsafePointer<CChar>!, Int) -> MIDIMessage_128](./midi2endpointnamenotificationmessage%28_,_,_%29.md)
- [func MIDI2EndpointProductInstanceIDNotificationMessage(UMPStreamMessageFormat, UnsafePointer<CChar>!, Int) -> MIDIMessage_128](./midi2endpointproductinstanceidnotificationmessage%28_,_,_%29.md)
- [func MIDI2FlexDataMessage(MIDIUInteger4, MIDIUInteger2, MIDIUInteger2, MIDIUInteger4, UInt8, UInt8, UInt32, UInt32, UInt32) -> MIDIMessage_128](./midi2flexdatamessage%28_,_,_,_,_,_,_,_,_%29.md)
- [func MIDI2FunctionBlockDiscoveryMessage(UInt8, Bool, Bool) -> MIDIMessage_128](./midi2functionblockdiscoverymessage%28_,_,_%29.md)
- [func MIDI2FunctionBlockInfoNotificationMessage(Bool, MIDIUInteger7, MIDIUMPFunctionBlockUIHint, MIDIUMPFunctionBlockMIDI1Info, MIDIUMPFunctionBlockDirection, UInt8, UInt8, UInt8, UInt8) -> MIDIMessage_128](./midi2functionblockinfonotificationmessage%28_,_,_,_,_,_,_,_,_%29.md)
- [func MIDI2FunctionBlockNameNotificationMessage(UMPStreamMessageFormat, UInt8, UnsafePointer<CChar>!, Int) -> MIDIMessage_128](./midi2functionblocknamenotificationmessage%28_,_,_,_%29.md)
- [func MIDI2StartOfClipMessage() -> MIDIMessage_128](./midi2startofclipmessage%28%29.md)
- [func MIDI2StreamConfigurationNotificationMessage(UInt8, Bool, Bool) -> MIDIMessage_128](./midi2streamconfigurationnotificationmessage%28_,_,_%29.md)
- [func MIDI2StreamConfigurationRequestMessage(UInt8, Bool, Bool) -> MIDIMessage_128](./midi2streamconfigurationrequestmessage%28_,_,_%29.md)
- [func MIDI2StreamMessage(UMPStreamMessageFormat, UMPStreamMessageStatus, UInt16, UInt32, UInt32, UInt32) -> MIDIMessage_128](./midi2streammessage%28_,_,_,_,_,_%29.md)
- [func MIDI2StreamMessageFromData(UMPStreamMessageFormat, UMPStreamMessageStatus, UnsafePointer<UInt8>!, Int) -> MIDIMessage_128](./midi2streammessagefromdata%28_,_,_,_%29.md)
- [func MIDIDeltaClockstampTicksPerQuarterNoteMessage(UInt16) -> MIDIMessage_32](./midideltaclockstampticksperquarternotemessage%28_%29.md)
- [func MIDIDeviceAddEntity(MIDIDeviceRef, CFString, Bool, Int, Int, UnsafeMutablePointer<MIDIEntityRef>) -> OSStatus](./midideviceaddentity%28_,_,_,_,_,_%29.md)
  Specifies one of the entities that make up a device.
- [func MIDIEventListForEachEvent(UnsafePointer<MIDIEventList>!, MIDIEventVisitor!, UnsafeMutableRawPointer!)](./midieventlistforeachevent%28_,_,_%29.md)
- [func MIDIJitterReductionClockMessage(UInt16) -> MIDIMessage_32](./midijitterreductionclockmessage%28_%29.md)
- [func MIDIJitterReductionTimestampMessage(UInt16) -> MIDIMessage_32](./midijitterreductiontimestampmessage%28_%29.md)
- [func MIDINoOpMessage() -> MIDIMessage_32](./midinoopmessage%28%29.md)
- [func MIDITicksSinceLastEventMessage(UInt32) -> MIDIMessage_32](./miditickssincelasteventmessage%28_%29.md)
- [MIDIGetSerialPortDrivers](./midigetserialportdrivers.md)
  Returns a list of installed MIDI drivers for serial port MIDI devices.
- [MIDIGetSerialPortOwner](./midigetserialportowner.md)
  Returns the MIDI driver that owns a serial port.
- [MIDISetSerialPortOwner](./midisetserialportowner.md)
  Specifies the MIDI driver that owns a serial port.
- [MIDISetupCreate](./midisetupcreate.md)
  Queries drivers to discover what hardware is available.
- [MIDISetupDispose](./midisetupdispose.md)
  Disposes the specified setup object.
- [MIDISetupFromData](./midisetupfromdata.md)
  Creates a MIDISetup object from an XML stream.
- [MIDISetupGetCurrent](./midisetupgetcurrent.md)
  Returns the system’s current MIDISetup.
- [MIDISetupInstall](./midisetupinstall.md)
  Installs a MIDISetup as the system’s current state.
- [MIDISetupToData](./midisetuptodata.md)
  Creates an XML representation of a MIDISetup object.

## See Also

### Reference
- [Core MIDI Structures](./core-midi-structures.md)
- [Core MIDI Enumerations](./core-midi-enumerations.md)
- [Core MIDI Constants](./core-midi-constants.md)
- [Core MIDI Data Types](./core-midi-data-types.md)
- [Core MIDI Macros](./coremidi-macros.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/core-midi-functions)*