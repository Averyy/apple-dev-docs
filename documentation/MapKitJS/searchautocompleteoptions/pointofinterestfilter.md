# pointOfInterestFilter

**Framework**: MapKit JS  
**Kind**: property

A filter used to include or exclude point of interest categories in search results.

**Availability**:
- MapKit JS 5.32.2+

## Declaration

```swift
attribute mapkit.PointOfInterestFilter pointOfInterestFilter;
```

#### Discussion

If you provide a [`mapkit.PointOfInterestFilter`](mapkit.pointofinterestfilter.md) and set [`includePointsOfInterest`](searchconstructoroptions/includepointsofinterest.md) to `false` in the constructor, the filter overrides the Boolean value, and the search returns points of interest allowed by the filter.

To include or exclude all points of interest use `filterIncludingAllCategories` or `filterExcludingAllCategories`, respectively.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/searchautocompleteoptions/pointofinterestfilter)*