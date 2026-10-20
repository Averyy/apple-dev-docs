# MIDI Messages

**Framework**: Core MIDI  
**Role**: API Collection

Create and configure messages.

## Topics

### MIDI 1.0 Messages
- [func MIDI1UPNoteOn(UInt8, UInt8, UInt8, UInt8) -> MIDIMessage_32](./midi1upnoteon%28_,_,_,_%29.md)
- [func MIDI1UPNoteOff(UInt8, UInt8, UInt8, UInt8) -> MIDIMessage_32](./midi1upnoteoff%28_,_,_,_%29.md)
- [func MIDI1UPPitchBend(UInt8, UInt8, UInt8, UInt8) -> MIDIMessage_32](./midi1uppitchbend%28_,_,_,_%29.md)
- [func MIDI1UPControlChange(UInt8, UInt8, UInt8, UInt8) -> MIDIMessage_32](./midi1upcontrolchange%28_,_,_,_%29.md)
- [func MIDI1UPSystemCommon(UInt8, UInt8, UInt8, UInt8) -> MIDIMessage_32](./midi1upsystemcommon%28_,_,_,_%29.md)
- [func MIDI1UPChannelVoiceMessage(UInt8, UInt8, UInt8, UInt8, UInt8) -> MIDIMessage_32](./midi1upchannelvoicemessage%28_,_,_,_,_%29.md)
- [func MIDIMessageTypeForUPWord(UInt32) -> MIDIMessageType](./midimessagetypeforupword%28_%29.md)
### MIDI 2.0 Messages
- [func MIDI2ChannelVoiceMessage(UInt8, UInt8, UInt8, UInt16, UInt32) -> MIDIMessage_64](./midi2channelvoicemessage%28_,_,_,_,_%29.md)
- [func MIDI2NoteOn(UInt8, UInt8, UInt8, UInt8, UInt16, UInt16) -> MIDIMessage_64](./midi2noteon%28_,_,_,_,_,_%29.md)
- [func MIDI2NoteOff(UInt8, UInt8, UInt8, UInt8, UInt16, UInt16) -> MIDIMessage_64](./midi2noteoff%28_,_,_,_,_,_%29.md)
- [func MIDI2ControlChange(UInt8, UInt8, UInt8, UInt32) -> MIDIMessage_64](./midi2controlchange%28_,_,_,_%29.md)
- [func MIDI2ProgramChange(UInt8, UInt8, Bool, UInt8, UInt8, UInt8) -> MIDIMessage_64](./midi2programchange%28_,_,_,_,_,_%29.md)
- [func MIDI2PitchBend(UInt8, UInt8, UInt32) -> MIDIMessage_64](./midi2pitchbend%28_,_,_%29.md)
- [func MIDI2PerNotePitchBend(UInt8, UInt8, UInt8, UInt32) -> MIDIMessage_64](./midi2pernotepitchbend%28_,_,_,_%29.md)
- [func MIDI2ChannelPressure(UInt8, UInt8, UInt32) -> MIDIMessage_64](./midi2channelpressure%28_,_,_%29.md)
- [func MIDI2PolyPressure(UInt8, UInt8, UInt8, UInt32) -> MIDIMessage_64](./midi2polypressure%28_,_,_,_%29.md)
- [func MIDI2AssignableControl(UInt8, UInt8, UInt8, UInt8, UInt32) -> MIDIMessage_64](./midi2assignablecontrol%28_,_,_,_,_%29.md)
- [func MIDI2RelRegisteredControl(UInt8, UInt8, UInt8, UInt8, UInt32) -> MIDIMessage_64](./midi2relregisteredcontrol%28_,_,_,_,_%29.md)
- [func MIDI2AssignablePNC(UInt8, UInt8, UInt8, UInt8, UInt32) -> MIDIMessage_64](./midi2assignablepnc%28_,_,_,_,_%29.md)
- [func MIDI2RegisteredPNC(UInt8, UInt8, UInt8, UInt8, UInt32) -> MIDIMessage_64](./midi2registeredpnc%28_,_,_,_,_%29.md)
- [func MIDI2RelAssignableControl(UInt8, UInt8, UInt8, UInt8, UInt32) -> MIDIMessage_64](./midi2relassignablecontrol%28_,_,_,_,_%29.md)
- [func MIDI2RegisteredControl(UInt8, UInt8, UInt8, UInt8, UInt32) -> MIDIMessage_64](./midi2registeredcontrol%28_,_,_,_,_%29.md)
- [func MIDI2PerNoteManagment(UInt8, UInt8, UInt8, Bool, Bool) -> MIDIMessage_64](./midi2pernotemanagment%28_,_,_,_,_%29.md)
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
- [enum MIDIMessageType](./midimessagetype.md)
  Supported MIDI message types.

## See Also

### Services
- [MIDI Services](./midi-services.md)
  Communicate with hardware using Universal MIDI Packets.
- [MIDI System Setup](./midi-system-setup.md)
  Configure the global MIDI system.
- [MIDI Bluetooth](./midi-bluetooth.md)
  Connect to Bluetooth Low Energy MIDI peripherals.
- [MIDI Thru Connection](./midi-thru-connection.md)
  Create play-through connections between sources and destinations.
- [MIDI Networking](./midi-networking.md)
  Create and manage devices connected over a local network.
- [MIDI Drivers](./midi-drivers.md)
  Create driver plug-ins.
- [MIDI Capability Inquiry](./midi-capability-inquiry.md)
  Provide support for bidirectional discovery and configuration of devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midi-messages)*