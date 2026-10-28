# ARGeoTrackingStatus.State.localized

**Framework**: ARKit  
**Kind**: case  
**Role**: Case

Geo tracking is localized.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+

## Declaration

```swift
case localized
```

```c
ARGeoTrackingStateLocalized
```

## Discussion

In [`ARGeoTrackingStatus.State.localized`](./localized.md), ARKit has completed visual localization and the app is free to place location anchors ([`ARGeoAnchor`](../../argeoanchor.md)).

## See Also

### States
- [ARGeoTrackingStatus.State.initializing](./initializing.md)
  The session is initializing geo tracking.
- [ARGeoTrackingStatus.State.localizing](./localizing.md)
  Geo tracking is attempting to localize against a map.
- [ARGeoTrackingStatus.State.notAvailable](./notavailable.md)
  Geo tracking is not available.
- [ARGeoTrackingStatus.State.initializing](./initializing.md)
  The session is initializing geo tracking.
- [ARGeoTrackingStatus.State.localizing](./localizing.md)
  Geo tracking is attempting to localize against a map.
- [ARGeoTrackingStatus.State.notAvailable](./notavailable.md)
  Geo tracking is not available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/argeotrackingstatus/state-swift.enum/localized)*