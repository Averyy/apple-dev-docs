# MIDI Messages

**Framework**: Core MIDI

Create and configure messages.

## Topics

### MIDI 1.0 Messages
- [func MIDI1UPNoteOn(UInt8, UInt8, UInt8, UInt8) -> MIDIMessage_32](midi1upnoteon(_:_:_:_:).md)
- [func MIDI1UPNoteOff(UInt8, UInt8, UInt8, UInt8) -> MIDIMessage_32](midi1upnoteoff(_:_:_:_:).md)
- [func MIDI1UPPitchBend(UInt8, UInt8, UInt8, UInt8) -> MIDIMessage_32](midi1uppitchbend(_:_:_:_:).md)
- [func MIDI1UPControlChange(UInt8, UInt8, UInt8, UInt8) -> MIDIMessage_32](midi1upcontrolchange(_:_:_:_:).md)
- [func MIDI1UPSystemCommon(UInt8, UInt8, UInt8, UInt8) -> MIDIMessage_32](midi1upsystemcommon(_:_:_:_:).md)
- [func MIDI1UPChannelVoiceMessage(UInt8, UInt8, UInt8, UInt8, UInt8) -> MIDIMessage_32](midi1upchannelvoicemessage(_:_:_:_:_:).md)
- [func MIDIMessageTypeForUPWord(UInt32) -> MIDIMessageType](midimessagetypeforupword(_:).md)
### MIDI 2.0 Messages
- [func MIDI2ChannelVoiceMessage(UInt8, UInt8, UInt8, UInt16, UInt32) -> MIDIMessage_64](midi2channelvoicemessage(_:_:_:_:_:).md)
- [func MIDI2NoteOn(UInt8, UInt8, UInt8, UInt8, UInt16, UInt16) -> MIDIMessage_64](midi2noteon(_:_:_:_:_:_:).md)
- [func MIDI2NoteOff(UInt8, UInt8, UInt8, UInt8, UInt16, UInt16) -> MIDIMessage_64](midi2noteoff(_:_:_:_:_:_:).md)
- [func MIDI2ControlChange(UInt8, UInt8, UInt8, UInt32) -> MIDIMessage_64](midi2controlchange(_:_:_:_:).md)
- [func MIDI2ProgramChange(UInt8, UInt8, Bool, UInt8, UInt8, UInt8) -> MIDIMessage_64](midi2programchange(_:_:_:_:_:_:).md)
- [func MIDI2PitchBend(UInt8, UInt8, UInt32) -> MIDIMessage_64](midi2pitchbend(_:_:_:).md)
- [func MIDI2PerNotePitchBend(UInt8, UInt8, UInt8, UInt32) -> MIDIMessage_64](midi2pernotepitchbend(_:_:_:_:).md)
- [func MIDI2ChannelPressure(UInt8, UInt8, UInt32) -> MIDIMessage_64](midi2channelpressure(_:_:_:).md)
- [func MIDI2PolyPressure(UInt8, UInt8, UInt8, UInt32) -> MIDIMessage_64](midi2polypressure(_:_:_:_:).md)
- [func MIDI2AssignableControl(UInt8, UInt8, UInt8, UInt8, UInt32) -> MIDIMessage_64](midi2assignablecontrol(_:_:_:_:_:).md)
- [func MIDI2RelRegisteredControl(UInt8, UInt8, UInt8, UInt8, UInt32) -> MIDIMessage_64](midi2relregisteredcontrol(_:_:_:_:_:).md)
- [func MIDI2AssignablePNC(UInt8, UInt8, UInt8, UInt8, UInt32) -> MIDIMessage_64](midi2assignablepnc(_:_:_:_:_:).md)
- [func MIDI2RegisteredPNC(UInt8, UInt8, UInt8, UInt8, UInt32) -> MIDIMessage_64](midi2registeredpnc(_:_:_:_:_:).md)
- [func MIDI2RelAssignableControl(UInt8, UInt8, UInt8, UInt8, UInt32) -> MIDIMessage_64](midi2relassignablecontrol(_:_:_:_:_:).md)
- [func MIDI2RegisteredControl(UInt8, UInt8, UInt8, UInt8, UInt32) -> MIDIMessage_64](midi2registeredcontrol(_:_:_:_:_:).md)
- [func MIDI2PerNoteManagment(UInt8, UInt8, UInt8, Bool, Bool) -> MIDIMessage_64](midi2pernotemanagment(_:_:_:_:_:).md)
### Common
- [enum MIDICVStatus](midicvstatus.md)
  MIDI status types.
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

## See Also

- [MIDI Services](midi-services.md)
  Communicate with hardware using Universal MIDI Packets.
- [MIDI System Setup](midi-system-setup.md)
  Configure the global MIDI system.
- [MIDI Bluetooth](midi-bluetooth.md)
  Connect to Bluetooth Low Energy MIDI peripherals.
- [MIDI Thru Connection](midi-thru-connection.md)
  Create play-through connections between sources and destinations.
- [MIDI Networking](midi-networking.md)
  Create and manage devices connected over a local network.
- [MIDI Drivers](midi-drivers.md)
  Create driver plug-ins.
- [MIDI Capability Inquiry](midi-capability-inquiry.md)
  Provide support for bidirectional discovery and configuration of devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midi-messages)*