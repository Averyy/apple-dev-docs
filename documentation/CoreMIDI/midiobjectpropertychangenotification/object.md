# object

**Framework**: Core MIDI  
**Kind**: property  
**Role**: Instance Property

The object whose property changed.

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
var object: MIDIObjectRef
```

```c
MIDIObjectRef object;
```

## See Also

### Inspecting the Notification
- [var messageID: MIDINotificationMessageID](./messageid.md)
  The message type.
- [var messageSize: UInt32](./messagesize.md)
  The message size.
- [var objectType: MIDIObjectType](./objecttype.md)
  The object type.
- [var propertyName: Unmanaged<CFString>](./propertyname.md)
  The name of the modified property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midiobjectpropertychangenotification/object)*