# mapkit.Search

**Framework**: MapKit JS  
**Kind**: class

An object that retrieves map-based search results for a user-entered query.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
interface mapkit.Search
```

#### Overview

The search service allows developers to populate a map with results from a user-entered query, including information about businesses and other points of interest. MapKit JS provides this functionality through a search object that makes network requests to the search service.

Supplying  creates the most relevant results for a query. Context may include the user’s location, or a coordinate or region that the developer provides.

To use the search service, create an instance of a search object with the desired options. Use the search object to make search requests.

## Topics

### Creating a search
- [mapkit.Search](mapkit.search/mapkit.search.md)
  Creates a search object with optional initial values that you provide.
- [SearchConstructorOptions](searchconstructoroptions.md)
  Options you provide when you create a search object.
### Performing a search
- [search](mapkit.search/search.md)
  Retrieves the results of a search query.
- [SearchDelegate](searchdelegate.md)
  An object or callback function the framework calls when performing a search or an autocomplete request.
- [SearchOptions](searchoptions.md)
  An object that contains options to adjust a search.
- [SearchResponse](searchresponse.md)
  The result of a search, including the original search query, the bounding region, and a list of places that match the query.
### Performing a search autocomplete
- [autocomplete](mapkit.search/autocomplete.md)
  Retrieves a list of autocomplete results for the specified search query.
- [SearchAutocompleteOptions](searchautocompleteoptions.md)
  Options you provide to constrain an autocomplete request.
- [SearchAutocompleteResponse](searchautocompleteresponse.md)
  An object containing the response from an autocomplete request.
- [SearchAutocompleteResult](searchautocompleteresult.md)
  The result of an autocomplete query, including display lines and a coordinate.
### Filtering a search
- [mapkit.AddressCategory](mapkit.addresscategory.md)
  The categories of address components that users can search for with an address filter.
- [mapkit.AddressFilter](mapkit.addressfilter.md)
  An object that filters which address options to include or exclude in search results.
- [mapkit.Search.RegionPriority](mapkit.search.regionpriority.md)
  A value that indicates the importance of the configured region.
### Canceling a search
- [cancel](mapkit.search/cancel.md)
  Cancels a search request using its request ID.

## See Also

- [mapkit.AddressCategory](mapkit.addresscategory.md)
  The categories of address components that users can search for with an address filter.
- [mapkit.AddressFilter](mapkit.addressfilter.md)
  An object that filters which address options to include or exclude in search results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.search)*