# MIDIIOErrorNotification

**Framework**: Core MIDI  
**Kind**: struct  
**Role**: Structure

A general I/O error notification.

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
struct MIDIIOErrorNotification
```

```c
struct MIDIIOErrorNotification;
```

## Topics

### Creating an error notification
- [init()](./midiioerrornotification/init%28%29.md)
- [init(messageID: MIDINotificationMessageID, messageSize: UInt32, driverDevice: MIDIDeviceRef, errorCode: OSStatus)](./midiioerrornotification/init%28messageid,messagesize,driverdevice,errorcode%29.md)
### Inspecting an error notification
- [var messageID: MIDINotificationMessageID](./midiioerrornotification/messageid.md)
  The type of message.
- [var messageSize: UInt32](./midiioerrornotification/messagesize.md)
  The size of the message.
- [var driverDevice: MIDIDeviceRef](./midiioerrornotification/driverdevice.md)
  The device with an I/O error.
- [var errorCode: OSStatus](./midiioerrornotification/errorcode.md)
  The error code of the generated error.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### I/O management
- [struct MIDISysexSendRequest](./midisysexsendrequest.md)
  A request to asynchronously send a single system-exclusive (SysEx) event to a destination.
- [struct MIDISysexSendRequestUMP](./midisysexsendrequestump.md)
  A request to asynchronously send a single universal MIDI packet (UMP) system-exclusive (SysEx) event to a destination.
- [func MIDIFlushOutput(MIDIEndpointRef) -> OSStatus](./midiflushoutput%28_%29.md)
  Cancels all pending events that were previously scheduled to send.
- [func MIDIRestart() -> OSStatus](./midirestart%28%29.md)
  Stops and restarts MIDI I/O.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midiioerrornotification)*