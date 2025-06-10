# departureDate

**Framework**: MapKit  
**Kind**: property

The departure date for the trip.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var departureDate: Date? { get set }
```

#### Discussion

Specifying a departure date provides the server with extra information that it can use to optimize the returned routes. For example, for a trip that takes place during commute hours, the server might consider alternatives to routes that are typically congested at that time.

The use of this property is optional.

## See Also

- [var transportType: MKDirectionsTransportType](mkdirections/request/transporttype.md)
  The type of conveyance that the directions apply to.
- [var highwayPreference: MKDirections.RoutePreference](mkdirections/request/highwaypreference.md)
  The value that indicates whether the framework uses or avoids highways when providing directions.
- [var tollPreference: MKDirections.RoutePreference](mkdirections/request/tollpreference.md)
  The value that indicates whether the framework avoids routes that have tolls when providing directions.
- [MKDirections.RoutePreference](mkdirections/routepreference.md)
  Options that modify how the framework selects routes when calculating directions.
- [var requestsAlternateRoutes: Bool](mkdirections/request/requestsalternateroutes.md)
  A Boolean value that indicates whether your app requests multiple routes when they’re available.
- [var arrivalDate: Date?](mkdirections/request/arrivaldate.md)
  The arrival date for the trip.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkdirections/request/departuredate)*