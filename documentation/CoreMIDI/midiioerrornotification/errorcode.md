# errorCode

**Framework**: Core MIDI  
**Kind**: property  
**Role**: Instance Property

The error code of the generated error.

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
var errorCode: OSStatus
```

```c
OSStatus errorCode;
```

## See Also

### Inspecting an error notification
- [var messageID: MIDINotificationMessageID](./messageid.md)
  The type of message.
- [var messageSize: UInt32](./messagesize.md)
  The size of the message.
- [var driverDevice: MIDIDeviceRef](./driverdevice.md)
  The device with an I/O error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midiioerrornotification/errorcode)*