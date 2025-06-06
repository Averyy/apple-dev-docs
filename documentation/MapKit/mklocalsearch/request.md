# MKLocalSearch.Request

**Framework**: MapKit  
**Kind**: class

The parameters to use when searching for points of interest on the map.

**Availability**:
- iOS 6.1+
- iPadOS 6.1+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
class Request
```

#### Overview

You create an [`MKLocalSearch.Request`](mklocalsearch/request.md) object when you want to search for map locations based on a natural language string. For example, if your interface allows the user to type in addresses, place the typed text in this object and pass it to an [`MKLocalSearch`](mklocalsearch.md) object to begin the search process. When specifying your search strings, include a map region to narrow the search results to the specified geographical area.

When creating an MKLocalSearch.Request object yourself, set the [`naturalLanguageQuery`](mklocalsearch/request/naturallanguagequery.md) property to an appropriate search string, as in the following example:

If your app uses an [`MKLocalSearchCompleter`](mklocalsearchcompleter.md) object to implement autocomplete support for user-supplied search strings, initialize your search request using the search completion that the user selects. In that case, use the [`init(completion:)`](mklocalsearch/request/init(completion:).md) method instead of the [`init()`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/init()) method to initialize your search request object. The completion object automatically provides the value for the [`naturalLanguageQuery`](mklocalsearch/request/naturallanguagequery.md) property.

## Topics

### Creating a local search request
- [init()](mklocalsearch/request/init.md)
  Creates a local search request.
- [init(completion: MKLocalSearchCompletion)](mklocalsearch/request/init(completion:).md)
  Creates and returns a search request based on the specified search completion data.
### Configuring the search parameters
- [var addressFilter: MKAddressFilter?](mklocalsearch/request/addressfilter.md)
  A filter that lists which address options to include or exclude in search results.
- [var naturalLanguageQuery: String?](mklocalsearch/request/naturallanguagequery.md)
  A string containing the desired search item.
- [var region: MKCoordinateRegion](mklocalsearch/request/region.md)
  A map region that provides a hint as to where to search.
- [static var physicalFeature: MKLocalSearch.ResultType](mklocalsearch/resulttype/physicalfeature.md)
  A value that indicates that search results include physical features.
- [var pointOfInterestFilter: MKPointOfInterestFilter?](mklocalsearch/request/pointofinterestfilter.md)
  A filter that lists point-of-interest categories to include or exclude in search results.
- [var regionPriority: MKLocalSearchRegionPriority](mklocalsearch/request/regionpriority.md)
  A value that indicates the importance of the configured region.
- [var resultTypes: MKLocalSearch.ResultType](mklocalsearch/request/resulttypes.md)
  The types of items to include in the search results.
- [MKLocalSearch.Request.ResultType](mklocalsearch/request/resulttype.md)
  Options that indicate types of search results.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [init(request: MKLocalSearch.Request)](mklocalsearch/init(request:)-12tf0.md)
  Creates and returns a search object with the specified parameters.
- [init(request: MKLocalPointsOfInterestRequest)](mklocalsearch/init(request:)-9x8kn.md)
  Creates and returns a search object for fetching points of interest.
- [MKLocalSearch.ResultType](mklocalsearch/resulttype.md)
  Options that indicate types of search results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mklocalsearch/request)*