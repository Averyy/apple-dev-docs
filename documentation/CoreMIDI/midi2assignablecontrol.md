# MIDI2AssignableControl(_:_:_:_:_:)

**Framework**: Core MIDI  
**Kind**: func

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
func MIDI2AssignableControl(_ group: UInt8, _ channel: UInt8, _ bank: UInt8, _ index: UInt8, _ value: UInt32) -> MIDIMessage_64
```

## See Also

- [func MIDI2ChannelVoiceMessage(UInt8, UInt8, UInt8, UInt16, UInt32) -> MIDIMessage_64](midi2channelvoicemessage(_:_:_:_:_:).md)
- [func MIDI2NoteOn(UInt8, UInt8, UInt8, UInt8, UInt16, UInt16) -> MIDIMessage_64](midi2noteon(_:_:_:_:_:_:).md)
- [func MIDI2NoteOff(UInt8, UInt8, UInt8, UInt8, UInt16, UInt16) -> MIDIMessage_64](midi2noteoff(_:_:_:_:_:_:).md)
- [func MIDI2ControlChange(UInt8, UInt8, UInt8, UInt32) -> MIDIMessage_64](midi2controlchange(_:_:_:_:).md)
- [func MIDI2ProgramChange(UInt8, UInt8, Bool, UInt8, UInt8, UInt8) -> MIDIMessage_64](midi2programchange(_:_:_:_:_:_:).md)
- [func MIDI2PitchBend(UInt8, UInt8, UInt32) -> MIDIMessage_64](midi2pitchbend(_:_:_:).md)
- [func MIDI2PerNotePitchBend(UInt8, UInt8, UInt8, UInt32) -> MIDIMessage_64](midi2pernotepitchbend(_:_:_:_:).md)
- [func MIDI2ChannelPressure(UInt8, UInt8, UInt32) -> MIDIMessage_64](midi2channelpressure(_:_:_:).md)
- [func MIDI2PolyPressure(UInt8, UInt8, UInt8, UInt32) -> MIDIMessage_64](midi2polypressure(_:_:_:_:).md)
- [func MIDI2RelRegisteredControl(UInt8, UInt8, UInt8, UInt8, UInt32) -> MIDIMessage_64](midi2relregisteredcontrol(_:_:_:_:_:).md)
- [func MIDI2AssignablePNC(UInt8, UInt8, UInt8, UInt8, UInt32) -> MIDIMessage_64](midi2assignablepnc(_:_:_:_:_:).md)
- [func MIDI2RegisteredPNC(UInt8, UInt8, UInt8, UInt8, UInt32) -> MIDIMessage_64](midi2registeredpnc(_:_:_:_:_:).md)
- [func MIDI2RelAssignableControl(UInt8, UInt8, UInt8, UInt8, UInt32) -> MIDIMessage_64](midi2relassignablecontrol(_:_:_:_:_:).md)
- [func MIDI2RegisteredControl(UInt8, UInt8, UInt8, UInt8, UInt32) -> MIDIMessage_64](midi2registeredcontrol(_:_:_:_:_:).md)
- [func MIDI2PerNoteManagment(UInt8, UInt8, UInt8, Bool, Bool) -> MIDIMessage_64](midi2pernotemanagment(_:_:_:_:_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midi2assignablecontrol(_:_:_:_:_:))*