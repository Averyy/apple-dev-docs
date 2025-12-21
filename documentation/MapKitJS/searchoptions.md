# SearchOptions

**Framework**: MapKit JS  
**Kind**: struct

An object that contains options to adjust a search.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
interface SearchOptions
```

## Topics

### Search options
- [addressFilter](searchoptions/addressfilter.md)
  An address filter that lists which address components to include or exclude in search results.
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
- [region](searchoptions/region.md)
  A map region that provides a hint for the geographic area to search.
- [regionPriority](searchoptions/regionpriority.md)
  A region priority value that controls whether results occur outside, or strictly within, the region.

## Relationships

### Inherited By
- [SearchAutocompleteOptions](searchautocompleteoptions.md)

## See Also

- [search(query, callback, options)](search/search.md)
  Retrieves the results of a search query.
- [type SearchDelegate](searchdelegate.md)
  An object or callback function the framework calls when performing a search or an autocomplete request.
- [interface SearchResponse](searchresponse.md)
  The result of a search, including the original search query, the bounding region, and a list of places that match the query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/searchoptions)*