# propertyName

**Framework**: Core MIDI  
**Kind**: property  
**Role**: Instance Property

The name of the modified property.

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
var propertyName: Unmanaged<CFString>
```

```c
CFStringRef propertyName;
```

## See Also

### Inspecting the Notification
- [var messageID: MIDINotificationMessageID](./messageid.md)
  The message type.
- [var messageSize: UInt32](./messagesize.md)
  The message size.
- [var object: MIDIObjectRef](./object.md)
  The object whose property changed.
- [var objectType: MIDIObjectType](./objecttype.md)
  The object type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midiobjectpropertychangenotification/propertyname)*