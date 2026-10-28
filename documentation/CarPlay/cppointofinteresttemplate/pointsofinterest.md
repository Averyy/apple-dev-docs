# pointsOfInterest

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The points of interest the template displays on the map and in the scrollable picker.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var pointsOfInterest: [CPPointOfInterest] { get }
```

```objc
@property (nonatomic, readonly) NSArray<CPPointOfInterest *> * pointsOfInterest;
```

## Discussion

You must call the [`setPointsOfInterest(_:selectedIndex:)`](./setpointsofinterest%28_,selectedindex%29.md) method to update the points of interest the template displays.

## See Also

### Managing the Points of Interest
- [func setPointsOfInterest([CPPointOfInterest], selectedIndex: Int)](./setpointsofinterest%28_,selectedindex%29.md)
  Updates the points of interest and the current selection.
- [var selectedIndex: Int](./selectedindex.md)
  The current selection’s index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cppointofinteresttemplate/pointsofinterest)*