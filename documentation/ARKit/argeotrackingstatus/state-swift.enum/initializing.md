# ARGeoTrackingStatus.State.initializing

**Framework**: ARKit  
**Kind**: case

The session is initializing geo tracking.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
case initializing
```

#### Discussion

In this state, the session is preparing tracking and an app has the opportunity to onboard users to the experience. The app watches for changes in [`stateReason`](argeotrackingstatus/statereason-swift.property.md) and coaches the user accordingly to expedite initialization.

## See Also

- [ARGeoTrackingStatus.State.localized](argeotrackingstatus/state-swift.enum/localized.md)
  Geo tracking is localized.
- [ARGeoTrackingStatus.State.localizing](argeotrackingstatus/state-swift.enum/localizing.md)
  Geo tracking is attempting to localize against a map.
- [ARGeoTrackingStatus.State.notAvailable](argeotrackingstatus/state-swift.enum/notavailable.md)
  Geo tracking is not available.
- [ARGeoTrackingStatus.State.localized](argeotrackingstatus/state-swift.enum/localized.md)
  Geo tracking is localized.
- [ARGeoTrackingStatus.State.localizing](argeotrackingstatus/state-swift.enum/localizing.md)
  Geo tracking is attempting to localize against a map.
- [ARGeoTrackingStatus.State.notAvailable](argeotrackingstatus/state-swift.enum/notavailable.md)
  Geo tracking is not available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/argeotrackingstatus/state-swift.enum/initializing)*