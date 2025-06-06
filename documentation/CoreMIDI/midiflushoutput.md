# MIDIFlushOutput(_:)

**Framework**: Core MIDI  
**Kind**: func

Cancels all pending events that were previously scheduled to send.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.1+
- visionOS 1.0+

## Declaration

```swift
func MIDIFlushOutput(_ dest: MIDIEndpointRef) -> OSStatus
```

#### Return Value

An `OSStatus` result code.

## Parameters

- `dest`: The destination with pending events to cancel. If  , the operation applies to all destinations.

## See Also

- [struct MIDISysexSendRequest](midisysexsendrequest.md)
  A request to asynchronously send a single system-exclusive (SysEx) event to a destination.
- [struct MIDISysexSendRequestUMP](midisysexsendrequestump.md)
  A request to asynchronously send a single universal MIDI packet (UMP) system-exclusive (SysEx) event to a destination.
- [func MIDIRestart() -> OSStatus](midirestart().md)
  Stops and restarts MIDI I/O.
- [struct MIDIIOErrorNotification](midiioerrornotification.md)
  A general I/O error notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midiflushoutput(_:))*