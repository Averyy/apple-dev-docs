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

#### Discussion

Pass an `AbortSignal` from an `AbortController` to allow the controller to cancel a pending directions request. When the controller aborts, the promise it returns rejects with a `DOMException` whose `name` is `"AbortError"`.

```javascript
const controller = new AbortController();
const directions = new mapkit.Directions();

try {
    const response = await directions.route({
        origin: "San Francisco",
        destination: "Los Angeles",
        signal: controller.signal,
    });
} catch (error) {
    if (error.name === "AbortError") {
        // The request was canceled.
    }
}

// Cancel the request at any time:
controller.abort();
```

## See Also

### Directions request
- [origin](./origin.md)
  The starting point for routing directions.
- [destination](./destination.md)
  The end point for routing directions.
- [arrivalDate](./arrivaldate.md)
  The arrival date for the trip.
- [departureDate](./departuredate.md)
  The departure date for the trip.
- [requestsAlternateRoutes](./requestsalternateroutes.md)
  A Boolean value that indicates whether the server returns multiple routes when they’re available.
- [transportType](./transporttype.md)
  The mode of transportation the directions apply to.
- [avoidTolls](./avoidtolls.md)
  A Boolean value that prioritizes routes to avoid tolls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/directionsrequest/signal)*