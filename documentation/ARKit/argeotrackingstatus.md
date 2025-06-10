# ARGeoTrackingStatus

**Framework**: ARKit  
**Kind**: class

The state, accuracy, and reason that are possible for geo-tracking’s current condition.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
class ARGeoTrackingStatus
```

#### Overview

Geo tracking requires coordination with the user at various phases of the geo-tracking lifecycle. To elicit the right user actions, an app needs to provide clear instructions to the user based on the current frame’s [`geoTrackingStatus`](arframe/geotrackingstatus.md):

- Geo-tracking [`state`](argeotrackingstatus/state-swift.property.md) most notably regards the important process in which ARKit acquires a better understanding of the user’s geographic location and orientation than is possible with GPS and the compass heading alone. See [`ARGeoTrackingStatus.State.localizing`](argeotrackingstatus/state-swift.enum/localizing.md) for more information.
- Given a particular [`state`](argeotrackingstatus/state-swift.property.md), the app needs to tailor its user messaging according to the [`stateReason`](argeotrackingstatus/statereason-swift.property.md).
- An app may need to monitor [`accuracy`](argeotrackingstatus/accuracy-swift.property.md) closely if it requires high-precision localization.

## Topics

### Checking State
- [var state: ARGeoTrackingStatus.State](argeotrackingstatus/state-swift.property.md)
  A value that describes the session’s current geo-tracking state.
- [ARGeoTrackingStatus.State](argeotrackingstatus/state-swift.enum.md)
  Values that are possible for the current state of geo-tracking.
### Determining the Reason
- [var stateReason: ARGeoTrackingStatus.StateReason](argeotrackingstatus/statereason-swift.property.md)
  The reasons for the app’s geotracking status.
- [ARGeoTrackingStatus.StateReason](argeotrackingstatus/statereason-swift.enum.md)
  The reasons for the app’s geotracking status.
### Judging Accuracy
- [var accuracy: ARGeoTrackingStatus.Accuracy](argeotrackingstatus/accuracy-swift.property.md)
  The accuracy of geo tracking at the time the session captured the frame.
- [ARGeoTrackingStatus.Accuracy](argeotrackingstatus/accuracy-swift.enum.md)
  Values that are possible for the current accuracy of geo tracking.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var geoTrackingStatus: ARGeoTrackingStatus?](arframe/geotrackingstatus.md)
  The session’s condition with respect to geographic tracking at the time the session captured the frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/argeotrackingstatus)*