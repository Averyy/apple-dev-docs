# DirectionsResponse

**Framework**: MapKit JS  
**Kind**: struct

The directions and estimated travel time that return for a route.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
dictionary DirectionsResponse {
	DirectionsRequest request;
	mapkit.Coordinate?|Place? origin;
	mapkit.Coordinate?|Place? destination;
	Route[] routes;
};
```

## Mentions

- [MapKit JS 5](mapkit-js-5.md)

#### Overview

To get directions, create an instance of [`mapkit.Directions`](mapkit.directions.md) and call the [`route`](mapkit.directions/route.md) method.

When your code calls the [`route`](mapkit.directions/route.md) function, MapKit JS returns a `DirectionsResponse`  asynchronously via a callback function. MapKit JS invokes the callback function with two arguments, `error` and `data` on failure and success. The `data` parameter is a `DirectionsResponse` object,  and the `error` parameter contains an error code and text description of the error.

## Topics

### Directions response
- [request](directionsresponse/request.md)
  The request object associated with the direction’s response.
- [routes](directionsresponse/routes.md)
  An array of route objects.
- [origin](directionsresponse/origin.md)
  An optional starting point for routing directions.
- [destination](directionsresponse/destination.md)
  An optional end point for routing directions.

## See Also

- [route](mapkit.directions/route.md)
  Retrieves directions and estimated travel time based on the specified start and end points.
- [DirectionsRequest](directionsrequest.md)
  The requested start and end points for a route, as well as the planned mode of transportation.
- [Route](route.md)
  Information about a route, including step-by-step instructions, distance, and estimated travel time.
- [RouteStep](routestep.md)
  A single step of the route between the requested start and end points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/directionsresponse)*