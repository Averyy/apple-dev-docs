# MIDI System Setup

**Framework**: Core MIDI

Configure the global MIDI system.

#### Overview

The primary clients of this API are apps that present a user interface to configure the global MIDI system, and MIDI drivers that dynamically modify the system state as users connect and disconnect hardware.

## Topics

### Managing Devices
- [func MIDISetupAddDevice(MIDIDeviceRef) -> OSStatus](midisetupadddevice(_:).md)
  Adds a driver-owned MIDI device to the current MIDI setup.
- [func MIDISetupRemoveDevice(MIDIDeviceRef) -> OSStatus](midisetupremovedevice(_:).md)
  Removes a driver-owned MIDI device from the current MIDI setup.
### Managing External Devices
- [func MIDIExternalDeviceCreate(CFString, CFString, CFString, UnsafeMutablePointer<MIDIDeviceRef>) -> OSStatus](midiexternaldevicecreate(_:_:_:_:).md)
  Creates an external MIDI device.
- [func MIDISetupAddExternalDevice(MIDIDeviceRef) -> OSStatus](midisetupaddexternaldevice(_:).md)
  Adds an external MIDI device to the current MIDI setup.
- [func MIDISetupRemoveExternalDevice(MIDIDeviceRef) -> OSStatus](midisetupremoveexternaldevice(_:).md)
  Removes an external MIDI device from the current MIDI setup.
### Managing Entities
- [func MIDIDeviceNewEntity(MIDIDeviceRef, CFString, MIDIProtocolID, Bool, Int, Int, UnsafeMutablePointer<MIDIEntityRef>) -> OSStatus](mididevicenewentity(_:_:_:_:_:_:_:).md)
  Adds a new entity to a device.
- [func MIDIDeviceRemoveEntity(MIDIDeviceRef, MIDIEntityRef) -> OSStatus](midideviceremoveentity(_:_:).md)
  Removes an entity from a device.
- [func MIDIEntityAddOrRemoveEndpoints(MIDIEntityRef, Int, Int) -> OSStatus](midientityaddorremoveendpoints(_:_:_:).md)
  Adds or removes an entity’s endpoints.
### Deprecated
- [Deprecated Symbols](deprecated-symbols.md)
  Review unsupported symbols and their replacements.

## See Also

- [MIDI Services](midi-services.md)
  Communicate with hardware using Universal MIDI Packets.
- [MIDI Bluetooth](midi-bluetooth.md)
  Connect to Bluetooth Low Energy MIDI peripherals.
- [MIDI Messages](midi-messages.md)
  Create and configure messages.
- [MIDI Thru Connection](midi-thru-connection.md)
  Create play-through connections between sources and destinations.
- [MIDI Networking](midi-networking.md)
  Create and manage devices connected over a local network.
- [MIDI Drivers](midi-drivers.md)
  Create driver plug-ins.
- [MIDI Capability Inquiry](midi-capability-inquiry.md)
  Provide support for bidirectional discovery and configuration of devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midi-system-setup)*