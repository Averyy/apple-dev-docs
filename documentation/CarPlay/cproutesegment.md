# CPRouteSegment

**Framework**: CarPlay  
**Kind**: class

CPRouteSegment describes information pertaining to a segment of a route.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
class CPRouteSegment
```

## Topics

### Initializers
- [convenience init(origin: CPNavigationWaypoint, destination: CPNavigationWaypoint, maneuvers: [CPManeuver], laneGuidances: [CPLaneGuidance], currentManeuvers: [CPManeuver], currentLaneGuidance: CPLaneGuidance, tripTravelEstimates: CPTravelEstimates, maneuverTravelEstimates: CPTravelEstimates, coordinates: [CPLocationCoordinate3D])](cproutesegment/init(origin:destination:maneuvers:laneguidances:currentmaneuvers:currentlaneguidance:triptravelestimates:maneuvertravelestimates:coordinates:).md)
### Instance Properties
- [var coordinates: [CPLocationCoordinate3D]](cproutesegment/coordinates-8o5b.md)
- [var currentLaneGuidance: CPLaneGuidance](cproutesegment/currentlaneguidance.md)
  currentLaneGuidance is a CPLaneGuidance object, describing the current lane guidance.
- [var currentManeuvers: [CPManeuver]](cproutesegment/currentmaneuvers.md)
  currentManeuvers is an array of CPManeuver objects, describing the current maneuvers.
- [var destination: CPNavigationWaypoint](cproutesegment/destination.md)
  destination is a CPNavigationWaypoint, describing the destination of the segment.
- [var identifier: UUID](cproutesegment/identifier.md)
  identifier is a NSUUID that uniquely identifies this route segment.
- [var laneGuidances: [CPLaneGuidance]](cproutesegment/laneguidances.md)
  laneGuidances is an array of CPLaneGuidance objects, each describes a single lane guidance.
- [var maneuverTravelEstimates: CPTravelEstimates](cproutesegment/maneuvertravelestimates.md)
  maneuverTravelEstimates is a CPTravelEstimates object, describing the travel estimates for the first maneuver in the list of current maneuvers.
- [var maneuvers: [CPManeuver]](cproutesegment/maneuvers.md)
  maneuvers is an array of CPManeuver objects, each describes a single maneuver.
- [var origin: CPNavigationWaypoint](cproutesegment/origin.md)
  origin is a CPNavigationWaypoint, describing the origin of the segment.
- [var tripTravelEstimates: CPTravelEstimates](cproutesegment/triptravelestimates.md)
  tripTravelEstimates is a CPTravelEstimates object, describing the travel estimates for the current trip.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cproutesegment)*