# MIDI2EndOfClipMessage()

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
func MIDI2EndOfClipMessage() -> MIDIMessage_128
```

## See Also

- [func MIDI1UPChannelPressure(UInt8, UInt8, UInt8) -> MIDIMessage_32](midi1upchannelpressure(_:_:_:).md)
- [func MIDI1UPPolyPressure(UInt8, UInt8, UInt8, UInt8) -> MIDIMessage_32](midi1uppolypressure(_:_:_:_:).md)
- [func MIDI1UPProgramChange(UInt8, UInt8, UInt8) -> MIDIMessage_32](midi1upprogramchange(_:_:_:).md)
- [func MIDI1UPSysEx(UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8) -> MIDIMessage_64](midi1upsysex(_:_:_:_:_:_:_:_:_:).md)
- [func MIDI1UPSysExArray(UInt8, UInt8, UnsafePointer<UInt8>!, UnsafePointer<UInt8>!) -> MIDIMessage_64](midi1upsysexarray(_:_:_:_:).md)
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midi2endofclipmessage())*