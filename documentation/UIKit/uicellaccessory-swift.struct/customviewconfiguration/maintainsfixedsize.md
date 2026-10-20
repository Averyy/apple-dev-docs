# maintainsFixedSize

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether to preserve the frame size of the custom view.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS

## Declaration

```swift
var maintainsFixedSize: Bool
```

#### Discussion

When the value of this property is [`true`](../../../Swift/true.md), the system preserves the current frame size of the view. When the value of this property is [`false`](../../../Swift/false.md), the system sizes the view during layout of the accessories.

The default value of this property is [`false`](../../../Swift/false.md).

## See Also

### Accessing configuration options
- [var isHidden: Bool](./ishidden.md)
  A Boolean value that determines whether the cell hides the accessory.
- [let customView: UIView](./customview.md)
  The custom view to display for the accessory.
- [let placement: UICellAccessory.Placement](./placement.md)
  The placement for the accessory.
- [var reservedLayoutWidth: UICellAccessory.LayoutDimension](./reservedlayoutwidth.md)
  The layout width that the system reserves for the accessory, and then centers the accessory within.
- [var tintColor: UIColor?](./tintcolor.md)
  The tint color to apply to the accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicellaccessory-swift.struct/customviewconfiguration/maintainsfixedsize)*