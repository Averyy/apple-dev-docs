# MKLocalSearchCompleter.ResultType

**Framework**: MapKit  
**Kind**: struct

Options that indicate types of search completions.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
struct ResultType
```

## Topics

### Type properties
- [static var address: MKLocalSearchCompleter.ResultType](mklocalsearchcompleter/resulttype/address.md)
  A value that indicates that the search completer includes address completions in the result.
- [static var pointOfInterest: MKLocalSearchCompleter.ResultType](mklocalsearchcompleter/resulttype/pointofinterest.md)
  A value that indicates that the search completer includes point-of-interest completions in the result.
- [static var physicalFeature: MKLocalSearchCompleter.ResultType](mklocalsearchcompleter/resulttype/physicalfeature.md)
  A value that indicates that the search completer includes physical feature completions in the result.
- [static var query: MKLocalSearchCompleter.ResultType](mklocalsearchcompleter/resulttype/query.md)
  A value that indicates that the search completer includes query completions in the result.
### Initializers
- [init(rawValue: UInt)](mklocalsearchcompleter/resulttype/init(rawvalue:).md)
  Creates a direction transport type using a raw unsigned integer value.
- [static var address: MKLocalSearchCompleter.ResultType](mklocalsearchcompleter/resulttype/address.md)
  A value that indicates that the search completer includes address completions in the result.
- [static var pointOfInterest: MKLocalSearchCompleter.ResultType](mklocalsearchcompleter/resulttype/pointofinterest.md)
  A value that indicates that the search completer includes point-of-interest completions in the result.
- [static var physicalFeature: MKLocalSearchCompleter.ResultType](mklocalsearchcompleter/resulttype/physicalfeature.md)
  A value that indicates that the search completer includes physical feature completions in the result.
- [static var query: MKLocalSearchCompleter.ResultType](mklocalsearchcompleter/resulttype/query.md)
  A value that indicates that the search completer includes query completions in the result.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

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
- [class MKLocalSearchCompleter](mklocalsearchcompleter.md)
  A utility object for generating a list of completion strings based on a partial search string that you provide.
- [class MKLocalSearchCompletion](mklocalsearchcompletion.md)
  A fully formed string that completes a partial string.
- [class MKLocalPointsOfInterestRequest](mklocalpointsofinterestrequest.md)
  A structured request to use when searching for points of interest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mklocalsearchcompleter/resulttype)*