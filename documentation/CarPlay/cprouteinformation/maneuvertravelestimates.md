# maneuverTravelEstimates

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

An object that describes the time and distance estimates for a maneuver.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
@NSCopying
var maneuverTravelEstimates: CPTravelEstimates { get }
```

```objc
@property (nonatomic, copy, readonly) CPTravelEstimates * maneuverTravelEstimates;
```

### Discussion

This is the first maneuver in the current list of maneuvers.

## See Also

### Properties
- [var currentLaneGuidance: CPLaneGuidance](./currentlaneguidance.md)
  A lane guidance object that describes the current lane guidance.
- [var currentManeuvers: [CPManeuver]](./currentmaneuvers.md)
  An array of maneuver objects that describes the current maneuvers.
- [var laneGuidances: [CPLaneGuidance]](./laneguidances.md)
  An array of lane guidance objects.
- [var maneuvers: [CPManeuver]](./maneuvers.md)
  An array of maneuver objects.
- [var tripTravelEstimates: CPTravelEstimates](./triptravelestimates.md)
  A travel estimates object that describes the estimated time and distance for the current trip.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cprouteinformation/maneuvertravelestimates)*