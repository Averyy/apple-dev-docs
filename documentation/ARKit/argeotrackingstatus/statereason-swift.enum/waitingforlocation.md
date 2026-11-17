# ARGeoTrackingStatus.StateReason.waitingForLocation

**Framework**: ARKit  
**Kind**: case  
**Role**: Case

A state in which the framework performs a check for the user’s GPS position.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+

## Declaration

```swift
case waitingForLocation
```

```c
ARGeoTrackingStateReasonWaitingForLocation
```

## Discussion

While in this state, the app needs to wait for the Core Location subsystem to provide the user’s GPS location. Inform the user of the check in progress; for instance, present a message alerting them to the geo tracking initialization process.

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
- [ARGeoTrackingStatus.StateReason.worldTrackingUnstable](./worldtrackingunstable.md)
  The position or motion of the device makes geo tracking unstable.
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
- [ARGeoTrackingStatus.StateReason.worldTrackingUnstable](./worldtrackingunstable.md)
  The position or motion of the device makes geo tracking unstable.
- [ARGeoTrackingStatus.StateReason.waitingForAvailabilityCheck](./waitingforavailabilitycheck.md)
  A state in which the framework performs a check for geo tracking availability at the user’s location.
- [ARGeoTrackingStatus.StateReason.geoDataNotLoaded](./geodatanotloaded.md)
  A state in which the framework downloads localization imagery.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/argeotrackingstatus/statereason-swift.enum/waitingforlocation)*