# RouteStep

**Framework**: MapKit JS  
**Kind**: struct

A single step of the route between the requested start and end points.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
dictionary RouteStep {
	mapkit.Coordinate[] path;
	string instructions;
	number distance;
	mapkit.Directions.Transport transportType;
};
```

#### Overview

A [`RouteStep`](routestep.md) encapsulates information for a discrete segment of a route. A [`Route`](route.md) object’s [`steps`](route/steps.md) property is an array of [`RouteStep`](routestep.md) objects. You don’t instantiate [`RouteStep`](routestep.md) objects directly; MapKit JS returns them as part of the [`DirectionsResponse`](directionsresponse.md).

## Topics

### Route step geometry
- [path](routestep/path.md)
  An array of coordinate objects representing the path of the route segment.
### Route step details
- [instructions](routestep/instructions.md)
  The written instructions for following the path that the step represents.
- [distance](routestep/distance.md)
  The step distance, in meters.
- [transportType](routestep/transporttype.md)
  The transport type of the step.
- [mapkit.Directions.Transport](mapkit.directions.transport.md)
  The modes of transportation.

## See Also

- [route](mapkit.directions/route.md)
  Retrieves directions and estimated travel time based on the specified start and end points.
- [DirectionsRequest](directionsrequest.md)
  The requested start and end points for a route, as well as the planned mode of transportation.
- [DirectionsResponse](directionsresponse.md)
  The directions and estimated travel time that return for a route.
- [Route](route.md)
  Information about a route, including step-by-step instructions, distance, and estimated travel time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/routestep)*