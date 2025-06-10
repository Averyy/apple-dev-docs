# distance

**Framework**: MapKit  
**Kind**: property

The route distance, in meters.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
var distance: CLLocationDistance { get }
```

#### Discussion

This property reflects the distance that the user covers while traversing the path of the route. It’s not a linear distance between the start and end points of the route.

## See Also

- [var name: String](mkroute/name.md)
  The assigned name for the route.
- [var hasHighways: Bool](mkroute/hashighways.md)
  A Boolean value that indicates whether the route contains highways.
- [var hasTolls: Bool](mkroute/hastolls.md)
  A Boolean value that indicates whether the route has tolls.
- [var advisoryNotices: [String]](mkroute/advisorynotices.md)
  An array of advisory notice strings for the route.
- [var expectedTravelTime: TimeInterval](mkroute/expectedtraveltime.md)
  The expected travel time, in seconds.
- [var transportType: MKDirectionsTransportType](mkroute/transporttype.md)
  The overall route transport type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkroute/distance)*