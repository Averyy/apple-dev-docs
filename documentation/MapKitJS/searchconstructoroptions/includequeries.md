# includeQueries

**Framework**: MapKit JS  
**Kind**: property

A Boolean value that indicates whether the search results include queries.

**Availability**:
- MapKit JS 5.32.2+

## Declaration

```swift
includeQueries?: boolean;
```

#### Discussion

This option only applies to search autocomplete. For example, if you send  to [`autocomplete(query, callback, options)`](search/autocomplete.md), the search returns only . If you send  to [`autocomplete(query, callback, options)`](search/autocomplete.md) while `includeQueries` is `false`, the search returns only addresses and points of interest (given that the setting for those options is `true`) related to  and not necessarily related to .

The default value is `true`.

## See Also

- [includePhysicalFeatures](searchconstructoroptions/includephysicalfeatures.md)
  A Boolean value that indicates whether the search results include physical features, such as mountain ranges, rivers, and ocean basins.
- [limitToCountries](searchconstructoroptions/limittocountries.md)
  A string that constrains search results to within the provided countries.
- [regionPriority](searchconstructoroptions/regionpriority.md)
  A region priority value that controls whether results occur outside, or strictly within, the region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/searchconstructoroptions/includequeries)*