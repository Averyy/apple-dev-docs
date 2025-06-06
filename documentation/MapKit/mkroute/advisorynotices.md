# advisoryNotices

**Framework**: MapKit  
**Kind**: property

An array of advisory notice strings for the route.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
var advisoryNotices: [String] { get }
```

#### Discussion

This property contains an array of [`NSString`](https://developer.apple.com/documentation/Foundation/NSString) objects. The framework localizes each string according to the user’s language preferences. The strings contain additional information that’s important for the user to know about the route. For example, a string might note the closing of a portion of the route during the winter or after big storms.

## See Also

- [var name: String](mkroute/name.md)
  The assigned name for the route.
- [var hasHighways: Bool](mkroute/hashighways.md)
  A Boolean value that indicates whether the route contains highways.
- [var hasTolls: Bool](mkroute/hastolls.md)
  A Boolean value that indicates whether the route has tolls.
- [var distance: CLLocationDistance](mkroute/distance.md)
  The route distance, in meters.
- [var expectedTravelTime: TimeInterval](mkroute/expectedtraveltime.md)
  The expected travel time, in seconds.
- [var transportType: MKDirectionsTransportType](mkroute/transporttype.md)
  The overall route transport type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkroute/advisorynotices)*