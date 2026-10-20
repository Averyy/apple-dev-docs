# hasTolls

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the route has tolls.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var hasTolls: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL hasTolls;
```

## See Also

### Getting additional route details
- [var name: String](./name.md)
  The assigned name for the route.
- [var hasHighways: Bool](./hashighways.md)
  A Boolean value that indicates whether the route contains highways.
- [var advisoryNotices: [String]](./advisorynotices.md)
  An array of advisory notice strings for the route.
- [var distance: CLLocationDistance](./distance.md)
  The route distance, in meters.
- [var expectedTravelTime: TimeInterval](./expectedtraveltime.md)
  The expected travel time, in seconds.
- [var transportType: MKDirectionsTransportType](./transporttype.md)
  The overall route transport type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkroute/hastolls)*