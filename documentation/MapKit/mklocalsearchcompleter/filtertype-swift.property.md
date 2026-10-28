# filterType

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

The filter options for the search results.

**Availability**:
- iOS 9.3+ - Deprecated in 13.0
- iPadOS 9.3+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.11.4+ - Deprecated in 10.15
- tvOS 9.2+ - Deprecated in 13.0

> **Deprecated**: Use [`resultTypes`](./resulttypes.md) instead.

## Declaration

```swift
var filterType: MKLocalSearchCompleter.FilterType { get set }
```

```objc
@property (nonatomic, assign) MKSearchCompletionFilterType filterType;
```

## Discussion

Use this property to determine whether you want completions that represent points-of-interest or whether completions might yield additional relevant query strings.

## See Also

### Properties
- [var pinColor: MKPinAnnotationColor](../mkpinannotationview/pincolor.md)
  The color of the pin head.
- [var showsPointsOfInterest: Bool](../mkmapview/showspointsofinterest.md)
  A Boolean value that indicates whether the map displays point-of-interest information.
- [var showsPointsOfInterest: Bool](../mkmapsnapshotter/options/showspointsofinterest.md)
  A Boolean value that indicates whether the map displays point-of-interest information.
- [var mapType: MKMapType](../mkmapsnapshotter/options/maptype.md)
  The map’s visual style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mklocalsearchcompleter/filtertype-swift.property)*