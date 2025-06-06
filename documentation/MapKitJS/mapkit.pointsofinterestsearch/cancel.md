# cancel

**Framework**: MapKit JS  
**Kind**: method

Cancels a search request using its request ID.

**Availability**:
- MapKit JS 5.45+

## Declaration

```swift
boolean cancel(
	number id
);
```

#### Return Value

`true` if the server canceled the pending search request.

#### Discussion

Cancel an uncompleted search request by providing its request ID, the value returned from a call to [`search`](mapkit.pointsofinterestsearch/search.md), to this method.

## Parameters

- `id`: Pass the integer ID returned by a call to  . The system ignores an invalid ID or the ID of a request that has completed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.pointsofinterestsearch/cancel)*