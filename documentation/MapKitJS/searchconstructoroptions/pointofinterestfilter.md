# pointOfInterestFilter

**Framework**: MapKit JS  
**Kind**: property  
**Role**: Interface Property

A filter used to include or exclude point-of-interest categories.

**Availability**:
- MapKit JS 5.32.2+

## Declaration

```
pointOfInterestFilter?: PointOfInterestFilter;
```

## Discussion

If you provide a [`PointOfInterestFilter`](../pointofinterestfilter.md) and set [`includePointsOfInterest`](./includepointsofinterest.md) to `false`, the filter takes precedence and MapKit JS ignores the Boolean.

## See Also

### Points of Interest
- [includePointsOfInterest](./includepointsofinterest.md)
  A Boolean value that indicates whether the search results should include points of interest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/searchconstructoroptions/pointofinterestfilter)*