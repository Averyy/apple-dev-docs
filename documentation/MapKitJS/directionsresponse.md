# DirectionsResponse

**Framework**: MapKit JS  
**Kind**: struct

The directions and estimated travel time that return for a route.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
interface DirectionsResponse
```

## Mentions

- [MapKit JS 5](mapkit-js-5.md)

#### Overview

To get directions, create an instance of [`Directions`](directions.md) and call the [`route(request, callback)`](directions/route.md) method.

When your code calls the [`route(request, callback)`](directions/route.md) function, MapKit JS returns a `DirectionsResponse` asynchronously via a callback function. MapKit JS invokes the callback function with two arguments, `error` and `data` on failure and success. The `data` parameter is a `DirectionsResponse` object,  and the `error` parameter contains an error code and text description of the error.

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

- [route(request, callback)](directions/route.md)
  Retrieves directions and estimated travel time based on the specified start and end points.
- [interface DirectionsRequest](directionsrequest.md)
  The requested start and end points for a route, as well as the planned mode of transportation.
- [class Route](route.md)
  Information about a route, including step-by-step instructions, distance, and estimated travel time.
- [class RouteStep](routestep.md)
  A single step of the route between the requested start and end points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/directionsresponse)*