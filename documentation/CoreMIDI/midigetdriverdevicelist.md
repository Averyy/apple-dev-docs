# MIDIGetDriverDeviceList(_:)

**Framework**: Core MIDI  
**Kind**: func

Returns the list of driver-created devices in the current MIDI setup.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.1+
- visionOS 1.0+

## Declaration

```swift
func MIDIGetDriverDeviceList(_ driver: MIDIDriverRef) -> MIDIDeviceListRef
```

#### Return Value

The requested device list.

#### Discussion

Dispose this list when you’re finished working with it by calling [`MIDIDeviceListDispose(_:)`](mididevicelistdispose(_:).md).

## Parameters

- `driver`: The driver for which you return devices.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midigetdriverdevicelist(_:))*