# MIDIObjectPropertyChangeNotification

**Framework**: Core MIDI  
**Kind**: struct

A message that describes the change to an object property.

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
struct MIDIObjectPropertyChangeNotification
```

## Topics

### Inspecting the Notification
- [var messageID: MIDINotificationMessageID](midiobjectpropertychangenotification/messageid.md)
  The message type.
- [var messageSize: UInt32](midiobjectpropertychangenotification/messagesize.md)
  The message size.
- [var object: MIDIObjectRef](midiobjectpropertychangenotification/object.md)
  The object whose property changed.
- [var objectType: MIDIObjectType](midiobjectpropertychangenotification/objecttype.md)
  The object type.
- [var propertyName: Unmanaged<CFString>](midiobjectpropertychangenotification/propertyname.md)
  The name of the modified property.
### Initializers
- [init(messageID: MIDINotificationMessageID, messageSize: UInt32, object: MIDIObjectRef, objectType: MIDIObjectType, propertyName: Unmanaged<CFString>)](midiobjectpropertychangenotification/init(messageid:messagesize:object:objecttype:propertyname:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [struct MIDIObjectAddRemoveNotification](midiobjectaddremovenotification.md)
  A message that describes the addition or removal of an object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midiobjectpropertychangenotification)*