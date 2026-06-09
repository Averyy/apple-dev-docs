# init(trafficLights:)

**Framework**: CarPlay  
**Kind**: init

Creates additional route information for the number of traffic lights along the route.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
convenience init(trafficLights: Int)
```

#### Return Value

A new @c CPRouteDetail instance representing the traffic light count

#### Discussion

Use this method to display the count of traffic signals that will be encountered along the route. This helps users understand potential stop-and-go traffic patterns and estimate realistic travel time.

Traffic light count provides valuable context for route selection, especially in urban areas where signal timing can significantly impact travel time. Routes with fewer traffic lights may offer smoother travel despite similar distances.

> **Note**: The count should include all signalized intersections where the route requires stopping or yielding. Consider excluding traffic lights on cross streets that don’t affect the route. This information pairs well with travel time estimates to help users understand route flow.

## Parameters

- `trafficLights`: The number of traffic lights along the route. Common values range from 0 to 50+ for typical urban routes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cproutedetail/init(trafficlights:))*