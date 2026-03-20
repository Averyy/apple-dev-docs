# mapTemplate(_:didRequestToInsert:into:completion:)

**Framework**: CarPlay  
**Kind**: method

Called when the built-in navigation system sends a waypoint to the device for a specific segment.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
optional func mapTemplate(_ mapTemplate: CPMapTemplate, didRequestToInsert waypoint: CPNavigationWaypoint, into segment: CPRouteSegment) async -> CPTravelEstimates
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaptemplatedelegate/maptemplate(_:didrequesttoinsert:into:completion:))*