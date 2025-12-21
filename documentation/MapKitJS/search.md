# Search

**Framework**: MapKit JS  
**Kind**: class

An object that retrieves map-based search results for a user-entered query.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
class Search extends Service
```

## Mentions

- [MapKit JS 5](mapkit-js-5.md)

#### Overview

The search service allows developers to populate a map with results from a user-entered query, including information about businesses and other points of interest. MapKit JS provides this functionality through a search object that makes network requests to the search service.

Supplying  creates the most relevant results for a query. Context may include the user’s location, or a coordinate or region that the developer provides.

To use the search service, create an instance of a search object with the desired options. Use the search object to make search requests.

## Topics

### Creating a search
- [new Search(options)](search/searchconstructor.md)
  Creates a search object with optional initial values that you provide.
- [interface SearchConstructorOptions](searchconstructoroptions.md)
  Options you provide when you create a search object.
### Performing a search
- [search(query, callback, options)](search/search.md)
  Retrieves the results of a search query.
- [type SearchDelegate](searchdelegate.md)
  An object or callback function the framework calls when performing a search or an autocomplete request.
- [interface SearchOptions](searchoptions.md)
  An object that contains options to adjust a search.
- [interface SearchResponse](searchresponse.md)
  The result of a search, including the original search query, the bounding region, and a list of places that match the query.
### Performing a search autocomplete
- [autocomplete(query, callback, options)](search/autocomplete.md)
  Retrieves a list of autocomplete results for the specified search query.
- [interface SearchAutocompleteOptions](searchautocompleteoptions.md)
  Options you provide to constrain an autocomplete request.
- [interface SearchAutocompleteResponse](searchautocompleteresponse.md)
  An object containing the response from an autocomplete request.
- [class SearchAutocompleteResult](searchautocompleteresult.md)
  The result of an autocomplete query, including display lines and a coordinate.
### Filtering a search
- [const AddressCategory](addresscategory.md)
  The categories of address components that users can search for with an address filter.
- [class AddressFilter](addressfilter.md)
  An object that filters which address options to include or exclude in search results.
### Canceling a search
- [cancel(id)](service/cancel.md)
  Cancels a request using the provided request ID.
### Static properties
- [RegionPriority](search/regionpriority-data.var.md)
  A static property that allows you to access region priority enumeration.
### Instance Properties
- [addressFilter](search/addressfilter.md)
  An filter that lists which address components to include or exclude in search results.
- [coordinate](search/coordinate.md)
  A map coordinate that provides a hint for the geographic area to search.
- [includeAddresses](search/includeaddresses.md)
  A Boolean value that indicates whether the search results include addresses.
- [includePhysicalFeatures](search/includephysicalfeatures.md)
  A Boolean value that indicates whether the search results include physical features, such as mountain ranges, rivers, and ocean basins.
- [includePointsOfInterest](search/includepointsofinterest.md)
  A Boolean value that indicates whether the search results should include points of interest.
- [includeQueries](search/includequeries.md)
  A Boolean value that indicates whether the search results include queries.
- [limitToCountries](search/limittocountries.md)
  A string that constrains search results to be within the provided countries.
- [pointOfInterestFilter](search/pointofinterestfilter.md)
  A filter to use to include or exclude point-of-interest categories.
- [region](search/region.md)
  A map region that provides a hint about the geographic area to search.
- [regionPriority](search/regionpriority-data.property.md)
  A region priority value that controls whether results occur outside, or strictly within, the region.

## Relationships

### Inherits From
- [Service](service.md)

## See Also

- [const AddressCategory](addresscategory.md)
  The categories of address components that users can search for with an address filter.
- [class AddressFilter](addressfilter.md)
  An object that filters which address options to include or exclude in search results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/search)*