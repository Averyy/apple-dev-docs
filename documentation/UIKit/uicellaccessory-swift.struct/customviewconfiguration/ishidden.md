# isHidden

**Framework**: UIKit  
**Kind**: property

A Boolean value that determines whether the cell hides the accessory.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
var isHidden: Bool
```

#### Discussion

A hidden accessory takes up space in the layout, but it isn’t visible and doesn’t provide any behaviors.

Use this property to achieve a consistent layout across cells when some cells show this type of accessory and others don’t.

## See Also

- [let customView: UIView](uicellaccessory-swift.struct/customviewconfiguration/customview.md)
  The custom view to display for the accessory.
- [let placement: UICellAccessory.Placement](uicellaccessory-swift.struct/customviewconfiguration/placement.md)
  The placement for the accessory.
- [var reservedLayoutWidth: UICellAccessory.LayoutDimension](uicellaccessory-swift.struct/customviewconfiguration/reservedlayoutwidth.md)
  The layout width that the system reserves for the accessory, and then centers the accessory within.
- [var tintColor: UIColor?](uicellaccessory-swift.struct/customviewconfiguration/tintcolor.md)
  The tint color to apply to the accessory.
- [var maintainsFixedSize: Bool](uicellaccessory-swift.struct/customviewconfiguration/maintainsfixedsize.md)
  A Boolean value that determines whether to preserve the frame size of the custom view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicellaccessory-swift.struct/customviewconfiguration/ishidden)*