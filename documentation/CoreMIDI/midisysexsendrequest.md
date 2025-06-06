# MIDISysexSendRequest

**Framework**: Core MIDI  
**Kind**: struct

A request to asynchronously send a single system-exclusive (SysEx) event to a destination.

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
struct MIDISysexSendRequest
```

## Topics

### Creating a request
- [init(destination: MIDIEndpointRef, data: UnsafePointer<UInt8>, bytesToSend: UInt32, complete: DarwinBoolean, reserved: (UInt8, UInt8, UInt8), completionProc: MIDICompletionProc, completionRefCon: UnsafeMutableRawPointer?)](midisysexsendrequest/init(destination:data:bytestosend:complete:reserved:completionproc:completionrefcon:).md)
  Creates a new single system-exclusive (SysEx) event request.
### Configuring a request
- [var destination: MIDIEndpointRef](midisysexsendrequest/destination.md)
  The endpoint to send the event to.
- [var data: UnsafePointer<UInt8>](midisysexsendrequest/data.md)
  The request’s data.
- [var bytesToSend: UInt32](midisysexsendrequest/bytestosend.md)
  The number of bytes to send.
- [var complete: DarwinBoolean](midisysexsendrequest/complete.md)
  A Boolean value that indicates whether the transmission is complete.
- [typealias MIDICompletionProc](midicompletionproc.md)
  A function the system calls after it completely sends a system-exclusive (SysEx) event.
- [var completionProc: MIDICompletionProc](midisysexsendrequest/completionproc.md)
  A function that the system calls after it sends all bytes for the request, or after the client marks the request as complete.
- [var completionRefCon: UnsafeMutableRawPointer?](midisysexsendrequest/completionrefcon.md)
  Data to pass to the completion function.
- [var reserved: (UInt8, UInt8, UInt8)](midisysexsendrequest/reserved.md)
  A field that’s reserved for future use.
### Sending a request
- [func MIDISendSysex(UnsafeMutablePointer<MIDISysexSendRequest>) -> OSStatus](midisendsysex(_:).md)
  Asynchronously sends a single system-exclusive (SysEx) event.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [struct MIDISysexSendRequestUMP](midisysexsendrequestump.md)
  A request to asynchronously send a single universal MIDI packet (UMP) system-exclusive (SysEx) event to a destination.
- [func MIDIFlushOutput(MIDIEndpointRef) -> OSStatus](midiflushoutput(_:).md)
  Cancels all pending events that were previously scheduled to send.
- [func MIDIRestart() -> OSStatus](midirestart().md)
  Stops and restarts MIDI I/O.
- [struct MIDIIOErrorNotification](midiioerrornotification.md)
  A general I/O error notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midisysexsendrequest)*