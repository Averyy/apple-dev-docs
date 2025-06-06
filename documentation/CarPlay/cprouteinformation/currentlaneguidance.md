# currentLaneGuidance

**Framework**: CarPlay  
**Kind**: property

A lane guidance object that describes the current lane guidance.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
@NSCopying
var currentLaneGuidance: CPLaneGuidance { get }
```

## See Also

- [var currentManeuvers: [CPManeuver]](cprouteinformation/currentmaneuvers.md)
  An array of maneuver objects that describes the current maneuvers.
- [var laneGuidances: [CPLaneGuidance]](cprouteinformation/laneguidances.md)
  An array of lane guidance objects.
- [var maneuverTravelEstimates: CPTravelEstimates](cprouteinformation/maneuvertravelestimates.md)
  An object that describes the time and distance estimates for a maneuver.
- [var maneuvers: [CPManeuver]](cprouteinformation/maneuvers.md)
  An array of maneuver objects.
- [var tripTravelEstimates: CPTravelEstimates](cprouteinformation/triptravelestimates.md)
  A travel estimates object that describes the estimated time and distance for the current trip.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cprouteinformation/currentlaneguidance)*