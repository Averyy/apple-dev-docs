# state

**Framework**: ARKit  
**Kind**: property

A value that describes the session’s current geo-tracking state.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var state: ARGeoTrackingStatus.State { get }
```

#### Discussion

For any [`state`](argeotrackingstatus/state-swift.property.md) in a frame’s [`geoTrackingStatus`](arframe/geotrackingstatus.md), ARKit provides a [`stateReason`](argeotrackingstatus/statereason-swift.property.md). A given geo-tracking status may intermix states and reasons, so the reasons are not tied to specific states.

## See Also

- [ARGeoTrackingStatus.State](argeotrackingstatus/state-swift.enum.md)
  Values that are possible for the current state of geo-tracking.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/argeotrackingstatus/state-swift.property)*