# destination

**Framework**: MapKit JS  
**Kind**: property

The end point for routing directions.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
attribute string|mapkit.Coordinate|Place destination;
```

#### Discussion

The destination can be a string that’s an address, a coordinate, or a [`Place`](place.md) object.

## See Also

- [origin](directionsrequest/origin.md)
  The starting point for routing directions.
- [arrivalDate](directionsrequest/arrivaldate.md)
  The arrival date for the trip.
- [departureDate](directionsrequest/departuredate.md)
  The departure date for the trip.
- [requestsAlternateRoutes](directionsrequest/requestsalternateroutes.md)
  A Boolean value that indicates whether the server returns multiple routes when they’re available.
- [transportType](directionsrequest/transporttype.md)
  The mode of transportation the directions apply to.
- [avoidTolls](directionsrequest/avoidtolls.md)
  A Boolean value that prioritizes routes to avoid tolls.
- [mapkit.Directions.Transport](mapkit.directions.transport.md)
  The modes of transportation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/directionsrequest/destination)*