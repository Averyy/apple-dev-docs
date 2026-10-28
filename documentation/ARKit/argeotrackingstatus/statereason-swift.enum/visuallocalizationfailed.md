# ARGeoTrackingStatus.StateReason.visualLocalizationFailed

**Framework**: ARKit  
**Kind**: case  
**Role**: Case

Localization imagery failed to match the view from the device’s camera.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+

## Declaration

```swift
case visualLocalizationFailed
```

```c
ARGeoTrackingStateReasonVisualLocalizationFailed
```

## Discussion

ARKit provides this reason when visual localization is taking too long. This indicates that the app has met all requirements for geo tracking, except for visual localization. In this situation, the app needs to ask the user to pan the device around the physical environment to acquire more camera-feed imagery. For more information, see [Assisting the User with Visual Localization](../state-swift.enum/localizing.md#Assisting-the-User-with-Visual-Localization).

## See Also

### Status Reasons
- [ARGeoTrackingStatus.StateReason.none](./none.md)
  No issues reported.
- [ARGeoTrackingStatus.StateReason.notAvailableAtLocation](./notavailableatlocation.md)
  The location doesn’t provide geotracking.
- [ARGeoTrackingStatus.StateReason.needLocationPermissions](./needlocationpermissions.md)
  The location requires user permission for geotracking.
- [ARGeoTrackingStatus.StateReason.devicePointedTooLow](./devicepointedtoolow.md)
  The position of the device is too low for geotracking.
- [ARGeoTrackingStatus.StateReason.worldTrackingUnstable](./worldtrackingunstable.md)
  The position or motion of the device makes geotracking unstable.
- [ARGeoTrackingStatus.StateReason.waitingForLocation](./waitingforlocation.md)
  A state in which the framework performs a check for the user’s GPS position.
- [ARGeoTrackingStatus.StateReason.waitingForAvailabilityCheck](./waitingforavailabilitycheck.md)
  A state in which the framework performs a check for geotracking availability at the user’s location.
- [ARGeoTrackingStatus.StateReason.geoDataNotLoaded](./geodatanotloaded.md)
  A state in which the framework downloads localization imagery.
- [ARGeoTrackingStatus.StateReason.none](./none.md)
  No issues reported.
- [ARGeoTrackingStatus.StateReason.notAvailableAtLocation](./notavailableatlocation.md)
  The location doesn’t provide geotracking.
- [ARGeoTrackingStatus.StateReason.needLocationPermissions](./needlocationpermissions.md)
  The location requires user permission for geotracking.
- [ARGeoTrackingStatus.StateReason.devicePointedTooLow](./devicepointedtoolow.md)
  The position of the device is too low for geotracking.
- [ARGeoTrackingStatus.StateReason.worldTrackingUnstable](./worldtrackingunstable.md)
  The position or motion of the device makes geotracking unstable.
- [ARGeoTrackingStatus.StateReason.waitingForLocation](./waitingforlocation.md)
  A state in which the framework performs a check for the user’s GPS position.
- [ARGeoTrackingStatus.StateReason.waitingForAvailabilityCheck](./waitingforavailabilitycheck.md)
  A state in which the framework performs a check for geotracking availability at the user’s location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/argeotrackingstatus/statereason-swift.enum/visuallocalizationfailed)*