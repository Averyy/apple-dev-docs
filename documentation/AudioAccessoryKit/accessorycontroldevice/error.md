# AccessoryControlDevice.Error

**Framework**: AudioAccessoryKit  
**Kind**: enum

An error that occurs during audio accessory configuration operations.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
enum Error
```

#### Overview

Use error cases to identify the cause of failures when registering devices or updating their state.

## Topics

### Error cases
- [AccessoryControlDevice.Error.accessoryNotCapable](accessorycontroldevice/error/accessorynotcapable.md)
  An error indicating the accessory doesn’t support the requested capability.
- [AccessoryControlDevice.Error.invalidRequest](accessorycontroldevice/error/invalidrequest.md)
  An error indicating an invalid request.
- [AccessoryControlDevice.Error.invalidated](accessorycontroldevice/error/invalidated.md)
  An error indicating a configuration that the system has invalidated.
- [AccessoryControlDevice.Error.unknown](accessorycontroldevice/error/unknown.md)
  An error indicating an unknown error.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [LocalizedError](../Foundation/LocalizedError.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audioaccessorykit/accessorycontroldevice/error)*