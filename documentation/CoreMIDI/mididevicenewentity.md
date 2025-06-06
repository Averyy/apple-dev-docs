# MIDIDeviceNewEntity(_:_:_:_:_:_:_:)

**Framework**: Core MIDI  
**Kind**: func

Adds a new entity to a device.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func MIDIDeviceNewEntity(_ device: MIDIDeviceRef, _ name: CFString, _ protocol: MIDIProtocolID, _ embedded: Bool, _ numSourceEndpoints: Int, _ numDestinationEndpoints: Int, _ newEntity: UnsafeMutablePointer<MIDIEntityRef>) -> OSStatus
```

#### Return Value

An `OSStatus` result code.

#### Discussion

Beginning with macOS 11 and iOS 14, non-drivers may call this function to add entities to external devices.

## Parameters

- `device`: The device that owns the new entity.
- `name`: The name of the new entity.
- `protocol`: The MIDI protocol variant used by the sources and destinations that make up this entity.
- `embedded`: A Boolean value that indicates whether this entity is inside the device. If you specify  , the entity consists only of external connectors to which you can attach other devices.
- `numSourceEndpoints`: The entity’s number of source endpoints.
- `numDestinationEndpoints`: The entity’s number of destination endpoints.
- `newEntity`: On successful return, points to the newly created entity.

## See Also

- [func MIDIDeviceRemoveEntity(MIDIDeviceRef, MIDIEntityRef) -> OSStatus](midideviceremoveentity(_:_:).md)
  Removes an entity from a device.
- [func MIDIEntityAddOrRemoveEndpoints(MIDIEntityRef, Int, Int) -> OSStatus](midientityaddorremoveendpoints(_:_:_:).md)
  Adds or removes an entity’s endpoints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/mididevicenewentity(_:_:_:_:_:_:_:))*