# MIDIDeviceDispose(_:)

**Framework**: Core MIDI  
**Kind**: func  
**Role**: Function

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

```c
extern OSStatus MIDIDeviceDispose(MIDIDeviceRef device);
```

#### Return Value

An `OSStatus` result code.

#### Discussion

Drivers may call this function to dispose of device objects that they haven’t already added to the system using [`MIDISetupAddDevice(_:)`](./midisetupadddevice%28_%29.md). To remove a device after adding it to the session, call [`MIDISetupRemoveDevice(_:)`](./midisetupremovedevice%28_%29.md).

Nondrivers can’t call this function, and instead must call [`MIDISetupAddDevice(_:)`](./midisetupadddevice%28_%29.md) and [`MIDISetupRemoveDevice(_:)`](./midisetupremovedevice%28_%29.md).

## Parameters

- `device`: The device to dispose.

## See Also

### Managing Device Lifecyle
- [func MIDIDeviceCreate(MIDIDriverRef?, CFString, CFString, CFString, UnsafeMutablePointer<MIDIDeviceRef>) -> OSStatus](./mididevicecreate%28_,_,_,_,_%29.md)
  Creates a new device object that corresponds to the available hardware.
- [typealias MIDIDeviceRef](./midideviceref.md)
  A MIDI device that contains entities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/mididevicedispose(_:))*