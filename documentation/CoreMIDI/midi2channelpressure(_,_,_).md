# MIDI2ChannelPressure(_:_:_:)

**Framework**: Core MIDI  
**Kind**: func  
**Role**: Function

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
func MIDI2ChannelPressure(_ group: UInt8, _ channel: UInt8, _ value: UInt32) -> MIDIMessage_64
```

```c
static MIDIMessage_64 MIDI2ChannelPressure(UInt8 group, UInt8 channel, UInt32 value);
```

## See Also

### MIDI 2.0 Messages
- [func MIDI2ChannelVoiceMessage(UInt8, UInt8, UInt8, UInt16, UInt32) -> MIDIMessage_64](./midi2channelvoicemessage%28_,_,_,_,_%29.md)
- [func MIDI2NoteOn(UInt8, UInt8, UInt8, UInt8, UInt16, UInt16) -> MIDIMessage_64](./midi2noteon%28_,_,_,_,_,_%29.md)
- [func MIDI2NoteOff(UInt8, UInt8, UInt8, UInt8, UInt16, UInt16) -> MIDIMessage_64](./midi2noteoff%28_,_,_,_,_,_%29.md)
- [func MIDI2ControlChange(UInt8, UInt8, UInt8, UInt32) -> MIDIMessage_64](./midi2controlchange%28_,_,_,_%29.md)
- [func MIDI2ProgramChange(UInt8, UInt8, Bool, UInt8, UInt8, UInt8) -> MIDIMessage_64](./midi2programchange%28_,_,_,_,_,_%29.md)
- [func MIDI2PitchBend(UInt8, UInt8, UInt32) -> MIDIMessage_64](./midi2pitchbend%28_,_,_%29.md)
- [func MIDI2PerNotePitchBend(UInt8, UInt8, UInt8, UInt32) -> MIDIMessage_64](./midi2pernotepitchbend%28_,_,_,_%29.md)
- [func MIDI2PolyPressure(UInt8, UInt8, UInt8, UInt32) -> MIDIMessage_64](./midi2polypressure%28_,_,_,_%29.md)
- [func MIDI2AssignableControl(UInt8, UInt8, UInt8, UInt8, UInt32) -> MIDIMessage_64](./midi2assignablecontrol%28_,_,_,_,_%29.md)
- [func MIDI2RelRegisteredControl(UInt8, UInt8, UInt8, UInt8, UInt32) -> MIDIMessage_64](./midi2relregisteredcontrol%28_,_,_,_,_%29.md)
- [func MIDI2AssignablePNC(UInt8, UInt8, UInt8, UInt8, UInt32) -> MIDIMessage_64](./midi2assignablepnc%28_,_,_,_,_%29.md)
- [func MIDI2RegisteredPNC(UInt8, UInt8, UInt8, UInt8, UInt32) -> MIDIMessage_64](./midi2registeredpnc%28_,_,_,_,_%29.md)
- [func MIDI2RelAssignableControl(UInt8, UInt8, UInt8, UInt8, UInt32) -> MIDIMessage_64](./midi2relassignablecontrol%28_,_,_,_,_%29.md)
- [func MIDI2RegisteredControl(UInt8, UInt8, UInt8, UInt8, UInt32) -> MIDIMessage_64](./midi2registeredcontrol%28_,_,_,_,_%29.md)
- [func MIDI2PerNoteManagment(UInt8, UInt8, UInt8, Bool, Bool) -> MIDIMessage_64](./midi2pernotemanagment%28_,_,_,_,_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midi2channelpressure(_:_:_:))*