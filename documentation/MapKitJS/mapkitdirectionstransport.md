# mapkit.Directions.Transport

**Framework**: MapKit JS  
**Kind**: enum

The modes of transportation.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
interface mapkit.Directions.Transport {
	const string Automobile;
	const string Walking;
	const string Cycling;
};
```

## Mentions

- [MapKit JS 5](mapkit-js-5.md)

#### Overview

Constants that describe the mode of transportation in [`DirectionsRequest`](directionsrequest.md) and [`DirectionsResponse`](directionsresponse.md).

## Topics

### Transport types
- [Walking](mapkit.directions.transport/walking.md)
  A constant identifying the mode of transportation as walking.
- [Automobile](mapkit.directions.transport/automobile.md)
  A constant identifying the mode of transportation as driving.
- [Cycling](mapkit.directions.transport/cycling.md)
  A constant identifying the mode of transportation as cycling.

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
- [avoidTolls](directionsrequest/avoidtolls.md)
  A Boolean value that prioritizes routes to avoid tolls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.directions.transport)*