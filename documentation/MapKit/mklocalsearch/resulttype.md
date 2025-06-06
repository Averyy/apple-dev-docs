# MKLocalSearch.ResultType

**Framework**: MapKit  
**Kind**: struct

Options that indicate types of search results.

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

#### Overview

These options configure the types of search results you want to receive from [`MKLocalSearch.Request`](mklocalsearch/request.md), including points of interest and addresses.

## Topics

### Creating the result type
- [init(rawValue: UInt)](mklocalsearch/resulttype/init(rawvalue:).md)
  Creates a search result type from the provided value.
### Specifying types of search results
- [static var address: MKLocalSearch.ResultType](mklocalsearch/resulttype/address.md)
  A value that indicates that search results include addresses.
- [static var pointOfInterest: MKLocalSearch.ResultType](mklocalsearch/resulttype/pointofinterest.md)
  A value that indicates that search results include points of interest.
- [static var physicalFeature: MKLocalSearch.ResultType](mklocalsearch/resulttype/physicalfeature.md)
  A value that indicates that search results include physical features.
- [static var address: MKLocalSearch.ResultType](mklocalsearch/resulttype/address.md)
  A value that indicates that search results include addresses.
- [static var pointOfInterest: MKLocalSearch.ResultType](mklocalsearch/resulttype/pointofinterest.md)
  A value that indicates that search results include points of interest.
- [static var physicalFeature: MKLocalSearch.ResultType](mklocalsearch/resulttype/physicalfeature.md)
  A value that indicates that search results include physical features.

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
- [class MKLocalSearch](mklocalsearch.md)
  A utility object for initiating map-based searches and processing the results.
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

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mklocalsearch/resulttype)*