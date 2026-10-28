# transportType

**Framework**: MapKit JS  
**Kind**: property  
**Role**: Interface Property

The mode of transportation the directions apply to.

**Availability**:
- MapKit JS 5.0+

## Declaration

```
transportType?: TransportType;
```

## Discussion

You can use this property to specify whether you want directions suited to a particular type of transportation. For example, you can specify if you want walking directions or driving directions.

The default value of this property is [`Automobile`](../transporttype/automobile.md).

## See Also

### Directions request
- [origin](./origin.md)
  The starting point for routing directions.
- [destination](./destination.md)
  The end point for routing directions.
- [arrivalDate](./arrivaldate.md)
  The arrival date for the trip.
- [departureDate](./departuredate.md)
  The departure date for the trip.
- [requestsAlternateRoutes](./requestsalternateroutes.md)
  A Boolean value that indicates whether the server returns multiple routes when they’re available.
- [avoidTolls](./avoidtolls.md)
  A Boolean value that prioritizes routes to avoid tolls.
- [signal](./signal.md)
  A signal object allowing you to cancel the request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/directionsrequest/transporttype)*