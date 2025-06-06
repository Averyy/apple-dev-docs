# pointOfInterestFilter

**Framework**: MapKit JS  
**Kind**: property

A filter for including or excluding point-of-interest categories in search results.

**Availability**:
- MapKit JS 5.32.2+

## Declaration

```swift
attribute mapkit.PointOfInterestFilter pointOfInterestFilter;
```

#### Discussion

If you provide a [`mapkit.PointOfInterestFilter`](mapkit.pointofinterestfilter.md)  and set [`includePointsOfInterest`](searchconstructoroptions/includepointsofinterest.md) to `false` in the constructor, the filter overrides the Boolean and the search returns points of interest allowed by the filter.

To include or exclude all points of interest use `filterIncludingAllCategories` or `filterExcludingAllCategories`, respectively.

## See Also

- [addressFilter](searchoptions/addressfilter.md)
  An object that filters which address components to include or exclude in search results.
- [coordinate](searchoptions/coordinate.md)
  A map coordinate that provides a hint for the geographic area to search.
- [includeAddresses](searchoptions/includeaddresses.md)
  A Boolean value that indicates whether the search results should include addresses.
- [includePhysicalFeatures](searchoptions/includephysicalfeatures.md)
  A Boolean value that indicates whether the search results include physical features, such as mountain ranges, rivers, and ocean basins.
- [includePointsOfInterest](searchoptions/includepointsofinterest.md)
  A Boolean value that indicates whether the search results should include points of interest.
- [language](searchoptions/language.md)
  A language ID that determines the language for the search result text.
- [limitToCountries](searchoptions/limittocountries.md)
  A string that constrains search results to within the provided countries.
- [region](searchoptions/region.md)
  A map region that provides a hint for the geographic area to search.
- [regionPriority](searchoptions/regionpriority.md)
  A filter that controls whether results occur outside, or strictly within, the region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/searchoptions/pointofinterestfilter)*