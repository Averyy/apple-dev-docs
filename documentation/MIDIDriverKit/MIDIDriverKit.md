# MIDIDriverKit

**Framework**: MIDIDriverKit  
**Kind**: module

Develop drivers for MIDI devices.

**Availability**:
- DriverKit 24.0+

#### Overview

Use the MIDIDriverKit framework to implement a MIDI driver extension that communicates with Core MIDI. The framework handles all user-client communication between your driver extension and the Core MIDI server so you don’t need to implement a MIDI driver plug-in. You can also leverage other transport-based driver extension frameworks, such as [`USBDriverKit`](https://developer.apple.com/documentation/USBDriverKit), in your implementation.

## Topics

### Essentials
- [Creating a MIDI device driver](creating-a-midi-device-driver.md)
  Implement a configurable virtual MIDI driver as a driver extension that runs in user space in macOS and iPadOS.
- [com.apple.developer.driverkit.family.midi](../BundleResources/Entitlements/com.apple.developer.driverkit.family.midi.md)
  A Boolean value that indicates whether to match the driver against devices that support MIDI.
### Classes
- [IOUserMIDIDestination](iousermididestination.md)
- [IOUserMIDIDevice](iousermididevice.md)
- [IOUserMIDIDriver](iousermididriver.md)
- [IOUserMIDIEndpoint](iousermidiendpoint.md)
- [IOUserMIDIEntity](iousermidientity.md)
- [IOUserMIDIObject](iousermidiobject.md)
- [IOUserMIDISource](iousermidisource.md)
### Reference
- [MIDIDriverKit Constants](mididriverkit-constants.md)
- [MIDIDriverKit Data Types](mididriverkit-data-types.md)
### Namespaces
- [MIDIDriverKit](mididriverkit.md)
### Macros
- [kIOUserMIDIDriverUserClientType](kiousermididriveruserclienttype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/MIDIDriverKit)*