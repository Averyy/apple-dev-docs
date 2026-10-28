# signal

**Framework**: MapKit JS  
**Kind**: property  
**Role**: Interface Property

A signal object allowing you to cancel the request.

**Availability**:
- MapKit JS 6.0+

## Declaration

```
signal?: AbortSignal;
```

## Discussion

Pass an `AbortSignal` from an `AbortController` to allow the controller to cancel a pending ETA request. When the controller aborts, the promise it returns rejects with a `DOMException` whose `name` is `"AbortError"`.

## See Also

### ETA Request
- [origin](./origin.md)
  The starting point for estimated arrival time requests.
- [departureDate](./departuredate.md)
  The time of departure used in an estimated arrival time request.
- [destinations](./destinations.md)
  An array of coordinates that represent end points for estimated arrival time requests.
- [transportType](./transporttype.md)
  The mode of transportation the server uses when estimating arrival times.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/etarequestoptions/signal)*