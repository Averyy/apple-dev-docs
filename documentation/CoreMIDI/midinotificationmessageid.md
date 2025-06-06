# MIDINotificationMessageID

**Framework**: Core MIDI  
**Kind**: enum

The types of state changes the system supports.

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
enum MIDINotificationMessageID
```

## Topics

### Change Types
- [MIDINotificationMessageID.msgSetupChanged](midinotificationmessageid/msgsetupchanged.md)
  Some aspect of the current MIDI setup changed.
- [MIDINotificationMessageID.msgObjectAdded](midinotificationmessageid/msgobjectadded.md)
  The system added a device, entity, or endpoint.
- [MIDINotificationMessageID.msgObjectRemoved](midinotificationmessageid/msgobjectremoved.md)
  The system removed a device, entity, or endpoint.
- [MIDINotificationMessageID.msgPropertyChanged](midinotificationmessageid/msgpropertychanged.md)
  An object’s property value changed.
- [MIDINotificationMessageID.msgThruConnectionsChanged](midinotificationmessageid/msgthruconnectionschanged.md)
  The system created or disposed of a persistent MIDI Thru connection.
- [MIDINotificationMessageID.msgSerialPortOwnerChanged](midinotificationmessageid/msgserialportownerchanged.md)
  The system changed a serial port owner.
- [MIDINotificationMessageID.msgIOError](midinotificationmessageid/msgioerror.md)
  A driver I/O error occurred.
### Enumeration Cases
- [MIDINotificationMessageID.msgInternalStart](midinotificationmessageid/msginternalstart.md)
### Initializers
- [init?(rawValue: Int32)](midinotificationmessageid/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var messageID: MIDINotificationMessageID](midinotification/messageid.md)
  An identifier that describes the type of state change.
- [var messageSize: UInt32](midinotification/messagesize.md)
  The size of the message including its ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midinotificationmessageid)*