# init(hov:)

**Framework**: CarPlay  
**Kind**: init

Creates additional route information for High-Occupancy Vehicle (HOV) lane access.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
convenience init(hov hovInfo: String)
```

#### Return Value

A new @c CPRouteDetail instance representing HOV lane information

#### Discussion

Use this method to display information about HOV lane eligibility and requirements for the route. This helps users understand whether they can use faster HOV lanes based on vehicle occupancy.

HOV information is valuable for users planning carpools or understanding time savings from using HOV lanes. Display requirements such as minimum passenger count or time restrictions.

> **Note**: Ensure HOV information is accurate for the specific route and time of day, as restrictions often vary by time and location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cproutedetail/init(hov:)-6ivii)*