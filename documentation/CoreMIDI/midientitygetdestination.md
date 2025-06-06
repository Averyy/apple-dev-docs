# MIDIEntityGetDestination(_:_:)

**Framework**: Core MIDI  
**Kind**: func

Returns one of an entity’s destinations.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func MIDIEntityGetDestination(_ entity: MIDIEntityRef, _ destIndex0: Int) -> MIDIEndpointRef
```

#### Return Value

A reference to a destination, or `NULL` if an error occurred.

## Parameters

- `entity`: The entity to query.
- `destIndex0`: The destination index.

## See Also

- [func MIDIEntityGetDevice(MIDIEntityRef, UnsafeMutablePointer<MIDIDeviceRef>?) -> OSStatus](midientitygetdevice(_:_:).md)
  Returns an entity’s device.
- [func MIDIEntityGetNumberOfSources(MIDIEntityRef) -> Int](midientitygetnumberofsources(_:).md)
  Returns the number of sources in an entity.
- [func MIDIEntityGetSource(MIDIEntityRef, Int) -> MIDIEndpointRef](midientitygetsource(_:_:).md)
  Returns one of an entity’s sources.
- [func MIDIEntityGetNumberOfDestinations(MIDIEntityRef) -> Int](midientitygetnumberofdestinations(_:).md)
  Returns the number of destinations in an entity.
- [typealias MIDIEntityRef](midientityref.md)
  An entity that a device owns and that contains endpoints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midientitygetdestination(_:_:))*