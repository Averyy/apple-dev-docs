# NIError.Code

**Framework**: Nearby Interaction  
**Kind**: enum  
**Role**: Enumeration

Codes that identify errors in Nearby Interaction.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- watchOS 7.3+

## Declaration

```swift
enum Code
```

```c
enum NIErrorCode : NSInteger;
```

## Overview

This enumeration uses [`session(_:didInvalidateWith:)`](../nisessiondelegate/session%28_,didinvalidatewith%29.md) to collect the errors the framework provides to the delegate.

## Topics

### Errors
- [NIError.Code.activeSessionsLimitExceeded](./code/activesessionslimitexceeded.md)
  An error code that indicates that the app reached the maximum number of sessions.
- [NIError.Code.invalidConfiguration](./code/invalidconfiguration.md)
  An error code that indicates that the nearby-interaction configuration isn’t valid.
- [NIError.Code.resourceUsageTimeout](./code/resourceusagetimeout.md)
  An error code that indicates that the framework timed out the session.
- [NIError.Code.sessionFailed](./code/sessionfailed.md)
  An error code that indicates that the session failed.
- [NIError.Code.unsupportedPlatform](./code/unsupportedplatform.md)
  An error code that indicates that the framework doesn’t support the device platform.
- [NIError.Code.userDidNotAllow](./code/userdidnotallow.md)
  An error code that indicates that the user declined the request to share their relative position with nearby devices.
- [NIError.Code.invalidARConfiguration](./code/invalidarconfiguration.md)
  An error that indicates the framework can’t begin Camera Assistance.
- [NIError.Code.accessoryPeerDeviceUnavailable](./code/accessorypeerdeviceunavailable.md)
  An error that indicates the peer Bluetooth accessory isn’t connected or paired.
- [NIError.Code.incompatiblePeerDevice](./code/incompatiblepeerdevice.md)
  An error that indicates the peer device isn’t compatible with this Nearby Interaction session instance.
- [NIError.Code.activeExtendedDistanceSessionsLimitExceeded](./code/activeextendeddistancesessionslimitexceeded.md)
  An error that indicates the device exceeds the available number of active extended distance sessions.
### Initializers
- [init?(rawValue: Int)](./code/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Identifying an error cause
- [static var activeSessionsLimitExceeded: NIError.Code](./activesessionslimitexceeded.md)
  An error code that indicates that the app reached the maximum number of sessions.
- [static var invalidConfiguration: NIError.Code](./invalidconfiguration.md)
  An error code that indicates that the nearby-interaction configuration isn’t valid.
- [static var resourceUsageTimeout: NIError.Code](./resourceusagetimeout.md)
  An error code that indicates that the framework timed out the session.
- [static var sessionFailed: NIError.Code](./sessionfailed.md)
  An error code that indicates that the session failed.
- [static var unsupportedPlatform: NIError.Code](./unsupportedplatform.md)
  An error code that indicates that the framework doesn’t support the device platform.
- [static var userDidNotAllow: NIError.Code](./userdidnotallow.md)
  An error code that indicates that the user declined the request to share their relative position with nearby devices.
- [static var invalidARConfiguration: NIError.Code](./invalidarconfiguration.md)
  An error that indicates the framework can’t begin Camera Assistance.
- [static var activeExtendedDistanceSessionsLimitExceeded: NIError.Code](./activeextendeddistancesessionslimitexceeded.md)
  An error code that indicates that the device exceeds the available number of active extended distance sessions.
- [static var incompatiblePeerDevice: NIError.Code](./incompatiblepeerdevice.md)
  An error that indicates the peer device isn’t compatible with this Nearby Interaction session instance.
- [static var accessoryPeerDeviceUnavailable: NIError.Code](./accessorypeerdeviceunavailable.md)
  An error that indicates the peer Bluetooth accessory isn’t connected or paired.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nierror/code)*