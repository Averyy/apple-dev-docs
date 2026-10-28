# NIError.Code.invalidConfiguration

**Framework**: Nearby Interaction  
**Kind**: case  
**Role**: Case

An error code that indicates that the nearby-interaction configuration isn’t valid.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- watchOS 7.3+

## Declaration

```swift
case invalidConfiguration
```

```c
NIErrorCodeInvalidConfiguration
```

## Mentions

- [Initiating and maintaining a session](../../initiating-and-maintaining-a-session.md)

## Discussion

The framework invalidates a session with this error code if the app provides an invalid discovery token to the [`init(peerToken:)`](../../ninearbypeerconfiguration/init%28peertoken%29.md) initializer.

## See Also

### Errors
- [NIError.Code.activeSessionsLimitExceeded](./activesessionslimitexceeded.md)
  An error code that indicates that the app reached the maximum number of sessions.
- [NIError.Code.resourceUsageTimeout](./resourceusagetimeout.md)
  An error code that indicates that the framework timed out the session.
- [NIError.Code.sessionFailed](./sessionfailed.md)
  An error code that indicates that the session failed.
- [NIError.Code.unsupportedPlatform](./unsupportedplatform.md)
  An error code that indicates that the framework doesn’t support the device platform.
- [NIError.Code.userDidNotAllow](./userdidnotallow.md)
  An error code that indicates that the user declined the request to share their relative position with nearby devices.
- [NIError.Code.invalidARConfiguration](./invalidarconfiguration.md)
  An error that indicates the framework can’t begin Camera Assistance.
- [NIError.Code.accessoryPeerDeviceUnavailable](./accessorypeerdeviceunavailable.md)
  An error that indicates the peer Bluetooth accessory isn’t connected or paired.
- [NIError.Code.incompatiblePeerDevice](./incompatiblepeerdevice.md)
  An error that indicates the peer device isn’t compatible with this Nearby Interaction session instance.
- [NIError.Code.activeExtendedDistanceSessionsLimitExceeded](./activeextendeddistancesessionslimitexceeded.md)
  An error that indicates the device exceeds the available number of active extended distance sessions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nierror/code/invalidconfiguration)*