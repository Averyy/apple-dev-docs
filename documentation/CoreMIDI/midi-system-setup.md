# MIDI System Setup

**Framework**: Core MIDI  
**Role**: API Collection

Configure the global MIDI system.

## Overview

The primary clients of this API are apps that present a user interface to configure the global MIDI system, and MIDI drivers that dynamically modify the system state as users connect and disconnect hardware.

## Topics

### Managing Devices
- [func MIDISetupAddDevice(MIDIDeviceRef) -> OSStatus](./midisetupadddevice%28_%29.md)
  Adds a driver-owned MIDI device to the current MIDI setup.
- [func MIDISetupRemoveDevice(MIDIDeviceRef) -> OSStatus](./midisetupremovedevice%28_%29.md)
  Removes a driver-owned MIDI device from the current MIDI setup.
### Managing External Devices
- [func MIDIExternalDeviceCreate(CFString, CFString, CFString, UnsafeMutablePointer<MIDIDeviceRef>) -> OSStatus](./midiexternaldevicecreate%28_,_,_,_%29.md)
  Creates an external MIDI device.
- [func MIDISetupAddExternalDevice(MIDIDeviceRef) -> OSStatus](./midisetupaddexternaldevice%28_%29.md)
  Adds an external MIDI device to the current MIDI setup.
- [func MIDISetupRemoveExternalDevice(MIDIDeviceRef) -> OSStatus](./midisetupremoveexternaldevice%28_%29.md)
  Removes an external MIDI device from the current MIDI setup.
### Managing Entities
- [func MIDIDeviceNewEntity(MIDIDeviceRef, CFString, MIDIProtocolID, Bool, Int, Int, UnsafeMutablePointer<MIDIEntityRef>) -> OSStatus](./mididevicenewentity%28_,_,_,_,_,_,_%29.md)
  Adds a new entity to a device.
- [func MIDIDeviceRemoveEntity(MIDIDeviceRef, MIDIEntityRef) -> OSStatus](./midideviceremoveentity%28_,_%29.md)
  Removes an entity from a device.
- [func MIDIEntityAddOrRemoveEndpoints(MIDIEntityRef, Int, Int) -> OSStatus](./midientityaddorremoveendpoints%28_,_,_%29.md)
  Adds or removes an entity’s endpoints.
### Deprecated
- [Deprecated Symbols](./deprecated-symbols.md)
  Review unsupported symbols and their replacements.

## See Also

### Services
- [MIDI Services](./midi-services.md)
  Communicate with hardware using Universal MIDI Packets.
- [MIDI Bluetooth](./midi-bluetooth.md)
  Connect to Bluetooth Low Energy MIDI peripherals.
- [MIDI Messages](./midi-messages.md)
  Create and configure messages.
- [MIDI Thru Connection](./midi-thru-connection.md)
  Create play-through connections between sources and destinations.
- [MIDI Networking](./midi-networking.md)
  Create and manage devices connected over a local network.
- [MIDI Drivers](./midi-drivers.md)
  Create driver plug-ins.
- [MIDI Capability Inquiry](./midi-capability-inquiry.md)
  Provide support for bidirectional discovery and configuration of devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midi-system-setup)*