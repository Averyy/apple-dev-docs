# unsupportedPlatform

**Framework**: Nearby Interaction  
**Kind**: property

An error code that indicates that the framework doesn’t support the device platform.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- watchOS 7.3+

## Declaration

```swift
static var unsupportedPlatform: NIError.Code { get }
```

#### Discussion

Before running an interaction session, call [`isSupported`](nisession/issupported.md) to ensure that Nearby Interaction supports the device’s platform.

## See Also

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

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nierror/unsupportedplatform)*