# highwayPreference

**Framework**: MapKit  
**Kind**: property

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

## See Also

- [var transportType: MKDirectionsTransportType](mkdirections/request/transporttype.md)
  The type of conveyance that the directions apply to.
- [var tollPreference: MKDirections.RoutePreference](mkdirections/request/tollpreference.md)
  The value that indicates whether the framework avoids routes that have tolls when providing directions.
- [MKDirections.RoutePreference](mkdirections/routepreference.md)
  Options that modify how the framework selects routes when calculating directions.
- [var requestsAlternateRoutes: Bool](mkdirections/request/requestsalternateroutes.md)
  A Boolean value that indicates whether your app requests multiple routes when they’re available.
- [var departureDate: Date?](mkdirections/request/departuredate.md)
  The departure date for the trip.
- [var arrivalDate: Date?](mkdirections/request/arrivaldate.md)
  The arrival date for the trip.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkdirections/request/highwaypreference)*