# MIDINotificationMessageID.msgObjectRemoved

**Framework**: Core MIDI  
**Kind**: case

The system removed a device, entity, or endpoint.

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
case msgObjectRemoved
```

#### Discussion

This type’s data is [`MIDIObjectAddRemoveNotification`](midiobjectaddremovenotification.md).

## See Also

- [MIDINotificationMessageID.msgSetupChanged](midinotificationmessageid/msgsetupchanged.md)
  Some aspect of the current MIDI setup changed.
- [MIDINotificationMessageID.msgObjectAdded](midinotificationmessageid/msgobjectadded.md)
  The system added a device, entity, or endpoint.
- [MIDINotificationMessageID.msgPropertyChanged](midinotificationmessageid/msgpropertychanged.md)
  An object’s property value changed.
- [MIDINotificationMessageID.msgThruConnectionsChanged](midinotificationmessageid/msgthruconnectionschanged.md)
  The system created or disposed of a persistent MIDI Thru connection.
- [MIDINotificationMessageID.msgSerialPortOwnerChanged](midinotificationmessageid/msgserialportownerchanged.md)
  The system changed a serial port owner.
- [MIDINotificationMessageID.msgIOError](midinotificationmessageid/msgioerror.md)
  A driver I/O error occurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midinotificationmessageid/msgobjectremoved)*