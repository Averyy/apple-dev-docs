# pointOfInterestFilter

**Framework**: MapKit JS  
**Kind**: property

A filter for including or excluding point-of-interest categories in search results.

**Availability**:
- MapKit JS 5.32.2+

## Declaration

```swift
pointOfInterestFilter?: PointOfInterestFilter;
```

#### Discussion

If you provide a [`PointOfInterestFilter`](pointofinterestfilter.md) and set [`includePointsOfInterest`](searchconstructoroptions/includepointsofinterest.md) to `false` in the constructor, the filter overrides the Boolean and the search returns points of interest allowed by the filter.

To include or exclude all points of interest use [`filterIncludingAllCategories`](mapkit/filterincludingallcategories.md) or [`filterExcludingAllCategories`](mapkit/filterexcludingallcategories.md), respectively.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/searchoptions/pointofinterestfilter)*