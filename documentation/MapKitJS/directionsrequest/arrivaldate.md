# arrivalDate

**Framework**: MapKit JS  
**Kind**: property

The arrival date for the trip.

**Availability**:
- MapKit JS 5.44+

## Declaration

```swift
attribute Date? arrivalDate;
```

## Mentions

- [MapKit JS 5](mapkit-js-5.md)

#### Discussion

Specify either a [`departureDate`](directionsrequest/departuredate.md) or an `arrivalDate`, don’t set both. If you send both values, MapKit JS logs a warning.

## See Also

- [origin](directionsrequest/origin.md)
  The starting point for routing directions.
- [destination](directionsrequest/destination.md)
  The end point for routing directions.
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

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/directionsrequest/arrivaldate)*