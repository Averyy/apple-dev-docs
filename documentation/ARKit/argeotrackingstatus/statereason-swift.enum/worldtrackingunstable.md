# ARGeoTrackingStatus.StateReason.worldTrackingUnstable

**Framework**: ARKit  
**Kind**: case

The position or motion of the device makes geotracking unstable.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
case worldTrackingUnstable
```

#### Discussion

This reason indicates that ARKit’s local-space tracking is functioning at a limited capacity. To retrieve more information about the cause, an app needs to refer to the camera’s [`trackingState`](arcamera/trackingstate-6i3pt.md). For the possible causes of this state, see [`ARTrackingState`](artrackingstate.md) and [`ARTrackingStateReason`](artrackingstatereason.md).

## See Also

- [ARGeoTrackingStatus.StateReason.none](argeotrackingstatus/statereason-swift.enum/none.md)
  No issues reported.
- [ARGeoTrackingStatus.StateReason.notAvailableAtLocation](argeotrackingstatus/statereason-swift.enum/notavailableatlocation.md)
  The location doesn’t provide geotracking.
- [ARGeoTrackingStatus.StateReason.needLocationPermissions](argeotrackingstatus/statereason-swift.enum/needlocationpermissions.md)
  The location requires user permission for geotracking.
- [ARGeoTrackingStatus.StateReason.devicePointedTooLow](argeotrackingstatus/statereason-swift.enum/devicepointedtoolow.md)
  The position of the device is too low for geotracking.
- [ARGeoTrackingStatus.StateReason.waitingForLocation](argeotrackingstatus/statereason-swift.enum/waitingforlocation.md)
  A state in which the framework performs a check for the user’s GPS position.
- [ARGeoTrackingStatus.StateReason.waitingForAvailabilityCheck](argeotrackingstatus/statereason-swift.enum/waitingforavailabilitycheck.md)
  A state in which the framework performs a check for geotracking availability at the user’s location.
- [ARGeoTrackingStatus.StateReason.geoDataNotLoaded](argeotrackingstatus/statereason-swift.enum/geodatanotloaded.md)
  A state in which the framework downloads localization imagery.
- [ARGeoTrackingStatus.StateReason.visualLocalizationFailed](argeotrackingstatus/statereason-swift.enum/visuallocalizationfailed.md)
  Localization imagery failed to match the view from the device’s camera.
- [ARGeoTrackingStatus.StateReason.none](argeotrackingstatus/statereason-swift.enum/none.md)
  No issues reported.
- [ARGeoTrackingStatus.StateReason.notAvailableAtLocation](argeotrackingstatus/statereason-swift.enum/notavailableatlocation.md)
  The location doesn’t provide geotracking.
- [ARGeoTrackingStatus.StateReason.needLocationPermissions](argeotrackingstatus/statereason-swift.enum/needlocationpermissions.md)
  The location requires user permission for geotracking.
- [ARGeoTrackingStatus.StateReason.devicePointedTooLow](argeotrackingstatus/statereason-swift.enum/devicepointedtoolow.md)
  The position of the device is too low for geotracking.
- [ARGeoTrackingStatus.StateReason.waitingForLocation](argeotrackingstatus/statereason-swift.enum/waitingforlocation.md)
  A state in which the framework performs a check for the user’s GPS position.
- [ARGeoTrackingStatus.StateReason.waitingForAvailabilityCheck](argeotrackingstatus/statereason-swift.enum/waitingforavailabilitycheck.md)
  A state in which the framework performs a check for geotracking availability at the user’s location.
- [ARGeoTrackingStatus.StateReason.geoDataNotLoaded](argeotrackingstatus/statereason-swift.enum/geodatanotloaded.md)
  A state in which the framework downloads localization imagery.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/argeotrackingstatus/statereason-swift.enum/worldtrackingunstable)*