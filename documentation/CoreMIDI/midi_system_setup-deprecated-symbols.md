# Deprecated Symbols

**Framework**: Core MIDI  
**Role**: API Collection

Review unsupported symbols and their replacements.

## Topics

### Managing System Setup
- [typealias MIDISetupRef](./midisetupref.md)
  A type that represents the global state of the MIDI system, that contains lists of the devices and serial port owners.
- [MIDISetupCreate](./midisetupcreate.md)
  Queries drivers to discover what hardware is available.
- [MIDISetupDispose](./midisetupdispose.md)
  Disposes the specified setup object.
- [MIDISetupFromData](./midisetupfromdata.md)
  Creates a MIDISetup object from an XML stream.
- [MIDISetupGetCurrent](./midisetupgetcurrent.md)
  Returns the system’s current MIDISetup.
- [MIDISetupInstall](./midisetupinstall.md)
  Installs a MIDISetup as the system’s current state.
- [MIDISetupToData](./midisetuptodata.md)
  Creates an XML representation of a MIDISetup object.
### Managing MIDI Devices
- [func MIDIDeviceAddEntity(MIDIDeviceRef, CFString, Bool, Int, Int, UnsafeMutablePointer<MIDIEntityRef>) -> OSStatus](./midideviceaddentity%28_,_,_,_,_,_%29.md)
  Specifies one of the entities that make up a device.
### Managing Serial Ports
- [MIDIGetSerialPortOwner](./midigetserialportowner.md)
  Returns the MIDI driver that owns a serial port.
- [MIDISetSerialPortOwner](./midisetserialportowner.md)
  Specifies the MIDI driver that owns a serial port.
- [MIDIGetSerialPortDrivers](./midigetserialportdrivers.md)
  Returns a list of installed MIDI drivers for serial port MIDI devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midi_system_setup-deprecated-symbols)*