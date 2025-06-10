# DirectionsRequest

**Framework**: MapKit JS  
**Kind**: struct

The requested start and end points for a route, as well as the planned mode of transportation.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
dictionary DirectionsRequest {
	string|mapkit.Coordinate|Place origin;
	string|mapkit.Coordinate|Place destination;
	mapkit.Directions.Transport? transportType;
	boolean? requestsAlternateRoutes;
	Date? arrivalDate;
	Date? departureDate;
	boolean? avoidTolls;
};
```

#### Overview

Provide a `DirectionsRequest` object to the [`route`](mapkit.directions/route.md) method to get directions between two points, as shown in the code listing that follows. Direction requests require [`origin`](directionsrequest/origin.md) and [`destination`](directionsrequest/destination.md).

```javascript
const myDirections = new mapkit.Directions();
myDirections.route({ 
  origin: "San Francisco, CA", 
  destination: "Oakland, CA", 
  transportType: mapkit.Directions.Transport.Automobile }, 
  function(error, data) { 
    // Results return asynchronously via this callback function, in `data`
  } 
);
```

## Topics

### Directions request
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
- [mapkit.Directions.Transport](mapkit.directions.transport.md)
  The modes of transportation.

## See Also

- [route](mapkit.directions/route.md)
  Retrieves directions and estimated travel time based on the specified start and end points.
- [DirectionsResponse](directionsresponse.md)
  The directions and estimated travel time that return for a route.
- [Route](route.md)
  Information about a route, including step-by-step instructions, distance, and estimated travel time.
- [RouteStep](routestep.md)
  A single step of the route between the requested start and end points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/directionsrequest)*