# route

**Framework**: MapKit JS  
**Kind**: method

Retrieves directions and estimated travel time based on the specified start and end points.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
number route(
	DirectionsRequest request,
	function callback
);
```

#### Return Value

A request ID, which you can pass to [`cancel`](mapkit.directions/cancel.md) to abort a pending request.

#### Discussion

Call the [`route`](mapkit.directions/route.md) method to get directions.

MapKit JS returns directions asynchronously via a callback function. This callback function is invoked with two arguments, `error` on failure and `data` on success.

`error` contains an error code and a text description of the error. `data` is a [`DirectionsResponse`](directionsresponse.md) object with the following two properties:

- `request` is the request object associated with this response.
- `routes` contains an array of up to three [`Route`](route.md) objects returned by the server.

## Parameters

- `request`: A   object that specifies details for the directions you want to retrieve.
- `callback`: A callback function that receives the directions, returned asynchronously.

## See Also

- [DirectionsRequest](directionsrequest.md)
  The requested start and end points for a route, as well as the planned mode of transportation.
- [DirectionsResponse](directionsresponse.md)
  The directions and estimated travel time that return for a route.
- [Route](route.md)
  Information about a route, including step-by-step instructions, distance, and estimated travel time.
- [RouteStep](routestep.md)
  A single step of the route between the requested start and end points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.directions/route)*