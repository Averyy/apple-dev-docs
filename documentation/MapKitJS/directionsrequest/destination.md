# destination

**Framework**: MapKit JS  
**Kind**: property  
**Role**: Interface Property

The end point for routing directions.

**Availability**:
- MapKit JS 5.0+

## Declaration

```
destination: string | CoordinateData | Place;
```

## Discussion

The destination can be a string that’s an address, a coordinate, or a [`Place`](../place.md) object.

## See Also

### Directions request
- [origin](./origin.md)
  The starting point for routing directions.
- [arrivalDate](./arrivaldate.md)
  The arrival date for the trip.
- [departureDate](./departuredate.md)
  The departure date for the trip.
- [requestsAlternateRoutes](./requestsalternateroutes.md)
  A Boolean value that indicates whether the server returns multiple routes when they’re available.
- [transportType](./transporttype.md)
  The mode of transportation the directions apply to.
- [avoidTolls](./avoidtolls.md)
  A Boolean value that prioritizes routes to avoid tolls.
- [signal](./signal.md)
  A signal object allowing you to cancel the request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/directionsrequest/destination)*