# data

**Framework**: Core MIDI  
**Kind**: property

The request’s data.

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
var data: UnsafePointer<UInt8>
```

#### Discussion

Initially, the value is a pointer to the System Exclusive (SysEx) event to send. [`MIDISendSysex(_:)`](midisendsysex(_:).md) advances this pointer as it sends bytes.

## See Also

- [var destination: MIDIEndpointRef](midisysexsendrequest/destination.md)
  The endpoint to send the event to.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midisysexsendrequest/data)*