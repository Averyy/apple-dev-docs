# MIDINotification

**Framework**: Core MIDI  
**Kind**: struct

A message that describes a system state change.

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
struct MIDINotification
```

## Topics

### Inspecting the Notification
- [enum MIDINotificationMessageID](midinotificationmessageid.md)
  The types of state changes the system supports.
- [var messageID: MIDINotificationMessageID](midinotification/messageid.md)
  An identifier that describes the type of state change.
- [var messageSize: UInt32](midinotification/messagesize.md)
  The size of the message including its ID.
### Initializers
- [init()](midinotification/init.md)
- [init(messageID: MIDINotificationMessageID, messageSize: UInt32)](midinotification/init(messageid:messagesize:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [typealias MIDINotifyProc](midinotifyproc.md)
  A callback function for notifying clients of state changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midinotification)*