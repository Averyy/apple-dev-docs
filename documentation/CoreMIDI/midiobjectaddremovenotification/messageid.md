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
- [var parent: MIDIObjectRef](./parent.md)
  The parent object of the added or removed child.
- [var parentType: MIDIObjectType](./parenttype.md)
  The parent object type.
- [var child: MIDIObjectRef](./child.md)
  The added or removed child object.
- [var childType: MIDIObjectType](./childtype.md)
  The child object type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midiobjectaddremovenotification/messageid)*