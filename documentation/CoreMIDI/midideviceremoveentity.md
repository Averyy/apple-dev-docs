# MIDIDeviceRemoveEntity(_:_:)

**Framework**: Core MIDI  
**Kind**: func

Removes an entity from a device.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.1+
- visionOS 1.0+

## Declaration

```swift
func MIDIDeviceRemoveEntity(_ device: MIDIDeviceRef, _ entity: MIDIEntityRef) -> OSStatus
```

#### Return Value

An `OSStatus` result code.

#### Discussion

Drivers call this function to remove one of a device’s entities.

## Parameters

- `device`: The device to update.
- `entity`: The entity to remove.

## See Also

- [func MIDIDeviceNewEntity(MIDIDeviceRef, CFString, MIDIProtocolID, Bool, Int, Int, UnsafeMutablePointer<MIDIEntityRef>) -> OSStatus](mididevicenewentity(_:_:_:_:_:_:_:).md)
  Adds a new entity to a device.
- [func MIDIEntityAddOrRemoveEndpoints(MIDIEntityRef, Int, Int) -> OSStatus](midientityaddorremoveendpoints(_:_:_:).md)
  Adds or removes an entity’s endpoints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midideviceremoveentity(_:_:))*