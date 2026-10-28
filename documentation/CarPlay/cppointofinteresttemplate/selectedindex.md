# selectedIndex

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The current selection’s index.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var selectedIndex: Int { get set }
```

```objc
@property (nonatomic, assign) NSUInteger selectedIndex;
```

## Discussion

The value of the property must be within the bounds of the [`pointsOfInterest`](./pointsofinterest.md) array, or [`NSNotFound`](../../Foundation/nsnotfound-4qp9h.md) to indicate no selection.

## See Also

### Managing the Points of Interest
- [var pointsOfInterest: [CPPointOfInterest]](./pointsofinterest.md)
  The points of interest the template displays on the map and in the scrollable picker.
- [func setPointsOfInterest([CPPointOfInterest], selectedIndex: Int)](./setpointsofinterest%28_,selectedindex%29.md)
  Updates the points of interest and the current selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cppointofinteresttemplate/selectedindex)*