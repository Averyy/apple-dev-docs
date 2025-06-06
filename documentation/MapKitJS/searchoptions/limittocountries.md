# limitToCountries

**Framework**: MapKit JS  
**Kind**: property

A string that constrains search results to within the provided countries.

**Availability**:
- MapKit JS 5.49+

## Declaration

```swift
attribute string limitToCountries;
```

#### Discussion

The string is a comma-separated list of two-digit ISO 3166-2 country and region codes. For example, to limit search results to Germany, Belgium,  and France specify `de,be,fr`.

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
- [pointOfInterestFilter](searchoptions/pointofinterestfilter.md)
  A filter for including or excluding point-of-interest categories in search results.
- [region](searchoptions/region.md)
  A map region that provides a hint for the geographic area to search.
- [regionPriority](searchoptions/regionpriority.md)
  A filter that controls whether results occur outside, or strictly within, the region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/searchoptions/limittocountries)*