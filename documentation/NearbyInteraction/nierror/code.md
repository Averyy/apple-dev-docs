# NIError.Code

**Framework**: Nearby Interaction  
**Kind**: enum

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

#### Overview

This enumeration uses [`session(_:didInvalidateWith:)`](nisessiondelegate/session(_:didinvalidatewith:).md) to collect the errors the framework provides to the delegate.

## Topics

### Errors
- [NIError.Code.activeSessionsLimitExceeded](nierror/code/activesessionslimitexceeded.md)
  An error code that indicates that the app reached the maximum number of sessions.
- [NIError.Code.invalidConfiguration](nierror/code/invalidconfiguration.md)
  An error code that indicates that the nearby-interaction configuration isn’t valid.
- [NIError.Code.resourceUsageTimeout](nierror/code/resourceusagetimeout.md)
  An error code that indicates that the framework timed out the session.
- [NIError.Code.sessionFailed](nierror/code/sessionfailed.md)
  An error code that indicates that the session failed.
- [NIError.Code.unsupportedPlatform](nierror/code/unsupportedplatform.md)
  An error code that indicates that the framework doesn’t support the device platform.
- [NIError.Code.userDidNotAllow](nierror/code/userdidnotallow.md)
  An error code that indicates that the user declined the request to share their relative position with nearby devices.
- [NIError.Code.invalidARConfiguration](nierror/code/invalidarconfiguration.md)
  An error that indicates the framework can’t begin Camera Assistance.
- [NIError.Code.accessoryPeerDeviceUnavailable](nierror/code/accessorypeerdeviceunavailable.md)
  An error that indicates the peer Bluetooth accessory isn’t connected or paired.
- [NIError.Code.incompatiblePeerDevice](nierror/code/incompatiblepeerdevice.md)
  An error that indicates the peer device isn’t compatible with this Nearby Interaction session instance.
- [NIError.Code.activeExtendedDistanceSessionsLimitExceeded](nierror/code/activeextendeddistancesessionslimitexceeded.md)
  An error that indicates the device exceeds the available number of active extended distance sessions.
### Initializers
- [init?(rawValue: Int)](nierror/code/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [static var activeSessionsLimitExceeded: NIError.Code](nierror/activesessionslimitexceeded.md)
  An error code that indicates that the app reached the maximum number of sessions.
- [static var invalidConfiguration: NIError.Code](nierror/invalidconfiguration.md)
  An error code that indicates that the nearby-interaction configuration isn’t valid.
- [static var resourceUsageTimeout: NIError.Code](nierror/resourceusagetimeout.md)
  An error code that indicates that the framework timed out the session.
- [static var sessionFailed: NIError.Code](nierror/sessionfailed.md)
  An error code that indicates that the session failed.
- [static var unsupportedPlatform: NIError.Code](nierror/unsupportedplatform.md)
  An error code that indicates that the framework doesn’t support the device platform.
- [static var userDidNotAllow: NIError.Code](nierror/userdidnotallow.md)
  An error code that indicates that the user declined the request to share their relative position with nearby devices.
- [static var invalidARConfiguration: NIError.Code](nierror/invalidarconfiguration.md)
  An error that indicates the framework can’t begin Camera Assistance.
- [static var activeExtendedDistanceSessionsLimitExceeded: NIError.Code](nierror/activeextendeddistancesessionslimitexceeded.md)
  An error code that indicates that the device exceeds the available number of active extended distance sessions.
- [static var incompatiblePeerDevice: NIError.Code](nierror/incompatiblepeerdevice.md)
  An error that indicates the peer device isn’t compatible with this Nearby Interaction session instance.
- [static var accessoryPeerDeviceUnavailable: NIError.Code](nierror/accessorypeerdeviceunavailable.md)
  An error that indicates the peer Bluetooth accessory isn’t connected or paired.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nierror/code)*