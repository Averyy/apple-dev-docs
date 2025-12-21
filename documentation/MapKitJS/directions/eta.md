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
        callback: (error: Error | null, result?: EtaResponse) => void,
    ): number | undefined;
```

#### Return Value

A request ID, which you can pass to [`cancel(id)`](service/cancel.md) to cancel a pending request.

#### Discussion

To get a set of estimated arrival times, provide an [`EtaRequestOptions`](etarequestoptions.md) object when you call the [`eta(request, callback)`](directions/eta.md) method. You may provide up to 10 destinations. The server returns an error if you request more than 10 destinations in a single request.

Estimated times are returned asynchronously via a callback function. MapKit JS invokes the callback function with two arguments, `error` on failure and `data` on success.

`error` contains an error code and a text description of the error. `data` is an [`EtaResponse`](etaresponse.md) object.

## Parameters

- `request`: An   object that specifies details for the server to provide estimated arrival times at one or more destinations.
- `callback`: A callback function that receives the estimated time response object, returned asynchronously.

## See Also

- [interface EtaRequestOptions](etarequestoptions.md)
  The options you may provide for requesting estimated arrival times.
- [interface EtaResponse](etaresponse.md)
  The estimated arrival times for a set of destinations.
- [interface EtaResult](etaresult.md)
  The mode of transportation, distance, and travel time estimates for a single destination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/directions/eta)*