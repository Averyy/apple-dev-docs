# MIDISetupRef

**Framework**: Core MIDI  
**Kind**: typealias

A type that represents the global state of the MIDI system, that contains lists of the devices and serial port owners.

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
typealias MIDISetupRef = MIDIObjectRef
```

#### Discussion

Derives from MIDIObjectRef, does not have an owner object.

Generally, only MIDI drivers and specialized configuration editors will need to manipulate MIDISetup objects, not the average MIDI client application. As of CoreMIDI 1.1, the MIDIServer maintains a single global MIDISetupRef, stored persistently in a preference file.

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
- [typealias MIDICISessionDisconnectBlock](midicisessiondisconnectblock.md)
  A block the system calls when a MIDI-CI session disconnects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midisetupref)*