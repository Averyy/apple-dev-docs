# NIError.Code.invalidARConfiguration

**Framework**: Nearby Interaction  
**Kind**: case  
**Role**: Case

An error that indicates the framework can’t begin Camera Assistance.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
case invalidARConfiguration
```

```c
NIErrorCodeInvalidARConfiguration
```

## Discussion

The framework invalidates a Nearby Interaction session when the app requests Camera Assistance ([`isCameraAssistanceEnabled`](../../ninearbypeerconfiguration/iscameraassistanceenabled.md)) and either of the following are true:

- The device doesn’t support Camera Assistance.
- The app’s AR session doesn’t meet the required criteria as defined in [`setARSession(_:)`](../../nisession/setarsession%28_%29.md).

## See Also

### Errors
- [NIError.Code.activeSessionsLimitExceeded](./activesessionslimitexceeded.md)
  An error code that indicates that the app reached the maximum number of sessions.
- [NIError.Code.invalidConfiguration](./invalidconfiguration.md)
  An error code that indicates that the nearby-interaction configuration isn’t valid.
- [NIError.Code.resourceUsageTimeout](./resourceusagetimeout.md)
  An error code that indicates that the framework timed out the session.
- [NIError.Code.sessionFailed](./sessionfailed.md)
  An error code that indicates that the session failed.
- [NIError.Code.unsupportedPlatform](./unsupportedplatform.md)
  An error code that indicates that the framework doesn’t support the device platform.
- [NIError.Code.userDidNotAllow](./userdidnotallow.md)
  An error code that indicates that the user declined the request to share their relative position with nearby devices.
- [NIError.Code.accessoryPeerDeviceUnavailable](./accessorypeerdeviceunavailable.md)
  An error that indicates the peer Bluetooth accessory isn’t connected or paired.
- [NIError.Code.incompatiblePeerDevice](./incompatiblepeerdevice.md)
  An error that indicates the peer device isn’t compatible with this Nearby Interaction session instance.
- [NIError.Code.activeExtendedDistanceSessionsLimitExceeded](./activeextendeddistancesessionslimitexceeded.md)
  An error that indicates the device exceeds the available number of active extended distance sessions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nierror/code/invalidarconfiguration)*