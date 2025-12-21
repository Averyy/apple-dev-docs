# pinColor

**Framework**: MapKit  
**Kind**: property

The color of the pin head.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.9+

## Declaration

```swift
@MainActor
var pinColor: MKPinAnnotationColor { get set }
```

#### Discussion

The Maps application uses different pin colors for different types of map annotations. Your own map annotation should use the available pin colors in the same way. For a description of when to use each type of pin, see the constants of [`MKPinAnnotationColor`](mkpinannotationcolor.md).

## See Also

- [var filterType: MKLocalSearchCompleter.FilterType](mklocalsearchcompleter/filtertype-swift.property.md)
  The filter options for the search results.
- [var showsPointsOfInterest: Bool](mkmapview/showspointsofinterest.md)
  A Boolean value that indicates whether the map displays point-of-interest information.
- [var showsPointsOfInterest: Bool](mkmapsnapshotter/options/showspointsofinterest.md)
  A Boolean value that indicates whether the map displays point-of-interest information.
- [var mapType: MKMapType](mkmapsnapshotter/options/maptype.md)
  The map’s visual style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkpinannotationview/pincolor)*