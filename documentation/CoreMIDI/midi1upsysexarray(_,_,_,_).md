# MIDI1UPSysExArray(_:_:_:_:)

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
func MIDI1UPSysExArray(_ group: UInt8, _ status: UInt8, _ begin: UnsafePointer<UInt8>!, _ end: UnsafePointer<UInt8>!) -> MIDIMessage_64
```

```c
static MIDIMessage_64 MIDI1UPSysExArray(UInt8 group, UInt8 status, const Byte *begin, const Byte *end);
```

## See Also

### Functions
- [func MIDI1UPChannelPressure(UInt8, UInt8, UInt8) -> MIDIMessage_32](./midi1upchannelpressure%28_,_,_%29.md)
- [func MIDI1UPPolyPressure(UInt8, UInt8, UInt8, UInt8) -> MIDIMessage_32](./midi1uppolypressure%28_,_,_,_%29.md)
- [func MIDI1UPProgramChange(UInt8, UInt8, UInt8) -> MIDIMessage_32](./midi1upprogramchange%28_,_,_%29.md)
- [func MIDI1UPSysEx(UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8) -> MIDIMessage_64](./midi1upsysex%28_,_,_,_,_,_,_,_,_%29.md)
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midi1upsysexarray(_:_:_:_:))*