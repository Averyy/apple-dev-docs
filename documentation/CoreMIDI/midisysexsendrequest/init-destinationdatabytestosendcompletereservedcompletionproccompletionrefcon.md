# init(destination:data:bytesToSend:complete:reserved:completionProc:completionRefCon:)

**Framework**: Core MIDI  
**Kind**: init

Creates a new single system-exclusive (SysEx) event request.

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
init(destination: MIDIEndpointRef, data: UnsafePointer<UInt8>, bytesToSend: UInt32, complete: DarwinBoolean, reserved: (UInt8, UInt8, UInt8), completionProc: MIDICompletionProc, completionRefCon: UnsafeMutableRawPointer?)
```

## Parameters

- `destination`: The endpoint to send the event to.
- `data`: Initially, a pointer to the SysEx event to send. The system advances this pointer as it sends the bytes.
- `bytesToSend`: Initially, a counter of the number of bytes to send. The system decrements this counter as it sends the bytes.
- `complete`: A Boolean value that indicates whether the transmission is complete. You can set this value to   to abort transmission and the system sets it to   after it transmits all the bytes.
- `reserved`: 
- `completionProc`: A function that the system calls after it sends all bytes for the request, or after the client marks the request as complete.
- `completionRefCon`: Data to pass to the  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midisysexsendrequest/init(destination:data:bytestosend:complete:reserved:completionproc:completionrefcon:))*