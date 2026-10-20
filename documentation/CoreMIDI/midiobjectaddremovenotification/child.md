# child

**Framework**: Core MIDI  
**Kind**: property  
**Role**: Instance Property

The added or removed child object.

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
var child: MIDIObjectRef
```

```c
MIDIObjectRef child;
```

## See Also

### Inspecting the Notification
- [var messageID: MIDINotificationMessageID](./messageid.md)
  The message type.
- [var messageSize: UInt32](./messagesize.md)
  The message size.
- [var parent: MIDIObjectRef](./parent.md)
  The parent object of the added or removed child.
- [var parentType: MIDIObjectType](./parenttype.md)
  The parent object type.
- [var childType: MIDIObjectType](./childtype.md)
  The child object type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midiobjectaddremovenotification/child)*