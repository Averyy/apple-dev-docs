# SearchConstructorOptions

**Framework**: MapKit JS  
**Kind**: struct

Options you provide when you create a search object.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
dictionary SearchConstructorOptions {
	string language;
	boolean getsUserLocation;
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

### Search Initialization
- [coordinate](searchconstructoroptions/coordinate.md)
  A map coordinate that provides a hint for the geographic area to search.
- [getsUserLocation](searchconstructoroptions/getsuserlocation.md)
  A Boolean value that indicates whether to limit the search results to the user’s location, according to the web browser.
- [language](searchconstructoroptions/language.md)
  A language ID that determines the language for the search results text.
- [region](searchconstructoroptions/region.md)
  A map region that provides a hint for the geographic area to search.
### Search filtering
- [includePhysicalFeatures](searchconstructoroptions/includephysicalfeatures.md)
  A Boolean value that indicates whether the search results include physical features, such as mountain ranges, rivers, and ocean basins.
- [includeQueries](searchconstructoroptions/includequeries.md)
  A Boolean value that indicates whether the search results include queries.
- [limitToCountries](searchconstructoroptions/limittocountries.md)
  A string that constrains search results to within the provided countries.
- [regionPriority](searchconstructoroptions/regionpriority.md)
  A filter that controls whether results occur outside, or strictly within, the region.
### Address filtering
- [addressFilter](searchconstructoroptions/addressfilter.md)
  A filter that lists which address components to include or exclude in search results.
- [includeAddresses](searchconstructoroptions/includeaddresses.md)
  A Boolean value that indicates whether the search results include addresses.
### Points of Interest
- [includePointsOfInterest](searchconstructoroptions/includepointsofinterest.md)
  A Boolean value that indicates whether the search results should include points of interest.
- [pointOfInterestFilter](searchconstructoroptions/pointofinterestfilter.md)
  A filter used to include or exclude point of interest categories.

## See Also

- [mapkit.Search](mapkit.search/mapkit.search.md)
  Creates a search object with optional initial values that you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/searchconstructoroptions)*