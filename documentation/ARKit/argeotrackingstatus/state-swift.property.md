# state

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

A value that describes the session’s current geo-tracking state.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+

## Declaration

```swift
var state: ARGeoTrackingStatus.State { get }
```

```objc
@property (nonatomic, readonly) ARGeoTrackingState state;
```

#### Discussion

For any [`state`](./state-swift.property.md) in a frame’s [`geoTrackingStatus`](../arframe/geotrackingstatus.md), ARKit provides a [`stateReason`](./statereason-swift.property.md). A given geo-tracking status may intermix states and reasons, so the reasons are not tied to specific states.

## See Also

### Checking State
- [ARGeoTrackingStatus.State](./state-swift.enum.md)
  Values that are possible for the current state of geo-tracking.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/argeotrackingstatus/state-swift.property)*