# region

**Framework**: MapKit JS  
**Kind**: property

A map region that provides a hint for the geographic area to search.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
attribute mapkit.CoordinateRegion region;
```

#### Discussion

This overrides the [`region`](searchconstructoroptions/region.md) provided to the [`mapkit.Search`](mapkit.search/mapkit.search.md) constructor.

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
- [pointOfInterestFilter](searchoptions/pointofinterestfilter.md)
  A filter for including or excluding point-of-interest categories in search results.
- [regionPriority](searchoptions/regionpriority.md)
  A filter that controls whether results occur outside, or strictly within, the region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/searchoptions/region)*