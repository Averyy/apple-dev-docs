# MIDIEntityGetDevice(_:_:)

**Framework**: Core MIDI  
**Kind**: func

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

#### Return Value

An `OSStatus` result code.

## Parameters

- `inEntity`: The entity to query.
- `outDevice`: On successful return, the entity’s owning device.

## See Also

- [func MIDIEntityGetNumberOfSources(MIDIEntityRef) -> Int](midientitygetnumberofsources(_:).md)
  Returns the number of sources in an entity.
- [func MIDIEntityGetSource(MIDIEntityRef, Int) -> MIDIEndpointRef](midientitygetsource(_:_:).md)
  Returns one of an entity’s sources.
- [func MIDIEntityGetNumberOfDestinations(MIDIEntityRef) -> Int](midientitygetnumberofdestinations(_:).md)
  Returns the number of destinations in an entity.
- [func MIDIEntityGetDestination(MIDIEntityRef, Int) -> MIDIEndpointRef](midientitygetdestination(_:_:).md)
  Returns one of an entity’s destinations.
- [typealias MIDIEntityRef](midientityref.md)
  An entity that a device owns and that contains endpoints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midientitygetdevice(_:_:))*