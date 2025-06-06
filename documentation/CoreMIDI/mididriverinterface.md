# MIDIDriverInterface

**Framework**: Core MIDI  
**Kind**: struct

The interface to a MIDI driver.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct MIDIDriverInterface
```

## Topics

### Properties
- [var FindDevices: (MIDIDriverRef, MIDIDeviceListRef) -> OSStatus](mididriverinterface/finddevices.md)
  Finds the available devices.
- [var Start: (MIDIDriverRef, MIDIDeviceListRef) -> OSStatus](mididriverinterface/start.md)
  Starts MIDI I/O.
- [var Stop: (MIDIDriverRef) -> OSStatus](mididriverinterface/stop.md)
  Stops MIDI I/O.
- [var Configure: (MIDIDriverRef, MIDIDeviceRef) -> OSStatus](mididriverinterface/configure.md)
  The system doesn’t currently use this method.
- [var Send: (MIDIDriverRef, UnsafePointer<MIDIPacketList>, UnsafeMutableRawPointer, UnsafeMutableRawPointer) -> OSStatus](mididriverinterface/send.md)
  Sends a MIDI packet list to the specified destination endpoints.
- [var EnableSource: (MIDIDriverRef, MIDIEndpointRef, DarwinBoolean) -> OSStatus](mididriverinterface/enablesource.md)
  Tells the driver whether input from a particular source has listeners.
- [var Flush: (MIDIDriverRef, MIDIEndpointRef, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> OSStatus](mididriverinterface/flush.md)
  Unschedules all pending output to the specified destination.
- [var Monitor: (MIDIDriverRef, MIDIEndpointRef, UnsafePointer<MIDIPacketList>) -> OSStatus](mididriverinterface/monitor.md)
  Enables monitoring of MIDI packet lists by the specified driver.
- [var MonitorEvents: (MIDIDriverRef, MIDIEndpointRef, UnsafePointer<MIDIEventList>) -> OSStatus](mididriverinterface/monitorevents.md)
  Enables monitoring of MIDI event lists by the specified driver.
- [var SendPackets: (MIDIDriverRef, UnsafePointer<MIDIEventList>, UnsafeMutableRawPointer, UnsafeMutableRawPointer) -> OSStatus](mididriverinterface/sendpackets.md)
  Sends a MIDI event list to the specified destination endpoints.
- [var AddRef: (UnsafeMutableRawPointer) -> ULONG](mididriverinterface/addref.md)
- [var QueryInterface: (UnsafeMutableRawPointer, REFIID, UnsafeMutablePointer<LPVOID?>?) -> HRESULT](mididriverinterface/queryinterface.md)
- [var Release: (UnsafeMutableRawPointer) -> ULONG](mididriverinterface/release.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [func MIDIGetDriverDeviceList(MIDIDriverRef) -> MIDIDeviceListRef](midigetdriverdevicelist(_:).md)
  Returns the list of driver-created devices in the current MIDI setup.
- [func MIDIDriverEnableMonitoring(MIDIDriverRef, Bool) -> OSStatus](mididriverenablemonitoring(_:_:).md)
  Enables monitoring of all outgoing MIDI packets.
- [func MIDIGetDriverIORunLoop() -> Unmanaged<CFRunLoop>](midigetdriveriorunloop().md)
  Returns the server’s driver I/O thread.
- [let kMIDIDriverPropertyUsesSerial: CFString](kmididriverpropertyusesserial.md)
  A value that indicates whether the driver uses serial ports and is eligible to have serial ports assigned to it.
- [typealias MIDIDriverRef](mididriverref.md)
  A MIDI driver object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/mididriverinterface)*