# driverDevice

**Framework**: Core MIDI  
**Kind**: property  
**Role**: Instance Property

The device with an I/O error.

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
var driverDevice: MIDIDeviceRef
```

```c
MIDIDeviceRef driverDevice;
```

## See Also

### Inspecting an error notification
- [var messageID: MIDINotificationMessageID](./messageid.md)
  The type of message.
- [var messageSize: UInt32](./messagesize.md)
  The size of the message.
- [var errorCode: OSStatus](./errorcode.md)
  The error code of the generated error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midiioerrornotification/driverdevice)*