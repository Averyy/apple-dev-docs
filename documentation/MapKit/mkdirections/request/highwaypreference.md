# highwayPreference

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

The value that indicates whether the framework uses or avoids highways when providing directions.

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
var highwayPreference: MKDirections.RoutePreference { get set }
```

```objc
@property (nonatomic) MKDirectionsRoutePreference highwayPreference;
```

## See Also

### Specifying transportation options
- [var transportType: MKDirectionsTransportType](./transporttype.md)
  The type of conveyance that the directions apply to.
- [var tollPreference: MKDirections.RoutePreference](./tollpreference.md)
  The value that indicates whether the framework avoids routes that have tolls when providing directions.
- [MKDirections.RoutePreference](../routepreference.md)
  Options that modify how the framework selects routes when calculating directions.
- [var requestsAlternateRoutes: Bool](./requestsalternateroutes.md)
  A Boolean value that indicates whether your app requests multiple routes when they’re available.
- [var departureDate: Date?](./departuredate.md)
  The departure date for the trip.
- [var arrivalDate: Date?](./arrivaldate.md)
  The arrival date for the trip.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkdirections/request/highwaypreference)*