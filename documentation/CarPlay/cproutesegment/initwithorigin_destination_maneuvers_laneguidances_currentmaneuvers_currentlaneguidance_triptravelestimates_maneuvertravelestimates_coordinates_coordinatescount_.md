# initWithOrigin:destination:maneuvers:laneGuidances:currentManeuvers:currentLaneGuidance:tripTravelEstimates:maneuverTravelEstimates:coordinates:coordinatesCount:

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Initialize a CPRouteSegment object with maneuvers, lane guidances, the current maneuvers, the current lane guidance, trip travel estimates, the current maneuver travel estimates, the origin and the destination. If the current trip supports route sharing, also provide coordinates along the current segment.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```objc
- (instancetype) initWithOrigin:(CPNavigationWaypoint *) origin destination:(CPNavigationWaypoint *) destination maneuvers:(NSArray<CPManeuver *> *) maneuvers laneGuidances:(NSArray<CPLaneGuidance *> *) laneGuidances currentManeuvers:(NSArray<CPManeuver *> *) currentManeuvers currentLaneGuidance:(CPLaneGuidance *) currentLaneGuidance tripTravelEstimates:(CPTravelEstimates *) tripTravelEstimates maneuverTravelEstimates:(CPTravelEstimates *) maneuverTravelEstimates coordinates:(CPLocationCoordinate3D *) coordinates coordinatesCount:(NSInteger) coordinatesCount;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cproutesegment/initwithorigin:destination:maneuvers:laneguidances:currentmaneuvers:currentlaneguidance:triptravelestimates:maneuvertravelestimates:coordinates:coordinatescount:)*