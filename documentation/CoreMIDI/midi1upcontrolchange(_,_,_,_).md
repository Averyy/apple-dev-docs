# MIDI1UPControlChange(_:_:_:_:)

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
func MIDI1UPControlChange(_ group: UInt8, _ channel: UInt8, _ index: UInt8, _ data: UInt8) -> MIDIMessage_32
```

```c
static MIDIMessage_32 MIDI1UPControlChange(UInt8 group, UInt8 channel, UInt8 index, UInt8 data);
```

## See Also

### MIDI 1.0 Messages
- [func MIDI1UPNoteOn(UInt8, UInt8, UInt8, UInt8) -> MIDIMessage_32](./midi1upnoteon%28_,_,_,_%29.md)
- [func MIDI1UPNoteOff(UInt8, UInt8, UInt8, UInt8) -> MIDIMessage_32](./midi1upnoteoff%28_,_,_,_%29.md)
- [func MIDI1UPPitchBend(UInt8, UInt8, UInt8, UInt8) -> MIDIMessage_32](./midi1uppitchbend%28_,_,_,_%29.md)
- [func MIDI1UPSystemCommon(UInt8, UInt8, UInt8, UInt8) -> MIDIMessage_32](./midi1upsystemcommon%28_,_,_,_%29.md)
- [func MIDI1UPChannelVoiceMessage(UInt8, UInt8, UInt8, UInt8, UInt8) -> MIDIMessage_32](./midi1upchannelvoicemessage%28_,_,_,_,_%29.md)
- [func MIDIMessageTypeForUPWord(UInt32) -> MIDIMessageType](./midimessagetypeforupword%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midi1upcontrolchange(_:_:_:_:))*