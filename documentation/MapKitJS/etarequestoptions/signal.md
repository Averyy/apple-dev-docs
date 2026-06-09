# signal

**Framework**: MapKit JS  
**Kind**: property

A signal object allowing you to cancel the request.

**Availability**:
- MapKit JS 6.0+

## Declaration

```swift
signal?: AbortSignal;
```

#### Discussion

Pass an `AbortSignal` from an `AbortController` to allow the controller to cancel a pending ETA request. When the controller aborts, the promise it returns rejects with a `DOMException` whose `name` is `"AbortError"`.

## See Also

- [origin](etarequestoptions/origin.md)
  The starting point for estimated arrival time requests.
- [departureDate](etarequestoptions/departuredate.md)
  The time of departure used in an estimated arrival time request.
- [destinations](etarequestoptions/destinations.md)
  An array of coordinates that represent end points for estimated arrival time requests.
- [transportType](etarequestoptions/transporttype.md)
  The mode of transportation the server uses when estimating arrival times.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/etarequestoptions/signal)*