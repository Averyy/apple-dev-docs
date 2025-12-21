# PointsOfInterestSearchDelegate

**Framework**: MapKit JS  
**Kind**: typealias

An object or callback function that MapKit JS calls when fetching points of interest.

**Availability**:
- MapKit JS 5.45+

## Declaration

```swift
type PointsOfInterestSearchDelegate =
    | {
          searchDidError: (error: Error) => void;
          searchDidComplete: (result: PointsOfInterestSearchResponse) => void;
      }
    | ((error: Error | null, result?: PointsOfInterestSearchResponse) => void);
```

#### Discussion

You may pass an object to the search method instead of using of a search delegate callback function. MapKit JS calls the following methods on the delegate object when they exist:

- `searchDidComplete` – Upon successful completion of a search request, this method returns a data object that is the same as the one passed to the search callback function.
- `searchDidError` – Called when the search request fails.

## See Also

- [search(callback, options)](pointsofinterestsearch/search.md)
  Fetches points of interest.
- [interface PointsOfInterestSearchResponse](pointsofinterestsearchresponse.md)
  The result of a request used to fetch points of interest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/pointsofinterestsearchdelegate)*