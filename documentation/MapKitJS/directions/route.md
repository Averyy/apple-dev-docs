# route(request)

**Framework**: MapKit JS  
**Kind**: method

Retrieves directions and estimated travel time based on the specified start and end points.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
route(request: DirectionsRequest): Promise<DirectionsResponse>;
```

#### Return Value

A promise that resolves with a [`DirectionsResponse`](directionsresponse.md) on success, or rejects with an `Error` on failure.

#### Discussion

Call the [`route(request)`](directions/route.md) method to get directions.

The resolved [`DirectionsResponse`](directionsresponse.md) object has the following properties:

- [`request`](directionsresponse/request.md) is the request object associated with this response.
- [`routes`](directionsresponse/routes.md) contains an array of up to three [`Route`](route.md) objects returned by the server.

Pass an `AbortSignal` from an `AbortController` to the [`signal`](directionsrequest/signal.md) option to allow the controller to cancel a pending request. When the controller aborts, the promise it returns rejects with a `DOMException` whose `name` is `"AbortError"`.

## Parameters

- `request`: A [`DirectionsRequest`](directionsrequest.md) object that specifies details for the directions you want to retrieve.

## See Also

- [interface DirectionsRequest](directionsrequest.md)
  The requested start and end points for a route, as well as the planned mode of transportation.
- [interface DirectionsResponse](directionsresponse.md)
  The directions and estimated travel time for a route.
- [class Route](route.md)
  Information about a route, including step-by-step instructions, distance, and estimated travel time.
- [class RouteStep](routestep.md)
  A single step of the route between the requested start and end points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/directions/route)*