# maintainsFixedSize

**Framework**: UIKit  
**Kind**: property

A Boolean value that determines whether to preserve the frame size of the custom view.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
var maintainsFixedSize: Bool
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/swift/true), the system preserves the current frame size of the view. When the value of this property is [`false`](https://developer.apple.com/documentation/swift/false), the system sizes the view during layout of the accessories.

The default value of this property is [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var isHidden: Bool](uicellaccessory-swift.struct/customviewconfiguration/ishidden.md)
  A Boolean value that determines whether the cell hides the accessory.
- [let customView: UIView](uicellaccessory-swift.struct/customviewconfiguration/customview.md)
  The custom view to display for the accessory.
- [let placement: UICellAccessory.Placement](uicellaccessory-swift.struct/customviewconfiguration/placement.md)
  The placement for the accessory.
- [var reservedLayoutWidth: UICellAccessory.LayoutDimension](uicellaccessory-swift.struct/customviewconfiguration/reservedlayoutwidth.md)
  The layout width that the system reserves for the accessory, and then centers the accessory within.
- [var tintColor: UIColor?](uicellaccessory-swift.struct/customviewconfiguration/tintcolor.md)
  The tint color to apply to the accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicellaccessory-swift.struct/customviewconfiguration/maintainsfixedsize)*