# words

**Framework**: Core MIDI  
**Kind**: property  
**Role**: Instance Property

A pointer to the event to send, which the system advances as it sends the data.

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
var words: UnsafeMutablePointer<UInt32>
```

```c
UInt32 * words;
```

## See Also

### Configuring and inspecting a request
- [var destination: MIDIEndpointRef](./destination.md)
  The endpoint to send the event to.
- [var wordsToSend: UInt32](./wordstosend.md)
  A counter of the number of words to send.
- [var complete: DarwinBoolean](./complete.md)
  A Boolean value that indicates whether the transmission is complete.
- [typealias MIDICompletionProcUMP](../midicompletionprocump.md)
  A function the system calls after it completely sends a UMP system-exclusive (SysEx) or SysEx 8-bit event.
- [var completionProc: MIDICompletionProcUMP](./completionproc.md)
  A function that the system calls after it sends all data for the request, or after the client marks the request as complete.
- [var completionRefCon: UnsafeMutableRawPointer?](./completionrefcon.md)
  Data to pass to the completion function.
- [func MIDIEventPacketSysexBytesForGroup(UnsafePointer<MIDIEventPacket>, UInt8, UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSStatus](../midieventpacketsysexbytesforgroup%28_,_,_%29.md)
  Gets MIDI 1.0 system-exclusive (SysEx) bytes on the indicated group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midisysexsendrequestump/words)*