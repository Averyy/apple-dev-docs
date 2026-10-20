# MKLocalSearchCompleter.FilterType

**Framework**: MapKit  
**Kind**: enum  
**Role**: Enumeration

Constants indicating the types of search completions to return.

**Availability**:
- iOS 9.3+ - Deprecated in 13.0
- iPadOS 9.3+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.11.4+ - Deprecated in 10.15
- tvOS 9.2+ - Deprecated in 13.0

> **Deprecated**: Use [`MKLocalSearchCompleter.ResultType`](./resulttype.md) instead.

## Declaration

```swift
enum FilterType
```

```c
enum MKSearchCompletionFilterType : NSInteger;
```

## Topics

### Constants
- [MKLocalSearchCompleter.FilterType.locationsAndQueries](./filtertype-swift.enum/locationsandqueries.md)
  Points of interest and query suggestions. Specify this value when you want both map-based points of interest and common query terms used to find locations. For example, the search string `cof` yields a completion for *coffee*.
- [MKLocalSearchCompleter.FilterType.locationsOnly](./filtertype-swift.enum/locationsonly.md)
  Points of interest only. Specify this value when you want the search string to yield completions that correspond to a specific point-of-interest on the map.
- [MKLocalSearchCompleter.FilterType.locationsAndQueries](./filtertype-swift.enum/locationsandqueries.md)
  Points of interest and query suggestions. Specify this value when you want both map-based points of interest and common query terms used to find locations. For example, the search string `cof` yields a completion for *coffee*.
- [MKLocalSearchCompleter.FilterType.locationsOnly](./filtertype-swift.enum/locationsonly.md)
  Points of interest only. Specify this value when you want the search string to yield completions that correspond to a specific point-of-interest on the map.
### Initializers
- [init?(rawValue: Int)](./filtertype-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Enumerations
- [enum MKMapType](../mkmaptype.md)
  The type of map to display.
- [enum MKPinAnnotationColor](../mkpinannotationcolor.md)
  The supported colors for pin annotations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mklocalsearchcompleter/filtertype-swift.enum)*