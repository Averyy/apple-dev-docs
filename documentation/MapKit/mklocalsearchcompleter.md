# MKLocalSearchCompleter

**Framework**: MapKit  
**Kind**: class

A utility object for generating a list of completion strings based on a partial search string that you provide.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- Mac Catalyst 13.1+
- macOS 10.11.4+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
class MKLocalSearchCompleter
```

#### Overview

You use an [`MKLocalSearchCompleter`](mklocalsearchcompleter.md) object to retrieve auto-complete suggestions for your own map-based search controls. As the user types text, you feed the current text string into the search completer object, which delivers possible string completions that match locations or points of interest.

You create and configure [`MKLocalSearchCompleter`](mklocalsearchcompleter.md) objects yourself. You must always assign a delegate object to the search completer so that you can receive the search results that it generates. Specify a search region to restrict results to a designated area. The following code shows a simple example of a view controller that stores the [`MKLocalSearchCompleter`](mklocalsearchcompleter.md) object in a property. The view controller itself acts as the delegate for the completer and the view controller uses the region associated with an [`MKMapView`](mkmapview.md) object that’s part of the view controller’s interface. Completer objects are long-lived objects, so you can store strong references to them and reuse them later in your code.

Listing 1. Creating and configuring a search completer

Update the value of the completer’s [`queryFragment`](mklocalsearchcompleter/queryfragment.md) property to begin a search query. You can update this property in real time as the user types new characters into a text field because the completer object waits a short amount of time for the query string to stabilize. When modifications to the query string stop, the completer initiates a new search and returns the results to your delegate as an array of [`MKLocalSearchCompletion`](mklocalsearchcompletion.md) objects.

## Topics

### Receiving the search results
- [var delegate: (any MKLocalSearchCompleterDelegate)?](mklocalsearchcompleter/delegate.md)
  The object that receives the completion results.
- [protocol MKLocalSearchCompleterDelegate](mklocalsearchcompleterdelegate.md)
  Methods the delegate calls with search completion data.
### Specifying the query attributes
- [var addressFilter: MKAddressFilter?](mklocalsearchcompleter/addressfilter.md)
  A filter that lists which address options to include or exclude in search results.
- [var queryFragment: String](mklocalsearchcompleter/queryfragment.md)
  The search string that you want completions for.
- [var region: MKCoordinateRegion](mklocalsearchcompleter/region.md)
  The region that defines the geographic scope of the search.
- [var regionPriority: MKLocalSearchRegionPriority](mklocalsearchcompleter/regionpriority.md)
  A value that indicates the importance of the configured region.
- [var resultTypes: MKLocalSearchCompleter.ResultType](mklocalsearchcompleter/resulttypes.md)
  The types of search completions to include.
- [var pointOfInterestFilter: MKPointOfInterestFilter?](mklocalsearchcompleter/pointofinterestfilter.md)
  A filter that lists point of interest categories to include or exclude in the search.
- [var filterType: MKLocalSearchCompleter.FilterType](mklocalsearchcompleter/filtertype-swift.property.md)
  The filter options for the search results.
- [MKLocalSearchCompleter.FilterType](mklocalsearchcompleter/filtertype-swift.enum.md)
  Constants indicating the types of search completions to return.
- [MKLocalSearchCompleter.ResultType](mklocalsearchcompleter/resulttype.md)
  Options that indicate types of search completions.
### Canceling the query
- [func cancel()](mklocalsearchcompleter/cancel.md)
  Cancels an in-progress search operation.
- [var isSearching: Bool](mklocalsearchcompleter/issearching.md)
  A Boolean value that indicates whether a search operation is in progress.
### Getting the current query results
- [var results: [MKLocalSearchCompletion]](mklocalsearchcompleter/results.md)
  The most recently received search completions.

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
- [class MKLocalSearch](mklocalsearch.md)
  A utility object for initiating map-based searches and processing the results.
- [MKAddressFilter.Options](mkaddressfilter/options.md)
  A structure that contains options for filtering results in a search.
- [class MKAddressFilter](mkaddressfilter.md)
  An object that filters which address options to include or exclude in search results.
- [MKLocalSearchCompleter.ResultType](mklocalsearchcompleter/resulttype.md)
  Options that indicate types of search completions.
- [class MKLocalSearchCompletion](mklocalsearchcompletion.md)
  A fully formed string that completes a partial string.
- [class MKLocalPointsOfInterestRequest](mklocalpointsofinterestrequest.md)
  A structured request to use when searching for points of interest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mklocalsearchcompleter)*