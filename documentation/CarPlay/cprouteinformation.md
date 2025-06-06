# CPRouteInformation

**Framework**: CarPlay  
**Kind**: class

A class that describes the characteristic elements of a route.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
class CPRouteInformation
```

## Topics

### Initializers
- [init(maneuvers: [CPManeuver], laneGuidances: [CPLaneGuidance], currentManeuvers: [CPManeuver], currentLaneGuidance: CPLaneGuidance, trip: CPTravelEstimates, maneuverTravelEstimates: CPTravelEstimates)](cprouteinformation/init(maneuvers:laneguidances:currentmaneuvers:currentlaneguidance:trip:maneuvertravelestimates:).md)
  Initializes a new route information object with maneuvers, lane guidances, the current maneuvers, the current lane guidance, and trip and current maneuver travel estimates.
### Properties
- [var currentLaneGuidance: CPLaneGuidance](cprouteinformation/currentlaneguidance.md)
  A lane guidance object that describes the current lane guidance.
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

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class CPLane](cplane.md)
  A class that describes characteristics of a lane on a roadway.
- [class CPLaneGuidance](cplaneguidance.md)
  A class that provides information that describes the number of lanes on a roadway and navigation instruction variants.
- [enum CPLaneStatus](cplanestatus.md)
  Values that describe the status or preferability of a lane.
- [enum CPJunctionType](cpjunctiontype.md)
  Values that represent types of roadway junctions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cprouteinformation)*