# MIDIEntityGetDevice(_:_:)

**Framework**: Core MIDI  
**Kind**: func  
**Role**: Function

Returns an entity’s device.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.2+
- visionOS 1.0+

## Declaration

```swift
func MIDIEntityGetDevice(_ inEntity: MIDIEntityRef, _ outDevice: UnsafeMutablePointer<MIDIDeviceRef>?) -> OSStatus
```

```c
extern OSStatus MIDIEntityGetDevice(MIDIEntityRef inEntity, MIDIDeviceRef *outDevice);
```

## Return Value

An `OSStatus` result code.

## Parameters

- `inEntity`: The entity to query.
- `outDevice`: On successful return, the entity’s owning device.

## See Also

### Entity lookup
- [func MIDIEntityGetNumberOfSources(MIDIEntityRef) -> Int](./midientitygetnumberofsources%28_%29.md)
  Returns the number of sources in an entity.
- [func MIDIEntityGetSource(MIDIEntityRef, Int) -> MIDIEndpointRef](./midientitygetsource%28_,_%29.md)
  Returns one of an entity’s sources.
- [func MIDIEntityGetNumberOfDestinations(MIDIEntityRef) -> Int](./midientitygetnumberofdestinations%28_%29.md)
  Returns the number of destinations in an entity.
- [func MIDIEntityGetDestination(MIDIEntityRef, Int) -> MIDIEndpointRef](./midientitygetdestination%28_,_%29.md)
  Returns one of an entity’s destinations.
- [typealias MIDIEntityRef](./midientityref.md)
  An entity that a device owns and that contains endpoints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midientitygetdevice(_:_:))*