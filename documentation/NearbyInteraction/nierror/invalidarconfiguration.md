# invalidARConfiguration

**Framework**: Nearby Interaction  
**Kind**: property  
**Role**: Type Property

An error that indicates the framework can’t begin Camera Assistance.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
static var invalidARConfiguration: NIError.Code { get }
```

## Discussion

The framework invalidates a Nearby Interaction session when the app requests Camera Assistance ([`isCameraAssistanceEnabled`](../ninearbypeerconfiguration/iscameraassistanceenabled.md)) and either of the following are true:

- The device doesn’t support Camera Assistance.
- The app’s AR session doesn’t meet the required criteria as defined in [`setARSession(_:)`](../nisession/setarsession%28_%29.md).

## See Also

### Identifying an error cause
- [NIError.Code](./code.md)
  Codes that identify errors in Nearby Interaction.
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
- [static var activeExtendedDistanceSessionsLimitExceeded: NIError.Code](./activeextendeddistancesessionslimitexceeded.md)
  An error code that indicates that the device exceeds the available number of active extended distance sessions.
- [static var incompatiblePeerDevice: NIError.Code](./incompatiblepeerdevice.md)
  An error that indicates the peer device isn’t compatible with this Nearby Interaction session instance.
- [static var accessoryPeerDeviceUnavailable: NIError.Code](./accessorypeerdeviceunavailable.md)
  An error that indicates the peer Bluetooth accessory isn’t connected or paired.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nierror/invalidarconfiguration)*