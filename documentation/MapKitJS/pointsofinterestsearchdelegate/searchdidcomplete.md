# searchDidComplete

**Framework**: MapKit JS  
**Kind**: method

Tells the delegate that the search completed.

**Availability**:
- MapKit JS 5.45+

## Declaration

```swift
void searchDidComplete(
	PointsOfInterestSearchResponse data
);
```

#### Discussion

MapKit JS calls this method on successful completion of a [`search`](mapkit.pointsofinterestsearch/search.md) request.

## Parameters

- `data`: The points of interest fetch results.

## See Also

- [searchDidError](pointsofinterestsearchdelegate/searchdiderror.md)
  Tells the delegate that the search failed due to an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/pointsofinterestsearchdelegate/searchdidcomplete)*