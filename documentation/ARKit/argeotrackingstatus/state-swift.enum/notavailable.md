# ARGeoTrackingStatus.State.notAvailable

**Framework**: ARKit  
**Kind**: case

Geo tracking is not available.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
case notAvailable
```

#### Discussion

This state occurs when ARKit doesn’t have the landscape data necessary for visual localization at the user’s location. For more information, see [`ARGeoTrackingStatus.State.localizing`](argeotrackingstatus/state-swift.enum/localizing.md).

## See Also

- [ARGeoTrackingStatus.State.initializing](argeotrackingstatus/state-swift.enum/initializing.md)
  The session is initializing geo tracking.
- [ARGeoTrackingStatus.State.localized](argeotrackingstatus/state-swift.enum/localized.md)
  Geo tracking is localized.
- [ARGeoTrackingStatus.State.localizing](argeotrackingstatus/state-swift.enum/localizing.md)
  Geo tracking is attempting to localize against a map.
- [ARGeoTrackingStatus.State.initializing](argeotrackingstatus/state-swift.enum/initializing.md)
  The session is initializing geo tracking.
- [ARGeoTrackingStatus.State.localized](argeotrackingstatus/state-swift.enum/localized.md)
  Geo tracking is localized.
- [ARGeoTrackingStatus.State.localizing](argeotrackingstatus/state-swift.enum/localizing.md)
  Geo tracking is attempting to localize against a map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/argeotrackingstatus/state-swift.enum/notavailable)*