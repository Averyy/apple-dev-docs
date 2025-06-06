# kMIDIDriverPropertyUsesSerial

**Framework**: Core MIDI  
**Kind**: var

A value that indicates whether the driver uses serial ports and is eligible to have serial ports assigned to it.

**Availability**:
- macOS 10.1+

## Declaration

```swift
let kMIDIDriverPropertyUsesSerial: CFString
```

## See Also

- [func MIDIGetDriverDeviceList(MIDIDriverRef) -> MIDIDeviceListRef](midigetdriverdevicelist(_:).md)
  Returns the list of driver-created devices in the current MIDI setup.
- [func MIDIDriverEnableMonitoring(MIDIDriverRef, Bool) -> OSStatus](mididriverenablemonitoring(_:_:).md)
  Enables monitoring of all outgoing MIDI packets.
- [func MIDIGetDriverIORunLoop() -> Unmanaged<CFRunLoop>](midigetdriveriorunloop().md)
  Returns the server’s driver I/O thread.
- [struct MIDIDriverInterface](mididriverinterface.md)
  The interface to a MIDI driver.
- [typealias MIDIDriverRef](mididriverref.md)
  A MIDI driver object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/kmididriverpropertyusesserial)*