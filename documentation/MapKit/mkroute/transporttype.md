# transportType

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

The overall route transport type.

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
var transportType: MKDirectionsTransportType { get }
```

```objc
@property (nonatomic, readonly) MKDirectionsTransportType transportType;
```

#### Discussion

This property reflects the primary transport type used for the route. Individual steps of the route might use different transport types.

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
- [var expectedTravelTime: TimeInterval](./expectedtraveltime.md)
  The expected travel time, in seconds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkroute/transporttype)*