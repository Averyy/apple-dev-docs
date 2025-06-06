# ARGeoTrackingStatus.StateReason.devicePointedTooLow

**Framework**: ARKit  
**Kind**: case

The position of the device is too low for geotracking.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
case devicePointedTooLow
```

#### Discussion

ARKit provides the app with this reason when the app is in state [`ARGeoTrackingStatus.State.localizing`](argeotrackingstatus/state-swift.enum/localizing.md) and the device is not capturing enough of the necessary live-camera imagery needed for visual localization because the user is pointing the camera too low. To resolve the issue, the app needs to instruct the user to raise the device and follow the guidance in [`Assisting the User with Visual Localization`](argeotrackingstatus/state-swift.enum/localizing#Assisting-the-User-with-Visual-Localization.md).

## See Also

- [ARGeoTrackingStatus.StateReason.none](argeotrackingstatus/statereason-swift.enum/none.md)
  No issues reported.
- [ARGeoTrackingStatus.StateReason.notAvailableAtLocation](argeotrackingstatus/statereason-swift.enum/notavailableatlocation.md)
  The location doesn’t provide geotracking.
- [ARGeoTrackingStatus.StateReason.needLocationPermissions](argeotrackingstatus/statereason-swift.enum/needlocationpermissions.md)
  The location requires user permission for geotracking.
- [ARGeoTrackingStatus.StateReason.worldTrackingUnstable](argeotrackingstatus/statereason-swift.enum/worldtrackingunstable.md)
  The position or motion of the device makes geotracking unstable.
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
- [ARGeoTrackingStatus.StateReason.worldTrackingUnstable](argeotrackingstatus/statereason-swift.enum/worldtrackingunstable.md)
  The position or motion of the device makes geotracking unstable.
- [ARGeoTrackingStatus.StateReason.waitingForLocation](argeotrackingstatus/statereason-swift.enum/waitingforlocation.md)
  A state in which the framework performs a check for the user’s GPS position.
- [ARGeoTrackingStatus.StateReason.waitingForAvailabilityCheck](argeotrackingstatus/statereason-swift.enum/waitingforavailabilitycheck.md)
  A state in which the framework performs a check for geotracking availability at the user’s location.
- [ARGeoTrackingStatus.StateReason.geoDataNotLoaded](argeotrackingstatus/statereason-swift.enum/geodatanotloaded.md)
  A state in which the framework downloads localization imagery.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/argeotrackingstatus/statereason-swift.enum/devicepointedtoolow)*