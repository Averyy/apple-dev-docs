# requestsAlternateRoutes

**Framework**: MapKit JS  
**Kind**: property

A Boolean value that indicates whether the server returns multiple routes when they’re available.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
requestsAlternateRoutes?: boolean;
```

#### Discussion

When this property is `false`, the server returns a single route between the start and end points. When this property is `true`, the server may return additional routes for the user to follow. The server returns additional routes only if they’re available and represent a reasonable path that the user might take.

The default value of this property is `true`.

## See Also

- [origin](directionsrequest/origin.md)
  The starting point for routing directions.
- [destination](directionsrequest/destination.md)
  The end point for routing directions.
- [arrivalDate](directionsrequest/arrivaldate.md)
  The arrival date for the trip.
- [departureDate](directionsrequest/departuredate.md)
  The departure date for the trip.
- [transportType](directionsrequest/transporttype.md)
  The mode of transportation the directions apply to.
- [avoidTolls](directionsrequest/avoidtolls.md)
  A Boolean value that prioritizes routes to avoid tolls.
- [const TransportType](transporttype.md)
  The modes of transportation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/directionsrequest/requestsalternateroutes)*