# MIDIDriverEnableMonitoring(_:_:)

**Framework**: Core MIDI  
**Kind**: func  
**Role**: Function

Enables monitoring of all outgoing MIDI packets.

**Availability**:
- macOS 10.1+

## Declaration

```swift
func MIDIDriverEnableMonitoring(_ driver: MIDIDriverRef, _ enabled: Bool) -> OSStatus
```

```c
extern OSStatus MIDIDriverEnableMonitoring(MIDIDriverRef driver, Boolean enabled);
```

#### Return Value

An `OSStatus` result code.

#### Discussion

Some specialized drivers, like a MIDI monitor display, can intercept and inspect all outgoing MIDI messages. Enablng monitoring causes the system to call the [`Monitor`](./mididriverinterface/monitor.md) function with the outgoing MIDI packets for all destinations in the system. The [`Monitor`](./mididriverinterface/monitor.md) function can’t rely on the MIDI events arriving in order, due to the MIDI server’s schedule-ahead facilities.

## Parameters

- `driver`: The driver for which to enable monitoring.
- `enabled`: A Boolean value that indicates whether to enable monitoring.

## See Also

### Inspecting a Driver
- [func MIDIGetDriverDeviceList(MIDIDriverRef) -> MIDIDeviceListRef](./midigetdriverdevicelist%28_%29.md)
  Returns the list of driver-created devices in the current MIDI setup.
- [func MIDIGetDriverIORunLoop() -> Unmanaged<CFRunLoop>](./midigetdriveriorunloop%28%29.md)
  Returns the server’s driver I/O thread.
- [let kMIDIDriverPropertyUsesSerial: CFString](./kmididriverpropertyusesserial.md)
  A value that indicates whether the driver uses serial ports and is eligible to have serial ports assigned to it.
- [struct MIDIDriverInterface](./mididriverinterface.md)
  The interface to a MIDI driver.
- [typealias MIDIDriverRef](./mididriverref.md)
  A MIDI driver object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/mididriverenablemonitoring(_:_:))*