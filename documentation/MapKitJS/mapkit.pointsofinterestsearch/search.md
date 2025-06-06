# search

**Framework**: MapKit JS  
**Kind**: method

Fetches points of interest.

**Availability**:
- MapKit JS 5.45+

## Declaration

```swift
number search(
	function|PointsOfInterestSearchDelegate callback,
	optional PointsOfInterestSearchOptions options
);
```

#### Return Value

This method returns a request ID (integer) that you can use with [`cancel`](mapkit.search/cancel.md) to abort a pending request.

#### Discussion

The [`search`](mapkit.pointsofinterestsearch/search.md) method returns a set of points of interest within the region defined and matching the [`mapkit.PointOfInterestFilter`](mapkit.pointofinterestfilter.md).

MapKit JS invokes the `callback` function on failure and success with two arguments, `error` and `data` that represent failure and success information, respectively. You may optionally provide a delegate object instead of a callback. If you call [`cancel`](mapkit.pointsofinterestsearch/cancel.md) before MapKit JS responds, the callback or delegate isn’t called.

## Parameters

- `callback`: A callback function or delegate object with the following parameters:
- `options`: A   object.

## See Also

- [PointsOfInterestSearchDelegate](pointsofinterestsearchdelegate.md)
  An object or callback function that MapKit JS calls when fetching points of interest.
- [PointsOfInterestSearchResponse](pointsofinterestsearchresponse.md)
  The result of a request used to fetch points of interest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.pointsofinterestsearch/search)*