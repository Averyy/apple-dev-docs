# setPointsOfInterest(_:selectedIndex:)

**Framework**: CarPlay  
**Kind**: method

Updates the points of interest and the current selection.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
func setPointsOfInterest(_ pointsOfInterest: [CPPointOfInterest], selectedIndex: Int)
```

#### Discussion

`pointsOfInterest` can contain a maximum of twelve points of interest because that is the most the template displays.

## Parameters

- `pointsOfInterest`: An array that contains the points of interest the template displays.
- `selectedIndex`: The selection’s index. This is the array’s index for the specific point of interest you want to select. Use   to indicate no initial selection.

## See Also

- [var pointsOfInterest: [CPPointOfInterest]](cppointofinteresttemplate/pointsofinterest.md)
  The points of interest the template displays on the map and in the scrollable picker.
- [var selectedIndex: Int](cppointofinteresttemplate/selectedindex.md)
  The current selection’s index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cppointofinteresttemplate/setpointsofinterest(_:selectedindex:))*