# expectedTravelTime

**Framework**: MapKit  
**Kind**: property

The expected travel time, in seconds.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
var expectedTravelTime: TimeInterval { get }
```

#### Discussion

This expected travel time reflects the time it takes to traverse the route under ideal conditions. The actual amount of time may vary based on conditions.

## See Also

- [var name: String](mkroute/name.md)
  The assigned name for the route.
- [var hasHighways: Bool](mkroute/hashighways.md)
  A Boolean value that indicates whether the route contains highways.
- [var hasTolls: Bool](mkroute/hastolls.md)
  A Boolean value that indicates whether the route has tolls.
- [var advisoryNotices: [String]](mkroute/advisorynotices.md)
  An array of advisory notice strings for the route.
- [var distance: CLLocationDistance](mkroute/distance.md)
  The route distance, in meters.
- [var transportType: MKDirectionsTransportType](mkroute/transporttype.md)
  The overall route transport type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkroute/expectedtraveltime)*