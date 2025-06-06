# MIDIIOErrorNotification

**Framework**: Core MIDI  
**Kind**: struct

A general I/O error notification.

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
struct MIDIIOErrorNotification
```

## Topics

### Creating an error notification
- [init()](midiioerrornotification/init.md)
- [init(messageID: MIDINotificationMessageID, messageSize: UInt32, driverDevice: MIDIDeviceRef, errorCode: OSStatus)](midiioerrornotification/init(messageid:messagesize:driverdevice:errorcode:).md)
### Inspecting an error notification
- [var messageID: MIDINotificationMessageID](midiioerrornotification/messageid.md)
  The type of message.
- [var messageSize: UInt32](midiioerrornotification/messagesize.md)
  The size of the message.
- [var driverDevice: MIDIDeviceRef](midiioerrornotification/driverdevice.md)
  The device with an I/O error.
- [var errorCode: OSStatus](midiioerrornotification/errorcode.md)
  The error code of the generated error.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct MIDISysexSendRequest](midisysexsendrequest.md)
  A request to asynchronously send a single system-exclusive (SysEx) event to a destination.
- [struct MIDISysexSendRequestUMP](midisysexsendrequestump.md)
  A request to asynchronously send a single universal MIDI packet (UMP) system-exclusive (SysEx) event to a destination.
- [func MIDIFlushOutput(MIDIEndpointRef) -> OSStatus](midiflushoutput(_:).md)
  Cancels all pending events that were previously scheduled to send.
- [func MIDIRestart() -> OSStatus](midirestart().md)
  Stops and restarts MIDI I/O.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midiioerrornotification)*