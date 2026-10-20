# MIDIObjectAddRemoveNotification

**Framework**: Core MIDI  
**Kind**: struct  
**Role**: Structure

A message that describes the addition or removal of an object.

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
struct MIDIObjectAddRemoveNotification
```

```c
struct MIDIObjectAddRemoveNotification;
```

## Topics

### Inspecting the Notification
- [var messageID: MIDINotificationMessageID](./midiobjectaddremovenotification/messageid.md)
  The message type.
- [var messageSize: UInt32](./midiobjectaddremovenotification/messagesize.md)
  The message size.
- [var parent: MIDIObjectRef](./midiobjectaddremovenotification/parent.md)
  The parent object of the added or removed child.
- [var parentType: MIDIObjectType](./midiobjectaddremovenotification/parenttype.md)
  The parent object type.
- [var child: MIDIObjectRef](./midiobjectaddremovenotification/child.md)
  The added or removed child object.
- [var childType: MIDIObjectType](./midiobjectaddremovenotification/childtype.md)
  The child object type.
### Initializers
- [init()](./midiobjectaddremovenotification/init%28%29.md)
- [init(messageID: MIDINotificationMessageID, messageSize: UInt32, parent: MIDIObjectRef, parentType: MIDIObjectType, child: MIDIObjectRef, childType: MIDIObjectType)](./midiobjectaddremovenotification/init%28messageid,messagesize,parent,parenttype,child,childtype%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Notifications
- [struct MIDIObjectPropertyChangeNotification](./midiobjectpropertychangenotification.md)
  A message that describes the change to an object property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midiobjectaddremovenotification)*