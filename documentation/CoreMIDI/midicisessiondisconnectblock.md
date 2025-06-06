# MIDICISessionDisconnectBlock

**Framework**: Core MIDI  
**Kind**: typealias

A block the system calls when a MIDI-CI session disconnects.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
typealias MIDICISessionDisconnectBlock = (MIDICISession, any Error) -> Void
```

#### Discussion

If the system calls this block, terminate the MIDI-CI session.

## Parameters

- `session`: The disconnected session instance.
- `error`: An object that provides error information, if any.

## See Also

- [typealias MIDICIDeviceID](midicideviceid.md)
- [MIDICIDeviceManager.DictionaryKey](midicidevicemanager/dictionarykey.md)
- [typealias MIDICIMUID](midicimuid.md)
- [struct MIDICIPropertyExchangeRequestID](midicipropertyexchangerequestid.md)
- [typealias MIDIEventVisitor](midieventvisitor.md)
- [typealias MIDIUInteger14](midiuinteger14.md)
- [typealias MIDIUInteger2](midiuinteger2.md)
- [typealias MIDIUInteger28](midiuinteger28.md)
- [typealias MIDIUInteger4](midiuinteger4.md)
- [typealias MIDIUInteger7](midiuinteger7.md)
- [MIDIUMPEndpointManager.DictionaryKey](midiumpendpointmanager/dictionarykey.md)
- [typealias MIDIUMPFunctionBlockID](midiumpfunctionblockid.md)
- [typealias MIDIUMPGroupNumber](midiumpgroupnumber.md)
- [typealias MIDICIDiscoveryResponseBlock](midicidiscoveryresponseblock.md)
  A block the system calls when a MIDI-CI node discovery request completes.
- [typealias MIDIChannelNumber](midichannelnumber.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midicisessiondisconnectblock)*