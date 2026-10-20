# expectedTravelTime

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

The expected travel time, in seconds.

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
var expectedTravelTime: TimeInterval { get }
```

```objc
@property (nonatomic, readonly) NSTimeInterval expectedTravelTime;
```

#### Discussion

This expected travel time reflects the time it takes to traverse the route under ideal conditions. The actual amount of time may vary based on conditions.

## See Also

### Getting additional route details
- [var name: String](./name.md)
  The assigned name for the route.
- [var hasHighways: Bool](./hashighways.md)
  A Boolean value that indicates whether the route contains highways.
- [var hasTolls: Bool](./hastolls.md)
  A Boolean value that indicates whether the route has tolls.
- [var advisoryNotices: [String]](./advisorynotices.md)
  An array of advisory notice strings for the route.
- [var distance: CLLocationDistance](./distance.md)
  The route distance, in meters.
- [var transportType: MKDirectionsTransportType](./transporttype.md)
  The overall route transport type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkroute/expectedtraveltime)*