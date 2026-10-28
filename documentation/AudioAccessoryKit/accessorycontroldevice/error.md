# AccessoryControlDevice.Error

**Framework**: AudioAccessoryKit  
**Kind**: enum  
**Role**: Enumeration

An error that occurs during audio accessory configuration operations.

**Availability**:
- iOS 26.4+

## Declaration

```swift
enum Error
```

## Overview

Use error cases to identify the cause of failures when registering devices or updating their state.

## Topics

### Error cases
- [AccessoryControlDevice.Error.accessoryNotCapable](./error/accessorynotcapable.md)
  An error indicating the accessory doesn’t support the requested capability.
- [AccessoryControlDevice.Error.invalidRequest](./error/invalidrequest.md)
  An error indicating an invalid request.
- [AccessoryControlDevice.Error.invalidated](./error/invalidated.md)
  An error indicating a configuration that the system has invalidated.
- [AccessoryControlDevice.Error.unknown](./error/unknown.md)
  An error indicating an unknown error.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Error](../../Swift/error.md)
- [Hashable](../../Swift/hashable.md)
- [LocalizedError](../../Foundation/localizederror.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audioaccessorykit/accessorycontroldevice/error)*