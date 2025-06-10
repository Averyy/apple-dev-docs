# MKLocalSearchCompleter.FilterType

**Framework**: MapKit  
**Kind**: enum

Constants indicating the types of search completions to return.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- Mac Catalyst 13.1+
- macOS 10.11.4+
- tvOS 9.2+

## Declaration

```swift
enum FilterType
```

## Topics

### Constants
- [MKLocalSearchCompleter.FilterType.locationsAndQueries](mklocalsearchcompleter/filtertype-swift.enum/locationsandqueries.md)
  Points of interest and query suggestions. Specify this value when you want both map-based points of interest and common query terms used to find locations. For example, the search string `cof` yields a completion for .
- [MKLocalSearchCompleter.FilterType.locationsOnly](mklocalsearchcompleter/filtertype-swift.enum/locationsonly.md)
  Points of interest only. Specify this value when you want the search string to yield completions that correspond to a specific point-of-interest on the map.
- [MKLocalSearchCompleter.FilterType.locationsAndQueries](mklocalsearchcompleter/filtertype-swift.enum/locationsandqueries.md)
  Points of interest and query suggestions. Specify this value when you want both map-based points of interest and common query terms used to find locations. For example, the search string `cof` yields a completion for .
- [MKLocalSearchCompleter.FilterType.locationsOnly](mklocalsearchcompleter/filtertype-swift.enum/locationsonly.md)
  Points of interest only. Specify this value when you want the search string to yield completions that correspond to a specific point-of-interest on the map.
### Initializers
- [init?(rawValue: Int)](mklocalsearchcompleter/filtertype-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

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
- [MKLocalSearchCompleter.ResultType](mklocalsearchcompleter/resulttype.md)
  Options that indicate types of search completions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mklocalsearchcompleter/filtertype-swift.enum)*