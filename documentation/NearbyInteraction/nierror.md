# NIError

**Framework**: Nearby Interaction  
**Kind**: struct

An error Nearby Interaction reports.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- watchOS 7.3+

## Declaration

```swift
struct NIError
```

#### Overview

Implement the [`session(_:didInvalidateWith:)`](nisessiondelegate/session(_:didinvalidatewith:).md) callback to check for errors.

## Topics

### Identifying an error cause
- [NIError.Code](nierror/code.md)
  Codes that identify errors in Nearby Interaction.
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
### Type Properties
- [static var errorDomain: String](nierror/errordomain.md)

## Relationships

### Conforms To
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [NIError.Code](nierror/code.md)
  Codes that identify errors in Nearby Interaction.
- [let NIErrorDomain: String](nierrordomain.md)
  A unique error domain for Nearby Interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nierror)*