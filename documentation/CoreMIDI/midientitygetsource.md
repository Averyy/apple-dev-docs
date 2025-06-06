# MIDIEntityGetSource(_:_:)

**Framework**: Core MIDI  
**Kind**: func

Returns one of an entity’s sources.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func MIDIEntityGetSource(_ entity: MIDIEntityRef, _ sourceIndex0: Int) -> MIDIEndpointRef
```

#### Return Value

A reference to a source, or `NULL` if an error occurred.

## Parameters

- `entity`: The entity to query.
- `sourceIndex0`: The source index.

## See Also

- [func MIDIEntityGetDevice(MIDIEntityRef, UnsafeMutablePointer<MIDIDeviceRef>?) -> OSStatus](midientitygetdevice(_:_:).md)
  Returns an entity’s device.
- [func MIDIEntityGetNumberOfSources(MIDIEntityRef) -> Int](midientitygetnumberofsources(_:).md)
  Returns the number of sources in an entity.
- [func MIDIEntityGetNumberOfDestinations(MIDIEntityRef) -> Int](midientitygetnumberofdestinations(_:).md)
  Returns the number of destinations in an entity.
- [func MIDIEntityGetDestination(MIDIEntityRef, Int) -> MIDIEndpointRef](midientitygetdestination(_:_:).md)
  Returns one of an entity’s destinations.
- [typealias MIDIEntityRef](midientityref.md)
  An entity that a device owns and that contains endpoints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midientitygetsource(_:_:))*