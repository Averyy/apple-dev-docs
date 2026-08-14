# search(options)

**Framework**: MapKit JS  
**Kind**: method

Fetches points of interest.

**Availability**:
- MapKit JS 5.45+

## Declaration

```swift
search(
    options?: PointsOfInterestSearchOptions,
): Promise<PointsOfInterestSearchResponse>;
```

#### Return Value

A promise that resolves with a [`PointsOfInterestSearchResponse`](pointsofinterestsearchresponse.md) on success, or rejects with an `Error` on failure.

#### Discussion

The [`search()`](pointsofinterestsearch/search.md) method returns a set of points of interest within the region defined and matching the [`PointOfInterestFilter`](pointofinterestfilter.md).

Pass an `AbortSignal` from an `AbortController` to the [`signal`](pointsofinterestsearchoptions/signal.md) option to allow the controller to cancel a pending request. When the controller aborts, the promise it returns rejects with a `DOMException` whose `name` is `"AbortError"`.

## Parameters

- `options`: A [`PointsOfInterestSearchOptions`](pointsofinterestsearchoptions.md) object that can overwrite the same options set on the property or that you supplied to the [`PointsOfInterestSearch`](pointsofinterestsearch.md) constructor.

## See Also

- [type PointsOfInterestSearchDelegate](pointsofinterestsearchdelegate.md)
  An object or callback function that MapKit JS calls when fetching points of interest.
- [interface PointsOfInterestSearchResponse](pointsofinterestsearchresponse.md)
  The result of a request used to fetch points of interest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/pointsofinterestsearch/search)*