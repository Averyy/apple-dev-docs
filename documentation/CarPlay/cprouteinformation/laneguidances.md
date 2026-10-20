# laneGuidances

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

An array of lane guidance objects.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
var laneGuidances: [CPLaneGuidance] { get }
```

```objc
@property (nonatomic, copy, readonly) NSArray<CPLaneGuidance *> * laneGuidances;
```

## See Also

### Properties
- [var currentLaneGuidance: CPLaneGuidance](./currentlaneguidance.md)
  A lane guidance object that describes the current lane guidance.
- [var currentManeuvers: [CPManeuver]](./currentmaneuvers.md)
  An array of maneuver objects that describes the current maneuvers.
- [var maneuverTravelEstimates: CPTravelEstimates](./maneuvertravelestimates.md)
  An object that describes the time and distance estimates for a maneuver.
- [var maneuvers: [CPManeuver]](./maneuvers.md)
  An array of maneuver objects.
- [var tripTravelEstimates: CPTravelEstimates](./triptravelestimates.md)
  A travel estimates object that describes the estimated time and distance for the current trip.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cprouteinformation/laneguidances)*