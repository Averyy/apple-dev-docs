# NIError.Code.accessoryPeerDeviceUnavailable

**Framework**: Nearby Interaction  
**Kind**: case

An error that indicates the peer Bluetooth accessory isn’t connected or paired.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
case accessoryPeerDeviceUnavailable
```

#### Discussion

For more on the backgrounding requirements of accessory interaction, see [`NINearbyAccessoryConfiguration`](ninearbyaccessoryconfiguration.md).

## See Also

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
- [NIError.Code.incompatiblePeerDevice](nierror/code/incompatiblepeerdevice.md)
  An error that indicates the peer device isn’t compatible with this Nearby Interaction session instance.
- [NIError.Code.activeExtendedDistanceSessionsLimitExceeded](nierror/code/activeextendeddistancesessionslimitexceeded.md)
  An error that indicates the device exceeds the available number of active extended distance sessions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nierror/code/accessorypeerdeviceunavailable)*