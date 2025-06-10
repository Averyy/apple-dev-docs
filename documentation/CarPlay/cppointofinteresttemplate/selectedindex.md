# selectedIndex

**Framework**: CarPlay  
**Kind**: property

The current selection’s index.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
@MainActor
var selectedIndex: Int { get set }
```

#### Discussion

The value of the property must be within the bounds of the [`pointsOfInterest`](cppointofinteresttemplate/pointsofinterest.md) array, or [`NSNotFound`](https://developer.apple.com/documentation/Foundation/NSNotFound-4qp9h) to indicate no selection.

## See Also

- [var pointsOfInterest: [CPPointOfInterest]](cppointofinteresttemplate/pointsofinterest.md)
  The points of interest the template displays on the map and in the scrollable picker.
- [func setPointsOfInterest([CPPointOfInterest], selectedIndex: Int)](cppointofinteresttemplate/setpointsofinterest(_:selectedindex:).md)
  Updates the points of interest and the current selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cppointofinteresttemplate/selectedindex)*