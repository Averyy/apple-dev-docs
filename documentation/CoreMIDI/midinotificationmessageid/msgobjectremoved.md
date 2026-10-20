# MIDINotificationMessageID.msgObjectRemoved

**Framework**: Core MIDI  
**Kind**: case  
**Role**: Case

The system removed a device, entity, or endpoint.

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
case msgObjectRemoved
```

```c
kMIDIMsgObjectRemoved
```

#### Discussion

This type’s data is [`MIDIObjectAddRemoveNotification`](../midiobjectaddremovenotification.md).

## See Also

### Change Types
- [MIDINotificationMessageID.msgSetupChanged](./msgsetupchanged.md)
  Some aspect of the current MIDI setup changed.
- [MIDINotificationMessageID.msgObjectAdded](./msgobjectadded.md)
  The system added a device, entity, or endpoint.
- [MIDINotificationMessageID.msgPropertyChanged](./msgpropertychanged.md)
  An object’s property value changed.
- [MIDINotificationMessageID.msgThruConnectionsChanged](./msgthruconnectionschanged.md)
  The system created or disposed of a persistent MIDI Thru connection.
- [MIDINotificationMessageID.msgSerialPortOwnerChanged](./msgserialportownerchanged.md)
  The system changed a serial port owner.
- [MIDINotificationMessageID.msgIOError](./msgioerror.md)
  A driver I/O error occurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midinotificationmessageid/msgobjectremoved)*