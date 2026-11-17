# mapTemplate(_:didRequestToRemove:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Called when the user removes a waypoint. Perform a reroute to update the route accordingly.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
optional func mapTemplate(_ mapTemplate: CPMapTemplate, didRequestToRemove waypoint: CPNavigationWaypoint)
```

```objc
- (void) mapTemplate:(CPMapTemplate *) mapTemplate didRequestToRemoveWaypoint:(CPNavigationWaypoint *) waypoint;
```

## See Also

### Adding and removing waypoints
- [func mapTemplate(CPMapTemplate, didRequestToInsert: CPNavigationWaypoint, into: CPRouteSegment, completion: (CPTravelEstimates) -> Void)](./maptemplate%28_,didrequesttoinsert,into,completion%29.md)
  Called when the built-in navigation system sends a waypoint to the device for a specific segment.
- [func mapTemplate(CPMapTemplate, waypoint: CPNavigationWaypoint, accepted: Bool, forSegment: CPRouteSegment?)](./maptemplate%28_,waypoint,accepted,forsegment%29.md)
  Called when the user responds to a proposal to add a waypoint as a stop on their route. If the waypoint is accepted, perform a reroute to update the route accordingly for the specified segment to include this new destination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaptemplatedelegate/maptemplate(_:didrequesttoremove:))*