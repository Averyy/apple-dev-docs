# pointsOfInterest

**Framework**: CarPlay  
**Kind**: property

The points of interest the template displays on the map and in the scrollable picker.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
@MainActor
var pointsOfInterest: [CPPointOfInterest] { get }
```

#### Discussion

You must call the [`setPointsOfInterest(_:selectedIndex:)`](cppointofinteresttemplate/setpointsofinterest(_:selectedindex:).md) method to update the points of interest the template displays.

## See Also

- [func setPointsOfInterest([CPPointOfInterest], selectedIndex: Int)](cppointofinteresttemplate/setpointsofinterest(_:selectedindex:).md)
  Updates the points of interest and the current selection.
- [var selectedIndex: Int](cppointofinteresttemplate/selectedindex.md)
  The current selection’s index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cppointofinteresttemplate/pointsofinterest)*