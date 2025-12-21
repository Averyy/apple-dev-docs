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

- [enum MKMapType](mkmaptype.md)
  The type of map to display.
- [enum MKPinAnnotationColor](mkpinannotationcolor.md)
  The supported colors for pin annotations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mklocalsearchcompleter/filtertype-swift.enum)*