# resumeNavigation(updatedTrip:routeSegments:currentSegment:rerouteReason:)

**Framework**: CarPlay  
**Kind**: method

Resume navigation with an updated trip and route segments for cases such as the trip destination changing.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
func resumeNavigation(updatedTrip trip: CPTrip, routeSegments: [CPRouteSegment], currentSegment: CPRouteSegment, rerouteReason: CPRerouteReason)
```

## Parameters

- `trip`: The updated trip
- `routeSegments`: The updated route segments for the current trip
- `currentSegment`: The current route segment
- `rerouteReason`: The reason for the reroute


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnavigationsession/resumenavigation(updatedtrip:routesegments:currentsegment:reroutereason:))*