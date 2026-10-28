# transportType

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

The type of conveyance that the directions apply to.

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
var transportType: MKDirectionsTransportType { get set }
```

```objc
@property (nonatomic) MKDirectionsTransportType transportType;
```

## Discussion

You can use this property to specify whether you want directions suited to a particular type of transportation. For example, you can use this to specify that you want walking directions or driving directions.

The default value of this property is [`any`](../../mkdirectionstransporttype/any.md).

## See Also

### Specifying transportation options
- [var highwayPreference: MKDirections.RoutePreference](./highwaypreference.md)
  The value that indicates whether the framework uses or avoids highways when providing directions.
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

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkdirections/request/transporttype)*