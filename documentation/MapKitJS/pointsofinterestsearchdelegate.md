# PointsOfInterestSearchDelegate

**Framework**: MapKit JS  
**Kind**: class

An object or callback function that MapKit JS calls when fetching points of interest.

**Availability**:
- MapKit JS 5.45+

## Declaration

```swift
interface PointsOfInterestSearchDelegate
```

#### Overview

You may pass an object to the search method instead of using of a search delegate callback function. MapKit JS calls the following methods on the delegate object when they exist:

- [`searchDidComplete`](pointsofinterestsearchdelegate/searchdidcomplete.md) – Upon successful completion of a search request, this method returns a data object that is the same as the one passed to the search callback function.
- [`searchDidError`](pointsofinterestsearchdelegate/searchdiderror.md) – Called when the search request fails.

## Topics

### Responding to state changes and errors
- [searchDidComplete](pointsofinterestsearchdelegate/searchdidcomplete.md)
  Tells the delegate that the search completed.
- [searchDidError](pointsofinterestsearchdelegate/searchdiderror.md)
  Tells the delegate that the search failed due to an error.

## See Also

- [search](mapkit.pointsofinterestsearch/search.md)
  Fetches points of interest.
- [PointsOfInterestSearchResponse](pointsofinterestsearchresponse.md)
  The result of a request used to fetch points of interest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/pointsofinterestsearchdelegate)*