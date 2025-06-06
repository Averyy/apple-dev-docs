# searchDidError

**Framework**: MapKit JS  
**Kind**: method

Tells the delegate that the search failed due to an error.

**Availability**:
- MapKit JS 5.45+

## Declaration

```swift
void searchDidError(
	Error error
);
```

#### Discussion

MapKit JS calls this method when the [`search`](mapkit.pointsofinterestsearch/search.md) request fails.

## Parameters

- `error`: The error from a failed fetch for points of interest.

## See Also

- [searchDidComplete](pointsofinterestsearchdelegate/searchdidcomplete.md)
  Tells the delegate that the search completed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/pointsofinterestsearchdelegate/searchdiderror)*