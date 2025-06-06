# MKLocalSearch

**Framework**: MapKit  
**Kind**: class

A utility object for initiating map-based searches and processing the results.

**Availability**:
- iOS 6.1+
- iPadOS 6.1+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
class MKLocalSearch
```

#### Overview

Use an [`MKLocalSearch`](mklocalsearch.md) object to execute a single search request. You might use this class to search for addresses or points of interest on the map. Upon completion of the request, the object delivers the results to the completion handler that you provide.

## Topics

### Creating a search request
- [init(request: MKLocalSearch.Request)](mklocalsearch/init(request:)-12tf0.md)
  Creates and returns a search object with the specified parameters.
- [init(request: MKLocalPointsOfInterestRequest)](mklocalsearch/init(request:)-9x8kn.md)
  Creates and returns a search object for fetching points of interest.
- [MKLocalSearch.Request](mklocalsearch/request.md)
  The parameters to use when searching for points of interest on the map.
- [MKLocalSearch.ResultType](mklocalsearch/resulttype.md)
  Options that indicate types of search results.
### Performing the search
- [func start(completionHandler: (MKLocalSearch.Response?, (any Error)?) -> Void)](mklocalsearch/start(completionhandler:).md)
  Starts the search and delivers the results to the specified completion handler.
- [MKLocalSearch.CompletionHandler](mklocalsearch/completionhandler.md)
  A completion handler block for a search operation.
- [var isSearching: Bool](mklocalsearch/issearching.md)
  A Boolean value that indicates whether the search is in progress.
- [func cancel()](mklocalsearch/cancel.md)
  Cancels an in-progress search operation.
### Getting search results
- [MKLocalSearch.Response](mklocalsearch/response.md)
  The results from a map-based search.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Interacting with nearby points of interest](interacting-with-nearby-points-of-interest.md)
  Provide automatic search completions for a partial search query, search the map for relevant locations nearby, and retrieve details for selected points of interest.
- [enum MKLocalSearchRegionPriority](mklocalsearchregionpriority.md)
  A value that indicates the importance of the configured region.
- [MKLocalSearch.ResultType](mklocalsearch/resulttype.md)
  Options that indicate types of search results.
- [MKAddressFilter.Options](mkaddressfilter/options.md)
  A structure that contains options for filtering results in a search.
- [class MKAddressFilter](mkaddressfilter.md)
  An object that filters which address options to include or exclude in search results.
- [MKLocalSearchCompleter.ResultType](mklocalsearchcompleter/resulttype.md)
  Options that indicate types of search completions.
- [class MKLocalSearchCompleter](mklocalsearchcompleter.md)
  A utility object for generating a list of completion strings based on a partial search string that you provide.
- [class MKLocalSearchCompletion](mklocalsearchcompletion.md)
  A fully formed string that completes a partial string.
- [class MKLocalPointsOfInterestRequest](mklocalpointsofinterestrequest.md)
  A structured request to use when searching for points of interest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mklocalsearch)*