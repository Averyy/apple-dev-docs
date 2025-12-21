# ARGeoTrackingStatus.State.localizing

**Framework**: ARKit  
**Kind**: case

Geo tracking is attempting to localize against a map.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
case localizing
```

#### Discussion

In [`ARGeoTrackingStatus.State.localizing`](argeotrackingstatus/state-swift.enum/localizing.md), the session downloads localization imagery for the user’s geographic location and compares it with captures from the device’s camera. This process is referred to as . When ARKit succeeds in matching this imagery with captures from the camera, the state moves to [`ARGeoTrackingStatus.State.localized`](argeotrackingstatus/state-swift.enum/localized.md) and the app is free to create location anchors. For more information about localization imagery, see [`Refine the user’s position with imagery`](argeotrackingconfiguration#Refine-the-users-position-with-imagery.md).

##### Assisting the User with Visual Localization

To establish visual localization, the user must move the camera so it acquires the captures that ARKit needs. To elicit the right user movements in [`ARGeoTrackingStatus.State.localizing`](argeotrackingstatus/state-swift.enum/localizing.md), the app needs to advise the user to:

- Point the camera at buildings and other visual landmarks to help ARKit match the live camera data with its preexisting landscape-data.
- Avoid pointing the device at objects that are too general, like trees. It’s better to focus on distinct visuals, like structures, or signs.
- Avoid pointing the device at real-world objects that are transient, like parked cars, or a construction site.
- Because lighting conditions can affect visual localization, avoid geo tracking at night.

## See Also

- [ARGeoTrackingStatus.State.initializing](argeotrackingstatus/state-swift.enum/initializing.md)
  The session is initializing geo tracking.
- [ARGeoTrackingStatus.State.localized](argeotrackingstatus/state-swift.enum/localized.md)
  Geo tracking is localized.
- [ARGeoTrackingStatus.State.notAvailable](argeotrackingstatus/state-swift.enum/notavailable.md)
  Geo tracking is not available.
- [ARGeoTrackingStatus.State.initializing](argeotrackingstatus/state-swift.enum/initializing.md)
  The session is initializing geo tracking.
- [ARGeoTrackingStatus.State.localized](argeotrackingstatus/state-swift.enum/localized.md)
  Geo tracking is localized.
- [ARGeoTrackingStatus.State.notAvailable](argeotrackingstatus/state-swift.enum/notavailable.md)
  Geo tracking is not available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/argeotrackingstatus/state-swift.enum/localizing)*