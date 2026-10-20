# UICellAccessory.CustomViewConfiguration

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

Configuration options for a custom accessory.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS

## Declaration

```swift
struct CustomViewConfiguration
```

## Topics

### Creating configuration options
- [init(customView: UIView, placement: UICellAccessory.Placement, isHidden: Bool?, reservedLayoutWidth: UICellAccessory.LayoutDimension?, tintColor: UIColor?, maintainsFixedSize: Bool?)](./customviewconfiguration/init%28customview,placement,ishidden,reservedlayoutwidth,tintcolor,maintainsfixedsize%29.md)
  Creates a custom accessory options structure.
### Accessing configuration options
- [var isHidden: Bool](./customviewconfiguration/ishidden.md)
  A Boolean value that determines whether the cell hides the accessory.
- [let customView: UIView](./customviewconfiguration/customview.md)
  The custom view to display for the accessory.
- [let placement: UICellAccessory.Placement](./customviewconfiguration/placement.md)
  The placement for the accessory.
- [var reservedLayoutWidth: UICellAccessory.LayoutDimension](./customviewconfiguration/reservedlayoutwidth.md)
  The layout width that the system reserves for the accessory, and then centers the accessory within.
- [var tintColor: UIColor?](./customviewconfiguration/tintcolor.md)
  The tint color to apply to the accessory.
- [var maintainsFixedSize: Bool](./customviewconfiguration/maintainsfixedsize.md)
  A Boolean value that determines whether to preserve the frame size of the custom view.

## See Also

### Creating a custom accessory
- [static func customView(configuration: UICellAccessory.CustomViewConfiguration) -> UICellAccessory](./customview%28configuration%29.md)
  Creates a custom view accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicellaccessory-swift.struct/customviewconfiguration)*