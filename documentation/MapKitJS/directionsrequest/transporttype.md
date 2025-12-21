# transportType

**Framework**: MapKit JS  
**Kind**: property

The mode of transportation the directions apply to.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
transportType?: TransportType;
```

#### Discussion

You can use this property to specify whether you want directions suited to a particular type of transportation. For example, you can specify if you want walking directions or driving directions.

The default value of this property is [`Automobile`](transporttype/automobile.md).

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
- [avoidTolls](directionsrequest/avoidtolls.md)
  A Boolean value that prioritizes routes to avoid tolls.
- [const TransportType](transporttype.md)
  The modes of transportation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/directionsrequest/transporttype)*