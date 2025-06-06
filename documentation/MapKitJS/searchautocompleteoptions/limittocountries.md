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

The string is a comma-separated list of two-letter, ISO 3166-1 country and region codes. For example, to limit search results to Germany, Belgium, and France specify `de,be,fr`.

## See Also

- [includePhysicalFeatures](searchautocompleteoptions/includephysicalfeatures.md)
  A Boolean value that indicates whether the autocomplete search results include physical features, such as mountain ranges, rivers, and ocean basins.
- [includePointsOfInterest](searchautocompleteoptions/includepointsofinterest.md)
  A Boolean value that indicates whether the search results include points of interest.
- [includeQueries](searchautocompleteoptions/includequeries.md)
  A Boolean value that indicates whether the search results include queries.
- [regionPriority](searchautocompleteoptions/regionpriority.md)
  A filter that controls whether results occur outside, or strictly within, the region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/searchautocompleteoptions/limittocountries)*