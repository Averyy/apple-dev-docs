# MIDINotification

**Framework**: Core MIDI  
**Kind**: struct  
**Role**: Structure

A message that describes a system state change.

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
struct MIDINotification
```

```c
struct MIDINotification;
```

## Topics

### Inspecting the Notification
- [enum MIDINotificationMessageID](./midinotificationmessageid.md)
  The types of state changes the system supports.
- [var messageID: MIDINotificationMessageID](./midinotification/messageid.md)
  An identifier that describes the type of state change.
- [var messageSize: UInt32](./midinotification/messagesize.md)
  The size of the message including its ID.
### Initializers
- [init()](./midinotification/init%28%29.md)
- [init(messageID: MIDINotificationMessageID, messageSize: UInt32)](./midinotification/init%28messageid,messagesize%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Callbacks
- [typealias MIDINotifyProc](./midinotifyproc.md)
  A callback function for notifying clients of state changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midinotification)*