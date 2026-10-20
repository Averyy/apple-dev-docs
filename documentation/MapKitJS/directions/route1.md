# route(request, callback)

**Framework**: MapKit JS  
**Kind**: method  
**Role**: Instance Method

Retrieves directions and estimated travel time based on the specified start and end points.

**Availability**:
- MapKit JS 5.0+ - Deprecated in 6.0

> **Deprecated**: Instead of passing in a callback, handle the returned promise instead. See [`route()`](./route.md).

## Declaration

```
route(
    request: DirectionsRequest,
    callback: (
        error: Error | null,
        result: DirectionsResponse | null,
    ) => void,
): Promise<DirectionsResponse>;
```

#### Return Value

A promise that resolves with a [`DirectionsResponse`](../directionsresponse.md) on success.

#### Discussion

Call the [`route()`](./route1.md) method to get directions.

MapKit JS returns directions asynchronously via a callback function. This callback function is invoked with two arguments, `error` on failure and `data` on success.

`error` contains an error code and a text description of the error. `data` is a [`DirectionsResponse`](../directionsresponse.md) object with the following two properties:

- [`request`](../directionsresponse/request.md) is the request object associated with this response.
- [`routes`](../directionsresponse/routes.md) contains an array of up to three [`Route`](../route.md) objects returned by the server.

## Parameters

- `request`: A [`DirectionsRequest`](../directionsrequest.md) object that specifies details for the directions you want to retrieve.
- `callback`: A callback function that receives the directions, returned asynchronously.

## See Also

### Deprecated
- [eta(request, callback)](./eta1.md)
  Retrieves estimated arrival times to up to 10 destinations from a single starting point.
- [Transport](./transport.md)
  A static property that refers to an object that describes the available transport type values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/directions/route1)*