# eta(request, callback)

**Framework**: MapKit JS  
**Kind**: method

Retrieves estimated arrival times to up to 10 destinations from a single starting point.

**Availability**:
- MapKit JS 5.46+

## Declaration

```swift
eta(
    request: EtaRequestOptions,
    callback: (error: Error | null, result: EtaResponse | null) => void,
): Promise<EtaResponse>;
```

#### Return Value

A promise that resolves with an [`EtaResponse`](etaresponse.md) on success.

#### Discussion

To get a set of estimated arrival times, provide an [`EtaRequestOptions`](etarequestoptions.md) object when you call the [`eta()`](directions/eta1.md) method. You can provide up to 10 destinations. The server returns an error if you request more than 10 destinations in a single request.

Estimated times are returned asynchronously via a callback function. MapKit JS invokes the callback function with two arguments, `error` on failure and `data` on success.

`error` contains an error code and a text description of the error. `data` is an [`EtaResponse`](etaresponse.md) object.

## Parameters

- `request`: An [`EtaRequestOptions`](etarequestoptions.md) object that specifies details for the server to provide estimated arrival times at one or more destinations.
- `callback`: A callback function that receives the estimated time response object, returned asynchronously.

## See Also

- [route(request, callback)](directions/route1.md)
  Retrieves directions and estimated travel time based on the specified start and end points.
- [Transport](directions/transport.md)
  A static property that refers to an object that describes the available transport type values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/directions/eta1)*