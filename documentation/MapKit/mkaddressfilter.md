# MKAddressFilter

**Framework**: MapKit  
**Kind**: class

An object that filters which address options to include or exclude in search results.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
class MKAddressFilter
```

#### Overview

Use this object to filter search results by criteria, such as country, region, and municipality. See [`MKAddressFilter.Options`](mkaddressfilter/options.md) for more information.

## Topics

### Creating a filter
- [init(excluding: MKAddressFilter.Options)](mkaddressfilter/init(excluding:).md)
  Creates an address filter with options for excluding results in a search.
- [init(including: MKAddressFilter.Options)](mkaddressfilter/init(including:).md)
  Creates an address filter with options for including results in a search.
### Filtering results
- [MKAddressFilter.Options](mkaddressfilter/options.md)
  A structure that contains options for filtering results in a search.
- [class var excludingAll: MKAddressFilter](mkaddressfilter/excludingall.md)
  A list of categories to exclude from a search.
- [class var includingAll: MKAddressFilter](mkaddressfilter/includingall.md)
  A list of categories to include in a search.
- [func excludes(MKAddressFilter.Options) -> Bool](mkaddressfilter/excludes(_:).md)
  Indicates whether options are excluded from filtering.
- [func includes(MKAddressFilter.Options) -> Bool](mkaddressfilter/includes(_:).md)
  Indicates whether options are included for filtering.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

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
- [MKLocalSearchCompleter.ResultType](mklocalsearchcompleter/resulttype.md)
  Options that indicate types of search completions.
- [class MKLocalSearchCompleter](mklocalsearchcompleter.md)
  A utility object for generating a list of completion strings based on a partial search string that you provide.
- [class MKLocalSearchCompletion](mklocalsearchcompletion.md)
  A fully formed string that completes a partial string.
- [class MKLocalPointsOfInterestRequest](mklocalpointsofinterestrequest.md)
  A structured request to use when searching for points of interest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkaddressfilter)*