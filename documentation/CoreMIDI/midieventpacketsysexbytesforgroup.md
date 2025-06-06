# MIDIEventPacketSysexBytesForGroup(_:_:_:)

**Framework**: Core MIDI  
**Kind**: func

Gets MIDI 1.0 system-exclusive (SysEx) bytes on the indicated group.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func MIDIEventPacketSysexBytesForGroup(_ pkt: UnsafePointer<MIDIEventPacket>, _ groupIndex: UInt8, _ outData: UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSStatus
```

#### Return Value

An `OSStatus` result code.

## Parameters

- `pkt`: A   that contains universal MIDI packet (UMP) SysEx data.
- `groupIndex`: The target group index, from   to  .
- `outData`: When successful, a reference byte stream of extracted SysEx data.

## See Also

- [var destination: MIDIEndpointRef](midisysexsendrequestump/destination.md)
  The endpoint to send the event to.
- [var words: UnsafeMutablePointer<UInt32>](midisysexsendrequestump/words.md)
  A pointer to the event to send, which the system advances as it sends the data.
- [var wordsToSend: UInt32](midisysexsendrequestump/wordstosend.md)
  A counter of the number of words to send.
- [var complete: DarwinBoolean](midisysexsendrequestump/complete.md)
  A Boolean value that indicates whether the transmission is complete.
- [typealias MIDICompletionProcUMP](midicompletionprocump.md)
  A function the system calls after it completely sends a UMP system-exclusive (SysEx) or SysEx 8-bit event.
- [var completionProc: MIDICompletionProcUMP](midisysexsendrequestump/completionproc.md)
  A function that the system calls after it sends all data for the request, or after the client marks the request as complete.
- [var completionRefCon: UnsafeMutableRawPointer?](midisysexsendrequestump/completionrefcon.md)
  Data to pass to the completion function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midieventpacketsysexbytesforgroup(_:_:_:))*