# MIDINotificationMessageID.msgSetupChanged

**Framework**: Core MIDI  
**Kind**: case  
**Role**: Case

Some aspect of the current MIDI setup changed.

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
case msgSetupChanged
```

```c
kMIDIMsgSetupChanged
```

#### Discussion

This type provides no data. Ignore this message if you’re explicitly handling other state changes.

## See Also

### Change Types
- [MIDINotificationMessageID.msgObjectAdded](./msgobjectadded.md)
  The system added a device, entity, or endpoint.
- [MIDINotificationMessageID.msgObjectRemoved](./msgobjectremoved.md)
  The system removed a device, entity, or endpoint.
- [MIDINotificationMessageID.msgPropertyChanged](./msgpropertychanged.md)
  An object’s property value changed.
- [MIDINotificationMessageID.msgThruConnectionsChanged](./msgthruconnectionschanged.md)
  The system created or disposed of a persistent MIDI Thru connection.
- [MIDINotificationMessageID.msgSerialPortOwnerChanged](./msgserialportownerchanged.md)
  The system changed a serial port owner.
- [MIDINotificationMessageID.msgIOError](./msgioerror.md)
  A driver I/O error occurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midinotificationmessageid/msgsetupchanged)*