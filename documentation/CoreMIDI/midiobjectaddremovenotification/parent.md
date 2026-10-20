# parent

**Framework**: Core MIDI  
**Kind**: property  
**Role**: Instance Property

The parent object of the added or removed child.

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
var parent: MIDIObjectRef
```

```c
MIDIObjectRef parent;
```

## See Also

### Inspecting the Notification
- [var messageID: MIDINotificationMessageID](./messageid.md)
  The message type.
- [var messageSize: UInt32](./messagesize.md)
  The message size.
- [var parentType: MIDIObjectType](./parenttype.md)
  The parent object type.
- [var child: MIDIObjectRef](./child.md)
  The added or removed child object.
- [var childType: MIDIObjectType](./childtype.md)
  The child object type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midiobjectaddremovenotification/parent)*