# departureDate

**Framework**: MapKit JS  
**Kind**: property  
**Role**: Interface Property

The departure date for the trip.

**Availability**:
- MapKit JS 5.44+

## Declaration

```
departureDate?: Date;
```

## Mentions

- [MapKit JS 5](../mapkit-js-5.md)

## Discussion

Specify either a `departureDate` or an [`arrivalDate`](./arrivaldate.md), don’t set both. If you send both values, MapKit JS logs a warning.

## See Also

### Directions request
- [origin](./origin.md)
  The starting point for routing directions.
- [destination](./destination.md)
  The end point for routing directions.
- [arrivalDate](./arrivaldate.md)
  The arrival date for the trip.
- [requestsAlternateRoutes](./requestsalternateroutes.md)
  A Boolean value that indicates whether the server returns multiple routes when they’re available.
- [transportType](./transporttype.md)
  The mode of transportation the directions apply to.
- [avoidTolls](./avoidtolls.md)
  A Boolean value that prioritizes routes to avoid tolls.
- [signal](./signal.md)
  A signal object allowing you to cancel the request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/directionsrequest/departuredate)*