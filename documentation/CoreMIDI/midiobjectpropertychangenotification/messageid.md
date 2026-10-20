# messageID

**Framework**: Core MIDI  
**Kind**: property  
**Role**: Instance Property

The message type.

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
var messageID: MIDINotificationMessageID
```

```c
MIDINotificationMessageID messageID;
```

## See Also

### Inspecting the Notification
- [var messageSize: UInt32](./messagesize.md)
  The message size.
- [var object: MIDIObjectRef](./object.md)
  The object whose property changed.
- [var objectType: MIDIObjectType](./objecttype.md)
  The object type.
- [var propertyName: Unmanaged<CFString>](./propertyname.md)
  The name of the modified property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midiobjectpropertychangenotification/messageid)*