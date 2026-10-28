# ARGeoTrackingStatus.State.localizing

**Framework**: ARKit  
**Kind**: case  
**Role**: Case

Geo tracking is attempting to localize against a map.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+

## Declaration

```swift
case localizing
```

```c
ARGeoTrackingStateLocalizing
```

## Discussion

In [`ARGeoTrackingStatus.State.localizing`](./localizing.md), the session downloads localization imagery for the user’s geographic location and compares it with captures from the device’s camera. This process is referred to as *visual localization*. When ARKit succeeds in matching this imagery with captures from the camera, the state moves to [`ARGeoTrackingStatus.State.localized`](./localized.md) and the app is free to create location anchors. For more information about localization imagery, see [Refine the user’s position with imagery](../../argeotrackingconfiguration.md#Refine-the-users-position-with-imagery).

### Assisting the User with Visual Localization

To establish visual localization, the user must move the camera so it acquires the captures that ARKit needs. To elicit the right user movements in [`ARGeoTrackingStatus.State.localizing`](./localizing.md), the app needs to advise the user to:

- Point the camera at buildings and other visual landmarks to help ARKit match the live camera data with its preexisting landscape-data.
- Avoid pointing the device at objects that are too general, like trees. It’s better to focus on distinct visuals, like structures, or signs.
- Avoid pointing the device at real-world objects that are transient, like parked cars, or a construction site.
- Because lighting conditions can affect visual localization, avoid geo tracking at night.

## See Also

### States
- [ARGeoTrackingStatus.State.initializing](./initializing.md)
  The session is initializing geo tracking.
- [ARGeoTrackingStatus.State.localized](./localized.md)
  Geo tracking is localized.
- [ARGeoTrackingStatus.State.notAvailable](./notavailable.md)
  Geo tracking is not available.
- [ARGeoTrackingStatus.State.initializing](./initializing.md)
  The session is initializing geo tracking.
- [ARGeoTrackingStatus.State.localized](./localized.md)
  Geo tracking is localized.
- [ARGeoTrackingStatus.State.notAvailable](./notavailable.md)
  Geo tracking is not available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/argeotrackingstatus/state-swift.enum/localizing)*