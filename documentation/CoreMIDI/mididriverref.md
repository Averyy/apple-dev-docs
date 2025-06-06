# MIDIDriverRef

**Framework**: Core MIDI  
**Kind**: typealias

A MIDI driver object.

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
typealias MIDIDriverRef = UnsafeMutablePointer<UnsafeMutablePointer<MIDIDriverInterface>>
```

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/mididriverref)*