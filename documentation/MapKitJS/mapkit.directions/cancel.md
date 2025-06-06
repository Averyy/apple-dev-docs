# cancel

**Framework**: MapKit JS  
**Kind**: method

Cancels a previous request for routes or estimated arrival times.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
boolean cancel(
	number id
);
```

#### Return Value

[`cancel`](mapkit.directions/cancel.md) returns `true` if the server cancels the pending [`route`](mapkit.directions/route.md) or [`eta`](mapkit.directions/eta.md) request. [`cancel`](mapkit.directions/cancel.md) returns `false` if the server can’t cancel the [`route`](mapkit.directions/route.md) or [`eta`](mapkit.directions/eta.md) request.

#### Discussion

Sometimes you need to cancel a request, either because the user initiates the cancellation or moves on to another activity. You can cancel a [`route`](mapkit.directions/route.md) or [`eta`](mapkit.directions/eta.md) request by providing its ID.

## Parameters

- `id`: The ID that returns from a call to   or  . Passing an invalid ID or the ID of a completed request has no effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.directions/cancel)*