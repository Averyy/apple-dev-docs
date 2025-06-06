# MIDIRestart()

**Framework**: Core MIDI  
**Kind**: func

Stops and restarts MIDI I/O.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.1+
- visionOS 1.0+

## Declaration

```swift
func MIDIRestart() -> OSStatus
```

#### Return Value

An `OSStatus` result code.

#### Discussion

Call this function to force Core MIDI to ask its drivers to rescan for hardware.

## See Also

- [struct MIDISysexSendRequest](midisysexsendrequest.md)
  A request to asynchronously send a single system-exclusive (SysEx) event to a destination.
- [struct MIDISysexSendRequestUMP](midisysexsendrequestump.md)
  A request to asynchronously send a single universal MIDI packet (UMP) system-exclusive (SysEx) event to a destination.
- [func MIDIFlushOutput(MIDIEndpointRef) -> OSStatus](midiflushoutput(_:).md)
  Cancels all pending events that were previously scheduled to send.
- [struct MIDIIOErrorNotification](midiioerrornotification.md)
  A general I/O error notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midirestart())*