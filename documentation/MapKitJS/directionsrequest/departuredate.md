# departureDate

**Framework**: MapKit JS  
**Kind**: property

The departure date for the trip.

**Availability**:
- MapKit JS 5.44+

## Declaration

```swift
departureDate?: Date;
```

## Mentions

- [MapKit JS 5](mapkit-js-5.md)

#### Discussion

Specify either a `departureDate` or an [`arrivalDate`](directionsrequest/arrivaldate.md), don’t set both. If you send both values, MapKit JS logs a warning.

## See Also

- [origin](directionsrequest/origin.md)
  The starting point for routing directions.
- [destination](directionsrequest/destination.md)
  The end point for routing directions.
- [arrivalDate](directionsrequest/arrivaldate.md)
  The arrival date for the trip.
- [requestsAlternateRoutes](directionsrequest/requestsalternateroutes.md)
  A Boolean value that indicates whether the server returns multiple routes when they’re available.
- [transportType](directionsrequest/transporttype.md)
  The mode of transportation the directions apply to.
- [avoidTolls](directionsrequest/avoidtolls.md)
  A Boolean value that prioritizes routes to avoid tolls.
- [const TransportType](transporttype.md)
  The modes of transportation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/directionsrequest/departuredate)*