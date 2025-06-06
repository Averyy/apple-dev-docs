# name

**Framework**: MapKit  
**Kind**: property

The assigned name for the route.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
var name: String { get }
```

#### Discussion

The framework localizes the string in this property according to the user’s language preferences. You can display this string to the user from your app’s user interface so that the user can distinguish one route from another.

The string itself describes the route using one of the route’s significant features. For example, a route that uses a major highway for a significant portion of the route might use that highway for its name.

## See Also

- [var hasHighways: Bool](mkroute/hashighways.md)
  A Boolean value that indicates whether the route contains highways.
- [var hasTolls: Bool](mkroute/hastolls.md)
  A Boolean value that indicates whether the route has tolls.
- [var advisoryNotices: [String]](mkroute/advisorynotices.md)
  An array of advisory notice strings for the route.
- [var distance: CLLocationDistance](mkroute/distance.md)
  The route distance, in meters.
- [var expectedTravelTime: TimeInterval](mkroute/expectedtraveltime.md)
  The expected travel time, in seconds.
- [var transportType: MKDirectionsTransportType](mkroute/transporttype.md)
  The overall route transport type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkroute/name)*