# ARGeoTrackingStatus.StateReason

**Framework**: ARKit  
**Kind**: enum  
**Role**: Enumeration

The reasons for the app’s geotracking status.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+

## Declaration

```swift
enum StateReason
```

```c
enum ARGeoTrackingStateReason : NSInteger;
```

## Overview

These possible values of [`stateReason`](./statereason-swift.property.md) provide more information about a geotracking session’s current [`state`](./state-swift.property.md).

## Topics

### Status Reasons
- [ARGeoTrackingStatus.StateReason.none](./statereason-swift.enum/none.md)
  No issues reported.
- [ARGeoTrackingStatus.StateReason.notAvailableAtLocation](./statereason-swift.enum/notavailableatlocation.md)
  The location doesn’t provide geotracking.
- [ARGeoTrackingStatus.StateReason.needLocationPermissions](./statereason-swift.enum/needlocationpermissions.md)
  The location requires user permission for geotracking.
- [ARGeoTrackingStatus.StateReason.devicePointedTooLow](./statereason-swift.enum/devicepointedtoolow.md)
  The position of the device is too low for geotracking.
- [ARGeoTrackingStatus.StateReason.worldTrackingUnstable](./statereason-swift.enum/worldtrackingunstable.md)
  The position or motion of the device makes geotracking unstable.
- [ARGeoTrackingStatus.StateReason.waitingForLocation](./statereason-swift.enum/waitingforlocation.md)
  A state in which the framework performs a check for the user’s GPS position.
- [ARGeoTrackingStatus.StateReason.waitingForAvailabilityCheck](./statereason-swift.enum/waitingforavailabilitycheck.md)
  A state in which the framework performs a check for geotracking availability at the user’s location.
- [ARGeoTrackingStatus.StateReason.geoDataNotLoaded](./statereason-swift.enum/geodatanotloaded.md)
  A state in which the framework downloads localization imagery.
- [ARGeoTrackingStatus.StateReason.visualLocalizationFailed](./statereason-swift.enum/visuallocalizationfailed.md)
  Localization imagery failed to match the view from the device’s camera.
- [ARGeoTrackingStatus.StateReason.none](./statereason-swift.enum/none.md)
  No issues reported.
- [ARGeoTrackingStatus.StateReason.notAvailableAtLocation](./statereason-swift.enum/notavailableatlocation.md)
  The location doesn’t provide geotracking.
- [ARGeoTrackingStatus.StateReason.needLocationPermissions](./statereason-swift.enum/needlocationpermissions.md)
  The location requires user permission for geotracking.
- [ARGeoTrackingStatus.StateReason.devicePointedTooLow](./statereason-swift.enum/devicepointedtoolow.md)
  The position of the device is too low for geotracking.
- [ARGeoTrackingStatus.StateReason.worldTrackingUnstable](./statereason-swift.enum/worldtrackingunstable.md)
  The position or motion of the device makes geotracking unstable.
- [ARGeoTrackingStatus.StateReason.waitingForLocation](./statereason-swift.enum/waitingforlocation.md)
  A state in which the framework performs a check for the user’s GPS position.
- [ARGeoTrackingStatus.StateReason.waitingForAvailabilityCheck](./statereason-swift.enum/waitingforavailabilitycheck.md)
  A state in which the framework performs a check for geotracking availability at the user’s location.
- [ARGeoTrackingStatus.StateReason.geoDataNotLoaded](./statereason-swift.enum/geodatanotloaded.md)
  A state in which the framework downloads localization imagery.
- [ARGeoTrackingStatus.StateReason.visualLocalizationFailed](./statereason-swift.enum/visuallocalizationfailed.md)
  Localization imagery failed to match the view from the device’s camera.
### Initializers
- [init?(rawValue: Int)](./statereason-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Determining the Reason
- [var stateReason: ARGeoTrackingStatus.StateReason](./statereason-swift.property.md)
  The reasons for the app’s geotracking status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/argeotrackingstatus/statereason-swift.enum)*