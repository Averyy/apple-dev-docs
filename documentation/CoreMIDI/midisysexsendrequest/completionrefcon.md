# completionRefCon

**Framework**: Core MIDI  
**Kind**: property  
**Role**: Instance Property

Data to pass to the completion function.

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
var completionRefCon: UnsafeMutableRawPointer?
```

```c
void * completionRefCon;
```

## See Also

### Configuring a request
- [var destination: MIDIEndpointRef](./destination.md)
  The endpoint to send the event to.
- [var data: UnsafePointer<UInt8>](./data.md)
  The request’s data.
- [var bytesToSend: UInt32](./bytestosend.md)
  The number of bytes to send.
- [var complete: DarwinBoolean](./complete.md)
  A Boolean value that indicates whether the transmission is complete.
- [typealias MIDICompletionProc](../midicompletionproc.md)
  A function the system calls after it completely sends a system-exclusive (SysEx) event.
- [var completionProc: MIDICompletionProc](./completionproc.md)
  A function that the system calls after it sends all bytes for the request, or after the client marks the request as complete.
- [var reserved: (UInt8, UInt8, UInt8)](./reserved.md)
  A field that’s reserved for future use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midisysexsendrequest/completionrefcon)*