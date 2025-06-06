# geoTrackingStatus

**Framework**: ARKit  
**Kind**: property

The session’s condition with respect to geographic tracking at the time the session captured the frame.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var geoTrackingStatus: ARGeoTrackingStatus? { get }
```

#### Discussion

For the current geo-tracking status, check the value of this property on the session’s [`currentFrame`](arsession/currentframe.md). ARKit populates this property only for [`ARGeoTrackingConfiguration`](argeotrackingconfiguration.md) sessions.

## See Also

- [class ARGeoTrackingStatus](argeotrackingstatus.md)
  The state, accuracy, and reason that are possible for geo-tracking’s current condition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arframe/geotrackingstatus)*