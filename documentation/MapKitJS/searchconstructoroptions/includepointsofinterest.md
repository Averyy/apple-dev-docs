# includePointsOfInterest

**Framework**: MapKit JS  
**Kind**: property

A Boolean value that indicates whether the search results should include points of interest.

**Availability**:
- MapKit JS 5.32.2+

## Declaration

```swift
attribute boolean includePointsOfInterest;
```

#### Discussion

If you set this value to `false` and include a [`pointOfInterestFilter`](searchoptions/pointofinterestfilter.md), the filter takes precedence and MapKit JS ignores the `false` value. The default value is `true`.

## See Also

- [pointOfInterestFilter](searchconstructoroptions/pointofinterestfilter.md)
  A filter used to include or exclude point of interest categories.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/searchconstructoroptions/includepointsofinterest)*