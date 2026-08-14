# ARGeoTrackingStatus.State

**Framework**: ARKit  
**Kind**: enum

Values that are possible for the current state of geo-tracking.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+

## Declaration

```swift
enum State
```

#### Discussion

For any [`state`](argeotrackingstatus/state-swift.property.md) in a frame’s [`geoTrackingStatus`](arframe/geotrackingstatus.md), ARKit provides a [`stateReason`](argeotrackingstatus/statereason-swift.property.md). A given geo-tracking status may intermix states and reasons, so the reasons are not tied to specific states.

## Topics

### States
- [ARGeoTrackingStatus.State.initializing](argeotrackingstatus/state-swift.enum/initializing.md)
  The session is initializing geo tracking.
- [ARGeoTrackingStatus.State.localized](argeotrackingstatus/state-swift.enum/localized.md)
  Geo tracking is localized.
- [ARGeoTrackingStatus.State.localizing](argeotrackingstatus/state-swift.enum/localizing.md)
  Geo tracking is attempting to localize against a map.
- [ARGeoTrackingStatus.State.notAvailable](argeotrackingstatus/state-swift.enum/notavailable.md)
  Geo tracking is not available.
- [ARGeoTrackingStatus.State.initializing](argeotrackingstatus/state-swift.enum/initializing.md)
  The session is initializing geo tracking.
- [ARGeoTrackingStatus.State.localized](argeotrackingstatus/state-swift.enum/localized.md)
  Geo tracking is localized.
- [ARGeoTrackingStatus.State.localizing](argeotrackingstatus/state-swift.enum/localizing.md)
  Geo tracking is attempting to localize against a map.
- [ARGeoTrackingStatus.State.notAvailable](argeotrackingstatus/state-swift.enum/notavailable.md)
  Geo tracking is not available.
### Initializers
- [init?(rawValue: Int)](argeotrackingstatus/state-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var state: ARGeoTrackingStatus.State](argeotrackingstatus/state-swift.property.md)
  A value that describes the session’s current geo-tracking state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/argeotrackingstatus/state-swift.enum)*