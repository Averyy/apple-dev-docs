# MKLocalSearchCompletion

**Framework**: MapKit  
**Kind**: class

A fully formed string that completes a partial string.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- Mac Catalyst 13.1+
- macOS 10.11.4+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
class MKLocalSearchCompletion
```

#### Overview

You don’t create instances of this class directly. Instead, you use an [`MKLocalSearchCompleter`](mklocalsearchcompleter.md) to initiate a search based on a set of partial search strings. That object stores any matches in its results property. Retrieve any `MKLocalSearchCompletion` objects from that property and display the search terms in your interface, or use one to initiate a search for content based on that search term.

When displaying text completions for a partial search term in your user interface, you might want to use a bold version of a font or add some other highlighting to the portion of the completion string that causes it to match the partial search term. To help you add this styling, the completion object includes highlight ranges for the title and subtitle strings.

## Topics

### Getting the search completions
- [var title: String](mklocalsearchcompletion/title.md)
  The title string associated with the point of interest.
- [var subtitle: String](mklocalsearchcompletion/subtitle.md)
  The subtitle (if any) associated with the point of interest.
- [var titleHighlightRanges: [NSValue]](mklocalsearchcompletion/titlehighlightranges.md)
  The ranges of characters to highlight in the title string.
- [var subtitleHighlightRanges: [NSValue]](mklocalsearchcompletion/subtitlehighlightranges.md)
  The ranges of characters to highlight in the subtitle string.

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
- [class MKLocalSearchCompleter](mklocalsearchcompleter.md)
  A utility object for generating a list of completion strings based on a partial search string that you provide.
- [class MKLocalPointsOfInterestRequest](mklocalpointsofinterestrequest.md)
  A structured request to use when searching for points of interest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mklocalsearchcompletion)*