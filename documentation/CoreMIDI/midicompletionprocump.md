# MIDICompletionProcUMP

**Framework**: Core MIDI  
**Kind**: typealias

A function the system calls after it completely sends a UMP system-exclusive (SysEx) or SysEx 8-bit event.

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
typealias MIDICompletionProcUMP = (UnsafeMutablePointer<MIDISysexSendRequestUMP>) -> Void
```

## Parameters

- `request`: The completed or aborted request.

## See Also

- [var destination: MIDIEndpointRef](midisysexsendrequestump/destination.md)
  The endpoint to send the event to.
- [var words: UnsafeMutablePointer<UInt32>](midisysexsendrequestump/words.md)
  A pointer to the event to send, which the system advances as it sends the data.
- [var wordsToSend: UInt32](midisysexsendrequestump/wordstosend.md)
  A counter of the number of words to send.
- [var complete: DarwinBoolean](midisysexsendrequestump/complete.md)
  A Boolean value that indicates whether the transmission is complete.
- [var completionProc: MIDICompletionProcUMP](midisysexsendrequestump/completionproc.md)
  A function that the system calls after it sends all data for the request, or after the client marks the request as complete.
- [var completionRefCon: UnsafeMutableRawPointer?](midisysexsendrequestump/completionrefcon.md)
  Data to pass to the completion function.
- [func MIDIEventPacketSysexBytesForGroup(UnsafePointer<MIDIEventPacket>, UInt8, UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSStatus](midieventpacketsysexbytesforgroup(_:_:_:).md)
  Gets MIDI 1.0 system-exclusive (SysEx) bytes on the indicated group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midicompletionprocump)*