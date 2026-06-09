# DirectionsResponse

**Framework**: MapKit JS  
**Kind**: struct

The directions and estimated travel time for a route.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
interface DirectionsResponse
```

## Mentions

- [MapKit JS 5](mapkit-js-5.md)

#### Overview

To get directions, create an instance of [`Directions`](directions.md) and call the [`route(request)`](directions/route.md) method.

The [`route(request)`](directions/route.md) method returns a promise that resolves with a `DirectionsResponse` on success.

## Topics

### Directions response
- [routes](directionsresponse/routes.md)
  An array of route objects.
- [origin](directionsresponse/origin.md)
  An optional starting point for routing directions.
- [destination](directionsresponse/destination.md)
  An optional end point for routing directions.
### Deprecated
- [request](directionsresponse/request.md)
  The request object associated with the direction’s response.

## See Also

- [route(request)](directions/route.md)
  Retrieves directions and estimated travel time based on the specified start and end points.
- [interface DirectionsRequest](directionsrequest.md)
  The requested start and end points for a route, as well as the planned mode of transportation.
- [class Route](route.md)
  Information about a route, including step-by-step instructions, distance, and estimated travel time.
- [class RouteStep](routestep.md)
  A single step of the route between the requested start and end points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/directionsresponse)*