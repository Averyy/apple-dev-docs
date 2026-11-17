# mapTemplate(_:waypoint:accepted:forSegment:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Called when the user responds to a proposal to add a waypoint as a stop on their route. If the waypoint is accepted, perform a reroute to update the route accordingly for the specified segment to include this new destination.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
optional func mapTemplate(_ mapTemplate: CPMapTemplate, waypoint: CPNavigationWaypoint, accepted: Bool, forSegment segment: CPRouteSegment?)
```

```objc
- (void) mapTemplate:(CPMapTemplate *) mapTemplate mapTemplateWaypoint:(CPNavigationWaypoint *) waypoint accepted:(BOOL) accepted forSegment:(CPRouteSegment *) segment;
```

## See Also

### Adding and removing waypoints
- [func mapTemplate(CPMapTemplate, didRequestToInsert: CPNavigationWaypoint, into: CPRouteSegment, completion: (CPTravelEstimates) -> Void)](./maptemplate%28_,didrequesttoinsert,into,completion%29.md)
  Called when the built-in navigation system sends a waypoint to the device for a specific segment.
- [func mapTemplate(CPMapTemplate, didRequestToRemove: CPNavigationWaypoint)](./maptemplate%28_,didrequesttoremove%29.md)
  Called when the user removes a waypoint. Perform a reroute to update the route accordingly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaptemplatedelegate/maptemplate(_:waypoint:accepted:forsegment:))*