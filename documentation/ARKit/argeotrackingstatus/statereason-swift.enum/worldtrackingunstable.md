# ARGeoTrackingStatus.StateReason.worldTrackingUnstable

**Framework**: ARKit  
**Kind**: case  
**Role**: Case

The position or motion of the device makes geo tracking unstable.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+

## Declaration

```swift
case worldTrackingUnstable
```

```c
ARGeoTrackingStateReasonWorldTrackingUnstable
```

## Discussion

This reason indicates that ARKit’s local-space tracking is functioning at a limited capacity. To retrieve more information about the cause, an app needs to refer to the camera’s [`trackingState`](../../arcamera/trackingstate-9pgmq.md). For the possible causes of this state, see [`ARTrackingState`](../../artrackingstate.md) and [`ARTrackingStateReason`](../../artrackingstatereason.md).

## See Also

### Status Reasons
- [ARGeoTrackingStatus.StateReason.none](./none.md)
  No issues reported.
- [ARGeoTrackingStatus.StateReason.notAvailableAtLocation](./notavailableatlocation.md)
  The location doesn’t provide geo tracking.
- [ARGeoTrackingStatus.StateReason.needLocationPermissions](./needlocationpermissions.md)
  The location requires user permission for geo tracking.
- [ARGeoTrackingStatus.StateReason.devicePointedTooLow](./devicepointedtoolow.md)
  The position of the device is too low for geo tracking.
- [ARGeoTrackingStatus.StateReason.waitingForLocation](./waitingforlocation.md)
  A state in which the framework performs a check for the user’s GPS position.
- [ARGeoTrackingStatus.StateReason.waitingForAvailabilityCheck](./waitingforavailabilitycheck.md)
  A state in which the framework performs a check for geo tracking availability at the user’s location.
- [ARGeoTrackingStatus.StateReason.geoDataNotLoaded](./geodatanotloaded.md)
  A state in which the framework downloads localization imagery.
- [ARGeoTrackingStatus.StateReason.visualLocalizationFailed](./visuallocalizationfailed.md)
  Localization imagery failed to match the view from the device’s camera.
- [ARGeoTrackingStatus.StateReason.none](./none.md)
  No issues reported.
- [ARGeoTrackingStatus.StateReason.notAvailableAtLocation](./notavailableatlocation.md)
  The location doesn’t provide geo tracking.
- [ARGeoTrackingStatus.StateReason.needLocationPermissions](./needlocationpermissions.md)
  The location requires user permission for geo tracking.
- [ARGeoTrackingStatus.StateReason.devicePointedTooLow](./devicepointedtoolow.md)
  The position of the device is too low for geo tracking.
- [ARGeoTrackingStatus.StateReason.waitingForLocation](./waitingforlocation.md)
  A state in which the framework performs a check for the user’s GPS position.
- [ARGeoTrackingStatus.StateReason.waitingForAvailabilityCheck](./waitingforavailabilitycheck.md)
  A state in which the framework performs a check for geo tracking availability at the user’s location.
- [ARGeoTrackingStatus.StateReason.geoDataNotLoaded](./geodatanotloaded.md)
  A state in which the framework downloads localization imagery.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/argeotrackingstatus/statereason-swift.enum/worldtrackingunstable)*