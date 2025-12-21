# avoidTolls

**Framework**: MapKit JS  
**Kind**: property

A Boolean value that prioritizes routes to avoid tolls.

**Availability**:
- MapKit JS 5.72+

## Declaration

```swift
avoidTolls?: boolean;
```

#### Discussion

Set this value to `true` to prioritize routes that don’t have any tolls. The returned routes may contain tolls if no reasonable toll-free routes exist, even if `avoidTolls` is `true`. To verify toll assumptions, check [`hasTolls`](route/hastolls.md). The default is `false`.

## See Also

- [origin](directionsrequest/origin.md)
  The starting point for routing directions.
- [destination](directionsrequest/destination.md)
  The end point for routing directions.
- [arrivalDate](directionsrequest/arrivaldate.md)
  The arrival date for the trip.
- [departureDate](directionsrequest/departuredate.md)
  The departure date for the trip.
- [requestsAlternateRoutes](directionsrequest/requestsalternateroutes.md)
  A Boolean value that indicates whether the server returns multiple routes when they’re available.
- [transportType](directionsrequest/transporttype.md)
  The mode of transportation the directions apply to.
- [const TransportType](transporttype.md)
  The modes of transportation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/directionsrequest/avoidtolls)*