# eta(request)

**Framework**: MapKit JS  
**Kind**: method

Retrieves estimated arrival times to up to 10 destinations from a single starting point.

**Availability**:
- MapKit JS 5.46+

## Declaration

```swift
eta(request: EtaRequestOptions): Promise<EtaResponse>;
```

#### Return Value

A promise that resolves with an [`EtaResponse`](etaresponse.md) on success, or rejects with an `Error` on failure.

#### Discussion

To get a set of estimated arrival times, provide an [`EtaRequestOptions`](etarequestoptions.md) object when you call the [`eta(request)`](directions/eta.md) method. You can provide up to 10 destinations. The server returns an error if you request more than 10 destinations in a single request.

Pass an `AbortSignal` from an `AbortController` to the [`signal`](etarequestoptions/signal.md) option to allow the controller to cancel a pending request. When the controller aborts, the promise it returns rejects with a `DOMException` whose `name` is `"AbortError"`.

## Parameters

- `request`: An [`EtaRequestOptions`](etarequestoptions.md) object that specifies details for the server to provide estimated arrival times at one or more destinations.

## See Also

- [interface EtaRequestOptions](etarequestoptions.md)
  The options you may provide for requesting estimated arrival times.
- [interface EtaResponse](etaresponse.md)
  The estimated arrival times for a set of destinations.
- [interface EtaResult](etaresult.md)
  The mode of transportation, distance, and travel time estimates for a single destination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/directions/eta)*