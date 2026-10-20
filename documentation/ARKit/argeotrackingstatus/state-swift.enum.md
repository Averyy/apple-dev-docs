# ARGeoTrackingStatus.State

**Framework**: ARKit  
**Kind**: enum  
**Role**: Enumeration

Values that are possible for the current state of geo-tracking.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+

## Declaration

```swift
enum State
```

```c
enum ARGeoTrackingState : NSInteger;
```

#### Discussion

For any [`state`](./state-swift.property.md) in a frame’s [`geoTrackingStatus`](../arframe/geotrackingstatus.md), ARKit provides a [`stateReason`](./statereason-swift.property.md). A given geo-tracking status may intermix states and reasons, so the reasons are not tied to specific states.

## Topics

### States
- [ARGeoTrackingStatus.State.initializing](./state-swift.enum/initializing.md)
  The session is initializing geo tracking.
- [ARGeoTrackingStatus.State.localized](./state-swift.enum/localized.md)
  Geo tracking is localized.
- [ARGeoTrackingStatus.State.localizing](./state-swift.enum/localizing.md)
  Geo tracking is attempting to localize against a map.
- [ARGeoTrackingStatus.State.notAvailable](./state-swift.enum/notavailable.md)
  Geo tracking is not available.
- [ARGeoTrackingStatus.State.initializing](./state-swift.enum/initializing.md)
  The session is initializing geo tracking.
- [ARGeoTrackingStatus.State.localized](./state-swift.enum/localized.md)
  Geo tracking is localized.
- [ARGeoTrackingStatus.State.localizing](./state-swift.enum/localizing.md)
  Geo tracking is attempting to localize against a map.
- [ARGeoTrackingStatus.State.notAvailable](./state-swift.enum/notavailable.md)
  Geo tracking is not available.
### Initializers
- [init?(rawValue: Int)](./state-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Checking State
- [var state: ARGeoTrackingStatus.State](./state-swift.property.md)
  A value that describes the session’s current geo-tracking state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/argeotrackingstatus/state-swift.enum)*