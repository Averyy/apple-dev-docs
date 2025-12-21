# pointOfInterestFilter

**Framework**: MapKit JS  
**Kind**: property

A filter to use to include or exclude point-of-interest categories.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
get pointOfInterestFilter(): PointOfInterestFilter | null;
set pointOfInterestFilter(value: PointOfInterestFilter | null);
```

#### Discussion

If you provide a [`PointOfInterestFilter`](pointofinterestfilter.md) and set [`includePointsOfInterest`](search/includepointsofinterest.md) to `false`, the filter takes precedence and MapKit JS ignores the Boolean.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/search/pointofinterestfilter)*