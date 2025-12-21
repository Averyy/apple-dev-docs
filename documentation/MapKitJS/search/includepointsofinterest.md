# includePointsOfInterest

**Framework**: MapKit JS  
**Kind**: property

A Boolean value that indicates whether the search results should include points of interest.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
get includePointsOfInterest(): boolean;
set includePointsOfInterest(value: boolean);
```

#### Discussion

If you set this value to `false` and include a [`pointOfInterestFilter`](search/pointofinterestfilter.md), the filter takes precedence and MapKit JS ignores the `false` value. The default value is `true`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/search/includepointsofinterest)*