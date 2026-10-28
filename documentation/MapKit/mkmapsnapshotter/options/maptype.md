# mapType

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

The map’s visual style.

**Availability**:
- iOS 7.0+ - Deprecated in 27.2
- iPadOS 7.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.2
- macOS 10.9+ - Deprecated in 27.2
- tvOS 9.2+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`preferredConfiguration`](./preferredconfiguration.md) instead.

## Declaration

```swift
var mapType: MKMapType { get set }
```

```objc
@property (nonatomic, assign) MKMapType mapType;
```

## Discussion

The default value of this property is [`MKMapType.standard`](../../mkmaptype/standard.md).

## See Also

### Properties
- [var filterType: MKLocalSearchCompleter.FilterType](../../mklocalsearchcompleter/filtertype-swift.property.md)
  The filter options for the search results.
- [var pinColor: MKPinAnnotationColor](../../mkpinannotationview/pincolor.md)
  The color of the pin head.
- [var showsPointsOfInterest: Bool](../../mkmapview/showspointsofinterest.md)
  A Boolean value that indicates whether the map displays point-of-interest information.
- [var showsPointsOfInterest: Bool](./showspointsofinterest.md)
  A Boolean value that indicates whether the map displays point-of-interest information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapsnapshotter/options/maptype)*