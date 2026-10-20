# showsPointsOfInterest

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the map displays point-of-interest information.

**Availability**:
- iOS 7.0+ - Deprecated in 13.0
- iPadOS 7.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.9+ - Deprecated in 10.15
- tvOS 9.2+ - Deprecated in 13.0

> **Deprecated**: Use [`pointOfInterestFilter`](./pointofinterestfilter.md) instead.

## Declaration

```swift
var showsPointsOfInterest: Bool { get set }
```

```objc
@property (nonatomic) BOOL showsPointsOfInterest;
```

#### Discussion

When this property is set to [`true`](../../Swift/true.md), the map displays icons and labels for restaurants, schools, and other relevant points of interest. The [`mapType`](./maptype.md) property must be set to [`MKMapType.standard`](../mkmaptype/standard.md) or [`MKMapType.hybrid`](../mkmaptype/hybrid.md) for points of interest to be displayed.The default value of this property is [`true`](../../Swift/true.md).

## See Also

### Properties
- [var filterType: MKLocalSearchCompleter.FilterType](../mklocalsearchcompleter/filtertype-swift.property.md)
  The filter options for the search results.
- [var pinColor: MKPinAnnotationColor](../mkpinannotationview/pincolor.md)
  The color of the pin head.
- [var showsPointsOfInterest: Bool](../mkmapsnapshotter/options/showspointsofinterest.md)
  A Boolean value that indicates whether the map displays point-of-interest information.
- [var mapType: MKMapType](../mkmapsnapshotter/options/maptype.md)
  The map’s visual style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/showspointsofinterest)*