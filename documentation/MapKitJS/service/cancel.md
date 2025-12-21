# cancel(id)

**Framework**: MapKit JS  
**Kind**: method

Cancels a request using the provided request ID.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
cancel(id: number): boolean;
```

#### Return Value

`true` if the server cancels the pending search request.

#### Discussion

Sometimes you need to cancel a request, either because a person initiates the cancellation or moves on to another activity. Cancel a search request by providing its request ID, which MapKit JS returns from a call to [`search(query, callback, options)`](search/search.md).

## Parameters

- `id`: Pass the integer ID that returns from a call. Passing an invalid ID or the ID of a completed request has no effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/service/cancel)*