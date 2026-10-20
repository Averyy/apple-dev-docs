# objectType

**Framework**: Core MIDI  
**Kind**: property  
**Role**: Instance Property

The object type.

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
var objectType: MIDIObjectType
```

```c
MIDIObjectType objectType;
```

## See Also

### Inspecting the Notification
- [var messageID: MIDINotificationMessageID](./messageid.md)
  The message type.
- [var messageSize: UInt32](./messagesize.md)
  The message size.
- [var object: MIDIObjectRef](./object.md)
  The object whose property changed.
- [var propertyName: Unmanaged<CFString>](./propertyname.md)
  The name of the modified property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midiobjectpropertychangenotification/objecttype)*