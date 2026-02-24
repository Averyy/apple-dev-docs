# AccessoryControlDevice.Error

**Framework**: AudioAccessoryKit  
**Kind**: enum

An error that occurs during audio accessory configuration operations.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)

## Declaration

```swift
enum Error
```

#### Overview

Use error cases to identify the cause of failures when registering devices or updating their state.

## Topics

### Error cases
- [AccessoryControlDevice.Error.connectionFailed](accessorycontroldevice/error/connectionfailed.md)
  An error indicating the Bluetooth connection to the device failed.
- [AccessoryControlDevice.Error.deviceNotCapable](accessorycontroldevice/error/devicenotcapable.md)
  An error indicating the device doesn’t support the requested capability.
- [AccessoryControlDevice.Error.fatal](accessorycontroldevice/error/fatal.md)
  An error indicating a fatal system error.
- [AccessoryControlDevice.Error.invalidRequest](accessorycontroldevice/error/invalidrequest.md)
  An error indicating an invalid request.
- [AccessoryControlDevice.Error.invalidated](accessorycontroldevice/error/invalidated.md)
  An error indicating a configuration that the system has invalidated.
- [AccessoryControlDevice.Error.unknown](accessorycontroldevice/error/unknown.md)
  An error indicating an unknown error.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Escapable](../Swift/Escapable.md)
- [Hashable](../Swift/Hashable.md)
- [LocalizedError](../Foundation/LocalizedError.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audioaccessorykit/accessorycontroldevice/error)*