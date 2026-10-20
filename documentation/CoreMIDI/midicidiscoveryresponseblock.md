# MIDICIDiscoveryResponseBlock

**Framework**: Core MIDI  
**Kind**: typealias  
**Role**: Type Alias

A block the system calls when a MIDI-CI node discovery request completes.

**Availability**:
- iOS 14.0+ - Deprecated in 18.0
- iPadOS 14.0+ - Deprecated in 18.0
- Mac Catalyst 14.0+ - Deprecated in 18.0
- macOS 11.0+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: No longer supported for CoreMIDI

## Declaration

```swift
typealias MIDICIDiscoveryResponseBlock = ([MIDICIDiscoveredNode]) -> Void
```

```c
typedef void (^)(NSArray<MIDICIDiscoveredNode *> *) MIDICIDiscoveryResponseBlock;
```

## Parameters

- `discoveredNodes`: The array of discovered nodes.

## See Also

### Data Types
- [typealias MIDICIDeviceID](./midicideviceid.md)
- [MIDICIDeviceManager.DictionaryKey](./midicidevicemanager/dictionarykey.md)
- [typealias MIDICIMUID](./midicimuid.md)
- [struct MIDICIPropertyExchangeRequestID](./midicipropertyexchangerequestid.md)
- [typealias MIDIEventVisitor](./midieventvisitor.md)
- [typealias MIDIUInteger14](./midiuinteger14.md)
- [typealias MIDIUInteger2](./midiuinteger2.md)
- [typealias MIDIUInteger28](./midiuinteger28.md)
- [typealias MIDIUInteger4](./midiuinteger4.md)
- [typealias MIDIUInteger7](./midiuinteger7.md)
- [MIDIUMPEndpointManager.DictionaryKey](./midiumpendpointmanager/dictionarykey.md)
- [typealias MIDIUMPFunctionBlockID](./midiumpfunctionblockid.md)
- [typealias MIDIUMPGroupNumber](./midiumpgroupnumber.md)
- [typealias MIDICISessionDisconnectBlock](./midicisessiondisconnectblock.md)
  A block the system calls when a MIDI-CI session disconnects.
- [typealias MIDIChannelNumber](./midichannelnumber.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midicidiscoveryresponseblock)*