# MIDIEntityGetNumberOfSources(_:)

**Framework**: Core MIDI  
**Kind**: func  
**Role**: Function

Returns the number of sources in an entity.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func MIDIEntityGetNumberOfSources(_ entity: MIDIEntityRef) -> Int
```

```c
extern ItemCount MIDIEntityGetNumberOfSources(MIDIEntityRef entity);
```

#### Return Value

The number of sources the entity contains, or 0 if an error occurred.

## Parameters

- `entity`: The entity to query.

## See Also

### Entity lookup
- [func MIDIEntityGetDevice(MIDIEntityRef, UnsafeMutablePointer<MIDIDeviceRef>?) -> OSStatus](./midientitygetdevice%28_,_%29.md)
  Returns an entity’s device.
- [func MIDIEntityGetSource(MIDIEntityRef, Int) -> MIDIEndpointRef](./midientitygetsource%28_,_%29.md)
  Returns one of an entity’s sources.
- [func MIDIEntityGetNumberOfDestinations(MIDIEntityRef) -> Int](./midientitygetnumberofdestinations%28_%29.md)
  Returns the number of destinations in an entity.
- [func MIDIEntityGetDestination(MIDIEntityRef, Int) -> MIDIEndpointRef](./midientitygetdestination%28_,_%29.md)
  Returns one of an entity’s destinations.
- [typealias MIDIEntityRef](./midientityref.md)
  An entity that a device owns and that contains endpoints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midientitygetnumberofsources(_:))*