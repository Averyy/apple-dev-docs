# mapTemplate(_:didRequestToInsert:into:completion:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Called when the built-in navigation system sends a waypoint to the device for a specific segment.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
optional func mapTemplate(_ mapTemplate: CPMapTemplate, didRequestToInsert waypoint: CPNavigationWaypoint, into segment: CPRouteSegment, completion: @escaping (CPTravelEstimates) -> Void)
```

```swift
optional func mapTemplate(_ mapTemplate: CPMapTemplate, didRequestToInsert waypoint: CPNavigationWaypoint, into segment: CPRouteSegment) async -> CPTravelEstimates
```

```objc
- (void) mapTemplate:(CPMapTemplate *) mapTemplate didRequestToInsertWaypoint:(CPNavigationWaypoint *) waypoint intoSegment:(CPRouteSegment *) segment completion:(void (^)(CPTravelEstimates *travelEstimates)) completion;
```

## See Also

### Adding and removing waypoints
- [func mapTemplate(CPMapTemplate, didRequestToRemove: CPNavigationWaypoint)](./maptemplate%28_,didrequesttoremove%29.md)
  Called when the user removes a waypoint. Perform a reroute to update the route accordingly.
- [func mapTemplate(CPMapTemplate, waypoint: CPNavigationWaypoint, accepted: Bool, forSegment: CPRouteSegment?)](./maptemplate%28_,waypoint,accepted,forsegment%29.md)
  Called when the user responds to a proposal to add a waypoint as a stop on their route. If the waypoint is accepted, perform a reroute to update the route accordingly for the specified segment to include this new destination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaptemplatedelegate/maptemplate(_:didrequesttoinsert:into:completion:))*