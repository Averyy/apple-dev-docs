# limitToCountries

**Framework**: MapKit JS  
**Kind**: property

A string that constrains search results to within the provided countries.

**Availability**:
- MapKit JS 5.49+

## Declaration

```swift
limitToCountries?: string;
```

#### Discussion

The string is a comma-separated list of two-digit ISO 3166-2 country and region codes. For example, to limit search results to Germany, Belgium, and France specify `de,be,fr`.

## See Also

- [includePhysicalFeatures](searchconstructoroptions/includephysicalfeatures.md)
  A Boolean value that indicates whether the search results include physical features, such as mountain ranges, rivers, and ocean basins.
- [includeQueries](searchconstructoroptions/includequeries.md)
  A Boolean value that indicates whether the search results include queries.
- [regionPriority](searchconstructoroptions/regionpriority.md)
  A region priority value that controls whether results occur outside, or strictly within, the region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/searchconstructoroptions/limittocountries)*