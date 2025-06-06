# MIDISysexSendRequestUMP

**Framework**: Core MIDI  
**Kind**: struct

A request to asynchronously send a single universal MIDI packet (UMP) system-exclusive (SysEx) event to a destination.

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
struct MIDISysexSendRequestUMP
```

## Topics

### Creating a request
- [init(destination: MIDIEndpointRef, words: UnsafeMutablePointer<UInt32>, wordsToSend: UInt32, complete: DarwinBoolean, completionProc: MIDICompletionProcUMP, completionRefCon: UnsafeMutableRawPointer?)](midisysexsendrequestump/init(destination:words:wordstosend:complete:completionproc:completionrefcon:).md)
  Creates a new single universal MIDI packet (UMP) system-exclusive (SysEx) event request.
### Configuring and inspecting a request
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
- [func MIDIEventPacketSysexBytesForGroup(UnsafePointer<MIDIEventPacket>, UInt8, UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSStatus](midieventpacketsysexbytesforgroup(_:_:_:).md)
  Gets MIDI 1.0 system-exclusive (SysEx) bytes on the indicated group.
### Sending a request
- [func MIDISendUMPSysex(UnsafeMutablePointer<MIDISysexSendRequestUMP>) -> OSStatus](midisendumpsysex(_:).md)
  Asynchronously sends a single universal MIDI packet (UMP) system-exclusive (SysEx) event.
- [func MIDISendUMPSysex8(UnsafeMutablePointer<MIDISysexSendRequestUMP>) -> OSStatus](midisendumpsysex8(_:).md)
  Asynchronously sends a single universal MIDI packet (UMP) system-exclusive (SysEx) event with an 8-bit message.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [struct MIDISysexSendRequest](midisysexsendrequest.md)
  A request to asynchronously send a single system-exclusive (SysEx) event to a destination.
- [func MIDIFlushOutput(MIDIEndpointRef) -> OSStatus](midiflushoutput(_:).md)
  Cancels all pending events that were previously scheduled to send.
- [func MIDIRestart() -> OSStatus](midirestart().md)
  Stops and restarts MIDI I/O.
- [struct MIDIIOErrorNotification](midiioerrornotification.md)
  A general I/O error notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midisysexsendrequestump)*