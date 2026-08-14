# search(callback, options)

**Framework**: MapKit JS  
**Kind**: method

Fetches points of interest.

**Availability**:
- MapKit JS 5.45+

## Declaration

```swift
search(
    callback: PointsOfInterestSearchDelegate,
    options?: PointsOfInterestSearchOptions,
): Promise<PointsOfInterestSearchResponse>;
```

#### Return Value

A promise that resolves with a [`PointsOfInterestSearchResponse`](pointsofinterestsearchresponse.md) on success.

#### Discussion

The [`search()`](pointsofinterestsearch/search1.md) method returns a set of points of interest within the region defined and matching the [`PointOfInterestFilter`](pointofinterestfilter.md).

MapKit JS invokes the `callback` function on failure and success with two arguments, `error` and `data` that represent failure and success information, respectively. You may optionally provide a delegate object instead of a callback. If you call [`cancel()`](service/cancel.md) before MapKit JS responds, the system doesn’t call the callback or delegate.

## Parameters

- `callback`: A callback function or delegate object with the following parameters: - **`error` (`Error`)**: An error code and descriptive message.
- **`data` ([`PointsOfInterestSearchResponse`](pointsofinterestsearchresponse.md))**: The search response object.
- `options`: A [`PointsOfInterestSearchOptions`](pointsofinterestsearchoptions.md) object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/pointsofinterestsearch/search1)*