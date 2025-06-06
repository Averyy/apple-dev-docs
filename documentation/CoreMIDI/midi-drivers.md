# MIDI Drivers

**Framework**: Core MIDI

Create driver plug-ins.

## Topics

### Managing Device Lifecyle
- [func MIDIDeviceCreate(MIDIDriverRef?, CFString, CFString, CFString, UnsafeMutablePointer<MIDIDeviceRef>) -> OSStatus](mididevicecreate(_:_:_:_:_:).md)
  Creates a new device object that corresponds to the available hardware.
- [func MIDIDeviceDispose(MIDIDeviceRef) -> OSStatus](mididevicedispose(_:).md)
  Disposes of a MIDI device.
- [typealias MIDIDeviceRef](midideviceref.md)
  A MIDI device that contains entities.
### Managing Device Lists
- [func MIDIDeviceListGetNumberOfDevices(MIDIDeviceListRef) -> Int](mididevicelistgetnumberofdevices(_:).md)
  Retrieves the number of devices in a device list.
- [func MIDIDeviceListGetDevice(MIDIDeviceListRef, Int) -> MIDIDeviceRef](mididevicelistgetdevice(_:_:).md)
  Retrieves a MIDI device from a device list.
- [func MIDIDeviceListAddDevice(MIDIDeviceListRef, MIDIDeviceRef) -> OSStatus](mididevicelistadddevice(_:_:).md)
  Adds the specified device to the device list.
- [func MIDIDeviceListDispose(MIDIDeviceListRef) -> OSStatus](mididevicelistdispose(_:).md)
  Disposes of a device list, but not its devices.
- [typealias MIDIDeviceListRef](mididevicelistref.md)
  A list of MIDI devices.
### Inspecting a Driver
- [func MIDIGetDriverDeviceList(MIDIDriverRef) -> MIDIDeviceListRef](midigetdriverdevicelist(_:).md)
  Returns the list of driver-created devices in the current MIDI setup.
- [func MIDIDriverEnableMonitoring(MIDIDriverRef, Bool) -> OSStatus](mididriverenablemonitoring(_:_:).md)
  Enables monitoring of all outgoing MIDI packets.
- [func MIDIGetDriverIORunLoop() -> Unmanaged<CFRunLoop>](midigetdriveriorunloop().md)
  Returns the server’s driver I/O thread.
- [let kMIDIDriverPropertyUsesSerial: CFString](kmididriverpropertyusesserial.md)
  A value that indicates whether the driver uses serial ports and is eligible to have serial ports assigned to it.
- [struct MIDIDriverInterface](mididriverinterface.md)
  The interface to a MIDI driver.
- [typealias MIDIDriverRef](mididriverref.md)
  A MIDI driver object.

## See Also

- [MIDI Services](midi-services.md)
  Communicate with hardware using Universal MIDI Packets.
- [MIDI System Setup](midi-system-setup.md)
  Configure the global MIDI system.
- [MIDI Bluetooth](midi-bluetooth.md)
  Connect to Bluetooth Low Energy MIDI peripherals.
- [MIDI Messages](midi-messages.md)
  Create and configure messages.
- [MIDI Thru Connection](midi-thru-connection.md)
  Create play-through connections between sources and destinations.
- [MIDI Networking](midi-networking.md)
  Create and manage devices connected over a local network.
- [MIDI Capability Inquiry](midi-capability-inquiry.md)
  Provide support for bidirectional discovery and configuration of devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midi-drivers)*