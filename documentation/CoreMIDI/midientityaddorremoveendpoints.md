# MIDIEntityAddOrRemoveEndpoints(_:_:_:)

**Framework**: Core MIDI  
**Kind**: func

Adds or removes an entity’s endpoints.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.2+
- visionOS 1.0+

## Declaration

```swift
func MIDIEntityAddOrRemoveEndpoints(_ entity: MIDIEntityRef, _ numSourceEndpoints: Int, _ numDestinationEndpoints: Int) -> OSStatus
```

#### Return Value

An `OSStatus` result code.

#### Discussion

Drivers and configuration editors may call this function to add to or remove an entity’s endpoints. The [`MIDIProtocolID`](midiprotocolid.md) of new endpoints is initially the same as that of the entity.

## Parameters

- `entity`: The entity to update.
- `numSourceEndpoints`: The number of source endpoints.
- `numDestinationEndpoints`: The number of destination endpoints.

## See Also

- [func MIDIDeviceNewEntity(MIDIDeviceRef, CFString, MIDIProtocolID, Bool, Int, Int, UnsafeMutablePointer<MIDIEntityRef>) -> OSStatus](mididevicenewentity(_:_:_:_:_:_:_:).md)
  Adds a new entity to a device.
- [func MIDIDeviceRemoveEntity(MIDIDeviceRef, MIDIEntityRef) -> OSStatus](midideviceremoveentity(_:_:).md)
  Removes an entity from a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midientityaddorremoveendpoints(_:_:_:))*