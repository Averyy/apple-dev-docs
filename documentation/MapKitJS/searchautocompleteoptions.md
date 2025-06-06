# SearchAutocompleteOptions

**Framework**: MapKit JS  
**Kind**: struct

Options you provide to constrain an autocomplete request.

**Availability**:
- MapKit JS 5.32.2+

## Declaration

```swift
dictionary SearchAutocompleteOptions {
	string language;
	mapkit.Coordinate coordinate;
	mapkit.CoordinateRegion region;
	string regionPriority;
	boolean includeAddresses;
	boolean includePointsOfInterest;
	boolean includePhysicalFeatures;
	boolean includeQueries;
	mapkit.AddressFilter addressFilter;
	mapkit.PointOfInterestFilter pointOfInterestFilter;
	string limitToCountries;
};
```

## Topics

### Autocomplete search initialization
- [coordinate](searchautocompleteoptions/coordinate.md)
  A map coordinate that provides a hint for the geographic area to search.
- [language](searchautocompleteoptions/language.md)
  A language ID that determines the language for the search result text.
- [region](searchautocompleteoptions/region.md)
  A map region that provides a hint for the geographic area to search.
### Autocomplete search filtering
- [includePhysicalFeatures](searchautocompleteoptions/includephysicalfeatures.md)
  A Boolean value that indicates whether the autocomplete search results include physical features, such as mountain ranges, rivers, and ocean basins.
- [includePointsOfInterest](searchautocompleteoptions/includepointsofinterest.md)
  A Boolean value that indicates whether the search results include points of interest.
- [includeQueries](searchautocompleteoptions/includequeries.md)
  A Boolean value that indicates whether the search results include queries.
- [limitToCountries](searchautocompleteoptions/limittocountries.md)
  A string that constrains search results to within the provided countries.
- [regionPriority](searchautocompleteoptions/regionpriority.md)
  A filter that controls whether results occur outside, or strictly within, the region.
### Address filtering
- [addressFilter](searchautocompleteoptions/addressfilter.md)
  A filter that lists which address options to include or exclude in search results.
- [includeAddresses](searchautocompleteoptions/includeaddresses.md)
  A Boolean value that indicates whether the search results include addresses.
### Points of interest
- [pointOfInterestFilter](searchautocompleteoptions/pointofinterestfilter.md)
  A filter used to include or exclude point of interest categories in search results.

## See Also

- [autocomplete](mapkit.search/autocomplete.md)
  Retrieves a list of autocomplete results for the specified search query.
- [SearchAutocompleteResponse](searchautocompleteresponse.md)
  An object containing the response from an autocomplete request.
- [SearchAutocompleteResult](searchautocompleteresult.md)
  The result of an autocomplete query, including display lines and a coordinate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/searchautocompleteoptions)*