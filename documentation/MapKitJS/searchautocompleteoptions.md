# SearchAutocompleteOptions

**Framework**: MapKit JS  
**Kind**: struct

Options you provide to constrain an autocomplete request.

**Availability**:
- MapKit JS 5.32.2+

## Declaration

```swift
interface SearchAutocompleteOptions extends SearchOptions
```

## Topics

### Autocomplete search initialization
- [coordinate](searchoptions/coordinate.md)
  A map coordinate that provides a hint for the geographic area to search.
- [language](searchoptions/language.md)
  A language ID that determines the language for the search result text.
- [region](searchoptions/region.md)
  A map region that provides a hint for the geographic area to search.
### Autocomplete search filtering
- [includePhysicalFeatures](searchoptions/includephysicalfeatures.md)
  A Boolean value that indicates whether the search results include physical features, such as mountain ranges, rivers, and ocean basins.
- [includePointsOfInterest](searchoptions/includepointsofinterest.md)
  A Boolean value that indicates whether the search results should include points of interest.
- [includeQueries](searchautocompleteoptions/includequeries.md)
  A Boolean value that indicates whether the search results include queries.
- [limitToCountries](searchoptions/limittocountries.md)
  A string that constrains search results to within the provided countries.
- [regionPriority](searchoptions/regionpriority.md)
  A region priority value that controls whether results occur outside, or strictly within, the region.
### Address filtering
- [addressFilter](searchoptions/addressfilter.md)
  An address filter that lists which address components to include or exclude in search results.
- [includeAddresses](searchoptions/includeaddresses.md)
  A Boolean value that indicates whether the search results should include addresses.
### Points of interest
- [pointOfInterestFilter](searchoptions/pointofinterestfilter.md)
  A filter for including or excluding point-of-interest categories in search results.

## Relationships

### Inherits From
- [SearchOptions](searchoptions.md)

## See Also

- [autocomplete(query, callback, options)](search/autocomplete.md)
  Retrieves a list of autocomplete results for the specified search query.
- [interface SearchAutocompleteResponse](searchautocompleteresponse.md)
  An object containing the response from an autocomplete request.
- [class SearchAutocompleteResult](searchautocompleteresult.md)
  The result of an autocomplete query, including display lines and a coordinate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/searchautocompleteoptions)*