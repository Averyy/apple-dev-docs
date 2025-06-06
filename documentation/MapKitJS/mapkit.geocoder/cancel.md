# cancel

**Framework**: MapKit JS  
**Kind**: method

Cancels the pending lookup or reverse lookup using its request ID.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
boolean cancel(
	number id
);
```

#### Return Value

Returns `true` if the system cancels a pending request.

#### Discussion

Returns `false` if the request is already complete or if the request ID is invalid.

#### Discussion

Sometimes you need to cancel a request, either because the user initiates the cancellation or moves on to another activity.

Cancel a geocoding [`lookup`](mapkit.geocoder/lookup.md) or [`reverseLookup`](mapkit.geocoder/reverselookup.md) by specifying its request ID, which MapKit JS returns when making the initial request.

## Parameters

- `id`: The request ID of the   or   to cancel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.geocoder/cancel)*