# MIDI1UPChannelVoiceMessage(_:_:_:_:_:)

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
func MIDI1UPChannelVoiceMessage(_ group: UInt8, _ status: UInt8, _ channel: UInt8, _ data1: UInt8, _ data2: UInt8) -> MIDIMessage_32
```

## See Also

- [func MIDI1UPNoteOn(UInt8, UInt8, UInt8, UInt8) -> MIDIMessage_32](midi1upnoteon(_:_:_:_:).md)
- [func MIDI1UPNoteOff(UInt8, UInt8, UInt8, UInt8) -> MIDIMessage_32](midi1upnoteoff(_:_:_:_:).md)
- [func MIDI1UPPitchBend(UInt8, UInt8, UInt8, UInt8) -> MIDIMessage_32](midi1uppitchbend(_:_:_:_:).md)
- [func MIDI1UPControlChange(UInt8, UInt8, UInt8, UInt8) -> MIDIMessage_32](midi1upcontrolchange(_:_:_:_:).md)
- [func MIDI1UPSystemCommon(UInt8, UInt8, UInt8, UInt8) -> MIDIMessage_32](midi1upsystemcommon(_:_:_:_:).md)
- [func MIDIMessageTypeForUPWord(UInt32) -> MIDIMessageType](midimessagetypeforupword(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midi1upchannelvoicemessage(_:_:_:_:_:))*