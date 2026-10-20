# MIDINotificationMessageID.msgPropertyChanged

**Framework**: Core MIDI  
**Kind**: case  
**Role**: Case

An object’s property value changed.

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
case msgPropertyChanged
```

```c
kMIDIMsgPropertyChanged
```

#### Discussion

This type’s data is [`MIDIObjectPropertyChangeNotification`](../midiobjectpropertychangenotification.md).

## See Also

### Change Types
- [MIDINotificationMessageID.msgSetupChanged](./msgsetupchanged.md)
  Some aspect of the current MIDI setup changed.
- [MIDINotificationMessageID.msgObjectAdded](./msgobjectadded.md)
  The system added a device, entity, or endpoint.
- [MIDINotificationMessageID.msgObjectRemoved](./msgobjectremoved.md)
  The system removed a device, entity, or endpoint.
- [MIDINotificationMessageID.msgThruConnectionsChanged](./msgthruconnectionschanged.md)
  The system created or disposed of a persistent MIDI Thru connection.
- [MIDINotificationMessageID.msgSerialPortOwnerChanged](./msgserialportownerchanged.md)
  The system changed a serial port owner.
- [MIDINotificationMessageID.msgIOError](./msgioerror.md)
  A driver I/O error occurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midinotificationmessageid/msgpropertychanged)*