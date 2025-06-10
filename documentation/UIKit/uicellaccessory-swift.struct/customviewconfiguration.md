# UICellAccessory.CustomViewConfiguration

**Framework**: UIKit  
**Kind**: struct

Configuration options for a custom accessory.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
struct CustomViewConfiguration
```

## Topics

### Creating configuration options
- [init(customView: UIView, placement: UICellAccessory.Placement, isHidden: Bool?, reservedLayoutWidth: UICellAccessory.LayoutDimension?, tintColor: UIColor?, maintainsFixedSize: Bool?)](uicellaccessory-swift.struct/customviewconfiguration/init(customview:placement:ishidden:reservedlayoutwidth:tintcolor:maintainsfixedsize:).md)
  Creates a custom accessory options structure.
### Accessing configuration options
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
- [var maintainsFixedSize: Bool](uicellaccessory-swift.struct/customviewconfiguration/maintainsfixedsize.md)
  A Boolean value that determines whether to preserve the frame size of the custom view.

## See Also

- [static func customView(configuration: UICellAccessory.CustomViewConfiguration) -> UICellAccessory](uicellaccessory-swift.struct/customview(configuration:).md)
  Creates a custom view accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicellaccessory-swift.struct/customviewconfiguration)*