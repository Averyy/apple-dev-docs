# MIDIEntityRef

**Framework**: Core MIDI  
**Kind**: typealias  
**Role**: Type Alias

An entity that a device owns and that contains endpoints.

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
typealias MIDIEntityRef = MIDIObjectRef
```

```c
typedef MIDIObjectRef MIDIEntityRef;
```

#### Discussion

An entity object derives from [`MIDIObjectRef`](./midiobjectref.md), and its owning object is a [`MIDIDeviceRef`](./midideviceref.md).

Devices may have multiple logically distinct subcomponents; for example, a MIDI synthesizer and a pair of MIDI ports are addressable using a USB port. By grouping a device’s endpoints into entities, the system has enough information for an app to make reasonable assumptions about how to communicate bidirectionally with each entity, as required by MIDI librarian apps.

## See Also

### Entity lookup
- [func MIDIEntityGetDevice(MIDIEntityRef, UnsafeMutablePointer<MIDIDeviceRef>?) -> OSStatus](./midientitygetdevice%28_,_%29.md)
  Returns an entity’s device.
- [func MIDIEntityGetNumberOfSources(MIDIEntityRef) -> Int](./midientitygetnumberofsources%28_%29.md)
  Returns the number of sources in an entity.
- [func MIDIEntityGetSource(MIDIEntityRef, Int) -> MIDIEndpointRef](./midientitygetsource%28_,_%29.md)
  Returns one of an entity’s sources.
- [func MIDIEntityGetNumberOfDestinations(MIDIEntityRef) -> Int](./midientitygetnumberofdestinations%28_%29.md)
  Returns the number of destinations in an entity.
- [func MIDIEntityGetDestination(MIDIEntityRef, Int) -> MIDIEndpointRef](./midientitygetdestination%28_,_%29.md)
  Returns one of an entity’s destinations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midientityref)*