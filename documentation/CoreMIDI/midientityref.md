# MIDIEntityRef

**Framework**: Core MIDI  
**Kind**: typealias

An entity that a device owns and that contains endpoints.

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
typealias MIDIEntityRef = MIDIObjectRef
```

#### Discussion

An entity object derives from [`MIDIObjectRef`](midiobjectref.md), and its owning object is a [`MIDIDeviceRef`](midideviceref.md).

Devices may have multiple logically distinct subcomponents; for example, a MIDI synthesizer and a pair of MIDI ports are addressable using a USB port. By grouping a device’s endpoints into entities, the system has enough information for an app to make reasonable assumptions about how to communicate bidirectionally with each entity, as required by MIDI librarian apps.

## See Also

- [func MIDIEntityGetDevice(MIDIEntityRef, UnsafeMutablePointer<MIDIDeviceRef>?) -> OSStatus](midientitygetdevice(_:_:).md)
  Returns an entity’s device.
- [func MIDIEntityGetNumberOfSources(MIDIEntityRef) -> Int](midientitygetnumberofsources(_:).md)
  Returns the number of sources in an entity.
- [func MIDIEntityGetSource(MIDIEntityRef, Int) -> MIDIEndpointRef](midientitygetsource(_:_:).md)
  Returns one of an entity’s sources.
- [func MIDIEntityGetNumberOfDestinations(MIDIEntityRef) -> Int](midientitygetnumberofdestinations(_:).md)
  Returns the number of destinations in an entity.
- [func MIDIEntityGetDestination(MIDIEntityRef, Int) -> MIDIEndpointRef](midientitygetdestination(_:_:).md)
  Returns one of an entity’s destinations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midientityref)*