# requestsAlternateRoutes

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether your app requests multiple routes when they’re available.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var requestsAlternateRoutes: Bool { get set }
```

```objc
@property (nonatomic) BOOL requestsAlternateRoutes;
```

#### Discussion

When this property is [`false`](../../../Swift/false.md), the server returns a single route between the start and end points. When this property is [`true`](../../../Swift/true.md), the server may return additional routes for the user to follow. The server returns additional routes only if they’re available and represent a reasonable path that the user might take.

The default value of this property is [`false`](../../../Swift/false.md).

## See Also

### Specifying transportation options
- [var transportType: MKDirectionsTransportType](./transporttype.md)
  The type of conveyance that the directions apply to.
- [var highwayPreference: MKDirections.RoutePreference](./highwaypreference.md)
  The value that indicates whether the framework uses or avoids highways when providing directions.
- [var tollPreference: MKDirections.RoutePreference](./tollpreference.md)
  The value that indicates whether the framework avoids routes that have tolls when providing directions.
- [MKDirections.RoutePreference](../routepreference.md)
  Options that modify how the framework selects routes when calculating directions.
- [var departureDate: Date?](./departuredate.md)
  The departure date for the trip.
- [var arrivalDate: Date?](./arrivaldate.md)
  The arrival date for the trip.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkdirections/request/requestsalternateroutes)*