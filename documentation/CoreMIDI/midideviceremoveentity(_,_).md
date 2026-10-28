# MIDIDeviceRemoveEntity(_:_:)

**Framework**: Core MIDI  
**Kind**: func  
**Role**: Function

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

```c
extern OSStatus MIDIDeviceRemoveEntity(MIDIDeviceRef device, MIDIEntityRef entity);
```

## Return Value

An `OSStatus` result code.

## Discussion

Drivers call this function to remove one of a device’s entities.

## Parameters

- `device`: The device to update.
- `entity`: The entity to remove.

## See Also

### Managing Entities
- [func MIDIDeviceNewEntity(MIDIDeviceRef, CFString, MIDIProtocolID, Bool, Int, Int, UnsafeMutablePointer<MIDIEntityRef>) -> OSStatus](./mididevicenewentity%28_,_,_,_,_,_,_%29.md)
  Adds a new entity to a device.
- [func MIDIEntityAddOrRemoveEndpoints(MIDIEntityRef, Int, Int) -> OSStatus](./midientityaddorremoveendpoints%28_,_,_%29.md)
  Adds or removes an entity’s endpoints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midideviceremoveentity(_:_:))*