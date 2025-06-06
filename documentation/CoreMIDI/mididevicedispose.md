# MIDIDeviceDispose(_:)

**Framework**: Core MIDI  
**Kind**: func

Disposes of a MIDI device.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.3+
- visionOS 1.0+

## Declaration

```swift
func MIDIDeviceDispose(_ device: MIDIDeviceRef) -> OSStatus
```

#### Return Value

An `OSStatus` result code.

#### Discussion

Drivers may call this function to dispose of device objects that they haven’t already added to the system using [`MIDISetupAddDevice(_:)`](midisetupadddevice(_:).md). To remove a device after adding it to the session, call [`MIDISetupRemoveDevice(_:)`](midisetupremovedevice(_:).md).

Nondrivers can’t call this function, and instead must call [`MIDISetupAddDevice(_:)`](midisetupadddevice(_:).md) and [`MIDISetupRemoveDevice(_:)`](midisetupremovedevice(_:).md).

## Parameters

- `device`: The device to dispose.

## See Also

- [func MIDIDeviceCreate(MIDIDriverRef?, CFString, CFString, CFString, UnsafeMutablePointer<MIDIDeviceRef>) -> OSStatus](mididevicecreate(_:_:_:_:_:).md)
  Creates a new device object that corresponds to the available hardware.
- [typealias MIDIDeviceRef](midideviceref.md)
  A MIDI device that contains entities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/mididevicedispose(_:))*