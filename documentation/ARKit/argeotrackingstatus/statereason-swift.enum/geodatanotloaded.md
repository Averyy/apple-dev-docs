# ARGeoTrackingStatus.StateReason.geoDataNotLoaded

**Framework**: ARKit  
**Kind**: case

A state in which the framework downloads localization imagery.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
case geoDataNotLoaded
```

#### Discussion

ARKit provides this reason in state [`ARGeoTrackingStatus.State.localizing`](argeotrackingstatus/state-swift.enum/localizing.md) when the session is actively attempting to download localization imagery (see [`Refine the user’s position with imagery`](argeotrackingconfiguration#Refine-the-users-position-with-imagery.md)).

If this state persists for too long, it may indicate a network issue. If a reasonable amount of time elapses in this state reason, the app may consider requesting that the user check their internet connection.

## See Also

- [ARGeoTrackingStatus.StateReason.none](argeotrackingstatus/statereason-swift.enum/none.md)
  No issues reported.
- [ARGeoTrackingStatus.StateReason.notAvailableAtLocation](argeotrackingstatus/statereason-swift.enum/notavailableatlocation.md)
  The location doesn’t provide geotracking.
- [ARGeoTrackingStatus.StateReason.needLocationPermissions](argeotrackingstatus/statereason-swift.enum/needlocationpermissions.md)
  The location requires user permission for geotracking.
- [ARGeoTrackingStatus.StateReason.devicePointedTooLow](argeotrackingstatus/statereason-swift.enum/devicepointedtoolow.md)
  The position of the device is too low for geotracking.
- [ARGeoTrackingStatus.StateReason.worldTrackingUnstable](argeotrackingstatus/statereason-swift.enum/worldtrackingunstable.md)
  The position or motion of the device makes geotracking unstable.
- [ARGeoTrackingStatus.StateReason.waitingForLocation](argeotrackingstatus/statereason-swift.enum/waitingforlocation.md)
  A state in which the framework performs a check for the user’s GPS position.
- [ARGeoTrackingStatus.StateReason.waitingForAvailabilityCheck](argeotrackingstatus/statereason-swift.enum/waitingforavailabilitycheck.md)
  A state in which the framework performs a check for geotracking availability at the user’s location.
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
- [ARGeoTrackingStatus.StateReason.worldTrackingUnstable](argeotrackingstatus/statereason-swift.enum/worldtrackingunstable.md)
  The position or motion of the device makes geotracking unstable.
- [ARGeoTrackingStatus.StateReason.waitingForLocation](argeotrackingstatus/statereason-swift.enum/waitingforlocation.md)
  A state in which the framework performs a check for the user’s GPS position.
- [ARGeoTrackingStatus.StateReason.waitingForAvailabilityCheck](argeotrackingstatus/statereason-swift.enum/waitingforavailabilitycheck.md)
  A state in which the framework performs a check for geotracking availability at the user’s location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/argeotrackingstatus/statereason-swift.enum/geodatanotloaded)*