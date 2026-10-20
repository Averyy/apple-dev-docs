# avoidTolls

**Framework**: MapKit JS  
**Kind**: property  
**Role**: Interface Property

A Boolean value that prioritizes routes to avoid tolls.

**Availability**:
- MapKit JS 5.72+

## Declaration

```
avoidTolls?: boolean;
```

#### Discussion

Set this value to `true` to prioritize routes that don’t have any tolls. The returned routes may contain tolls if no reasonable toll-free routes exist, even if `avoidTolls` is `true`. To verify toll assumptions, check [`hasTolls`](../route/hastolls.md). The default is `false`.

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
- [transportType](./transporttype.md)
  The mode of transportation the directions apply to.
- [signal](./signal.md)
  A signal object allowing you to cancel the request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/directionsrequest/avoidtolls)*