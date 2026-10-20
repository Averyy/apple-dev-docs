# MKLocalSearchCompleter.FilterType.locationsOnly

**Framework**: MapKit  
**Kind**: case  
**Role**: Case

Points of interest only. Specify this value when you want the search string to yield completions that correspond to a specific point-of-interest on the map.

**Availability**:
- iOS 9.3+ - Deprecated in 13.0
- iPadOS 9.3+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.11.4+ - Deprecated in 10.15
- tvOS 9.2+ - Deprecated in 13.0

> **Deprecated**: Use one of the options available in [`MKLocalSearchCompleter.ResultType`](../resulttype.md) instead.

## Declaration

```swift
case locationsOnly
```

```c
MKSearchCompletionFilterTypeLocationsOnly
```

## See Also

### Constants
- [MKLocalSearchCompleter.FilterType.locationsAndQueries](./locationsandqueries.md)
  Points of interest and query suggestions. Specify this value when you want both map-based points of interest and common query terms used to find locations. For example, the search string `cof` yields a completion for *coffee*.
- [MKLocalSearchCompleter.FilterType.locationsAndQueries](./locationsandqueries.md)
  Points of interest and query suggestions. Specify this value when you want both map-based points of interest and common query terms used to find locations. For example, the search string `cof` yields a completion for *coffee*.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mklocalsearchcompleter/filtertype-swift.enum/locationsonly)*