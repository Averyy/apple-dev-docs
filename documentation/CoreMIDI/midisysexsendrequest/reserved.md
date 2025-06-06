# reserved

**Framework**: Core MIDI  
**Kind**: property

A field that’s reserved for future use.

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
var reserved: (UInt8, UInt8, UInt8)
```

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midisysexsendrequest/reserved)*