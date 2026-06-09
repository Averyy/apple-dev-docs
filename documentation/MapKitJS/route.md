# Route

**Framework**: MapKit JS  
**Kind**: class

Information about a route, including step-by-step instructions, distance, and estimated travel time.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
class Route
```

#### Overview

A [`Route`](route.md) object encapsulates the information for a route that the server returns, including geometry that you can use to draw a path and step-by-step text instructions. You don’t instantiate [`Route`](route.md) objects directly; MapKit JS returns them as part of the [`DirectionsResponse`](directionsresponse.md).

## Topics

### Route geometry
- [polyline](route/polyline.md)
  An instance of a polyline overlay that represents the path of a route.
### Deprecated
- [path](route/path.md)
  An array of coordinate objects representing the path of the route.
### Route details
- [steps](route/steps.md)
  An array of steps that compose the overall route.
- [name](route/name.md)
  The name assigned to the route.
- [distance](route/distance.md)
  The route distance, in meters.
- [expectedTravelTime](route/expectedtraveltime.md)
  The expected travel time, in seconds.
- [transportType](route/transporttype.md)
  The overall route transport type.
- [hasTolls](route/hastolls.md)
  A Boolean value that indicates whether a route has tolls.

## See Also

- [route(request)](directions/route.md)
  Retrieves directions and estimated travel time based on the specified start and end points.
- [interface DirectionsRequest](directionsrequest.md)
  The requested start and end points for a route, as well as the planned mode of transportation.
- [interface DirectionsResponse](directionsresponse.md)
  The directions and estimated travel time for a route.
- [class RouteStep](routestep.md)
  A single step of the route between the requested start and end points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/route)*