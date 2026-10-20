# maneuvers

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

An array of maneuver objects.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
var maneuvers: [CPManeuver] { get }
```

```objc
@property (nonatomic, copy, readonly) NSArray<CPManeuver *> * maneuvers;
```

## See Also

### Properties
- [var currentLaneGuidance: CPLaneGuidance](./currentlaneguidance.md)
  A lane guidance object that describes the current lane guidance.
- [var currentManeuvers: [CPManeuver]](./currentmaneuvers.md)
  An array of maneuver objects that describes the current maneuvers.
- [var laneGuidances: [CPLaneGuidance]](./laneguidances.md)
  An array of lane guidance objects.
- [var maneuverTravelEstimates: CPTravelEstimates](./maneuvertravelestimates.md)
  An object that describes the time and distance estimates for a maneuver.
- [var tripTravelEstimates: CPTravelEstimates](./triptravelestimates.md)
  A travel estimates object that describes the estimated time and distance for the current trip.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cprouteinformation/maneuvers)*