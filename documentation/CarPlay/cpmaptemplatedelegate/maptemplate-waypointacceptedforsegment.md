# mapTemplate(_:waypoint:accepted:forSegment:)

**Framework**: CarPlay  
**Kind**: method

Called when the user responds to a proposal to add a waypoint as a stop on their route. If the waypoint is accepted, perform a reroute to update the route accordingly for the specified segment to include this new destination.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)
- Mac Catalyst 26.4+ (Beta)

## Declaration

```swift
optional func mapTemplate(_ mapTemplate: CPMapTemplate, waypoint: CPNavigationWaypoint, accepted: Bool, forSegment segment: CPRouteSegment?)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaptemplatedelegate/maptemplate(_:waypoint:accepted:forsegment:))*