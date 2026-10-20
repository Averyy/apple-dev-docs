# EnableSource

**Framework**: Core MIDI  
**Kind**: property  
**Role**: Instance Property

Tells the driver whether input from a particular source has listeners.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
var EnableSource: (MIDIDriverRef, MIDIEndpointRef, DarwinBoolean) -> OSStatus
```

```c
int (*)(struct MIDIDriverInterface **, unsigned int, unsigned char) EnableSource;
```

## See Also

### Properties
- [var FindDevices: (MIDIDriverRef, MIDIDeviceListRef) -> OSStatus](./finddevices.md)
  Finds the available devices.
- [var Start: (MIDIDriverRef, MIDIDeviceListRef) -> OSStatus](./start.md)
  Starts MIDI I/O.
- [var Stop: (MIDIDriverRef) -> OSStatus](./stop.md)
  Stops MIDI I/O.
- [var Configure: (MIDIDriverRef, MIDIDeviceRef) -> OSStatus](./configure.md)
  The system doesn’t currently use this method.
- [var Send: (MIDIDriverRef, UnsafePointer<MIDIPacketList>, UnsafeMutableRawPointer, UnsafeMutableRawPointer) -> OSStatus](./send.md)
  Sends a MIDI packet list to the specified destination endpoints.
- [var Flush: (MIDIDriverRef, MIDIEndpointRef, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> OSStatus](./flush.md)
  Unschedules all pending output to the specified destination.
- [var Monitor: (MIDIDriverRef, MIDIEndpointRef, UnsafePointer<MIDIPacketList>) -> OSStatus](./monitor.md)
  Enables monitoring of MIDI packet lists by the specified driver.
- [var MonitorEvents: (MIDIDriverRef, MIDIEndpointRef, UnsafePointer<MIDIEventList>) -> OSStatus](./monitorevents.md)
  Enables monitoring of MIDI event lists by the specified driver.
- [var SendPackets: (MIDIDriverRef, UnsafePointer<MIDIEventList>, UnsafeMutableRawPointer, UnsafeMutableRawPointer) -> OSStatus](./sendpackets.md)
  Sends a MIDI event list to the specified destination endpoints.
- [var AddRef: (UnsafeMutableRawPointer) -> ULONG](./addref.md)
- [var QueryInterface: (UnsafeMutableRawPointer, REFIID, UnsafeMutablePointer<LPVOID?>?) -> HRESULT](./queryinterface.md)
- [var Release: (UnsafeMutableRawPointer) -> ULONG](./release.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/mididriverinterface/enablesource)*