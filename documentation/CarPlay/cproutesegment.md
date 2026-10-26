# CPRouteSegment

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

CPRouteSegment describes information pertaining to a segment of a route.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
class CPRouteSegment
```

```objc
@interface CPRouteSegment : NSObject
```

## Topics

### Initializers
- [convenience init(origin: CPNavigationWaypoint, destination: CPNavigationWaypoint, maneuvers: [CPManeuver], laneGuidances: [CPLaneGuidance], currentManeuvers: [CPManeuver], currentLaneGuidance: CPLaneGuidance, tripTravelEstimates: CPTravelEstimates, maneuverTravelEstimates: CPTravelEstimates, coordinates: [CPLocationCoordinate3D])](./cproutesegment/init%28origin,destination,maneuvers,laneguidances,currentmaneuvers,currentlaneguidance,triptravelestimates,maneuvertravelestimates,coordinates%29.md)
### Instance Properties
- [var coordinates: [CPLocationCoordinate3D]](./cproutesegment/coordinates-8o5b.md)
- [var currentLaneGuidance: CPLaneGuidance](./cproutesegment/currentlaneguidance.md)
  currentLaneGuidance is a CPLaneGuidance object, describing the current lane guidance.
- [var currentManeuvers: [CPManeuver]](./cproutesegment/currentmaneuvers.md)
  currentManeuvers is an array of CPManeuver objects, describing the current maneuvers.
- [var destination: CPNavigationWaypoint](./cproutesegment/destination.md)
  destination is a CPNavigationWaypoint, describing the destination of the segment.
- [var identifier: UUID](./cproutesegment/identifier.md)
  identifier is a NSUUID that uniquely identifies this route segment.
- [var laneGuidances: [CPLaneGuidance]](./cproutesegment/laneguidances.md)
  laneGuidances is an array of CPLaneGuidance objects, each describes a single lane guidance.
- [var maneuverTravelEstimates: CPTravelEstimates](./cproutesegment/maneuvertravelestimates.md)
  maneuverTravelEstimates is a CPTravelEstimates object, describing the travel estimates for the first maneuver in the list of current maneuvers.
- [var maneuvers: [CPManeuver]](./cproutesegment/maneuvers.md)
  maneuvers is an array of CPManeuver objects, each describes a single maneuver.
- [var origin: CPNavigationWaypoint](./cproutesegment/origin.md)
  origin is a CPNavigationWaypoint, describing the origin of the segment.
- [var tripTravelEstimates: CPTravelEstimates](./cproutesegment/triptravelestimates.md)
  tripTravelEstimates is a CPTravelEstimates object, describing the travel estimates for the current trip.
- [coordinates](./cproutesegment/coordinates-9mw42.md)
  coordinates is an array of CPLocationCoordinate3D, describing coordinates along the segment.
- [coordinatesCount](./cproutesegment/coordinatescount.md)
  coordinatesCount is an integer, describing the number of coordinates along the segment.
### Instance Methods
- [- initWithOrigin:destination:maneuvers:laneGuidances:currentManeuvers:currentLaneGuidance:tripTravelEstimates:maneuverTravelEstimates:coordinates:coordinatesCount:](./cproutesegment/initwithorigin_destination_maneuvers_laneguidances_currentmaneuvers_currentlaneguidance_triptravelestimates_maneuvertravelestimates_coordinates_coordinatescount_.md)
  Initialize a CPRouteSegment object with maneuvers, lane guidances, the current maneuvers, the current lane guidance, trip travel estimates, the current maneuver travel estimates, the origin and the destination. If the current trip supports route sharing, also provide coordinates along the current segment.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cproutesegment)*