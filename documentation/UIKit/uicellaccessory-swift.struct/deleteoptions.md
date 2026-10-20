# UICellAccessory.DeleteOptions

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

Configuration options for a delete accessory.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS

## Declaration

```swift
struct DeleteOptions
```

## Topics

### Creating configuration options
- [init(isHidden: Bool?, reservedLayoutWidth: UICellAccessory.LayoutDimension?, tintColor: UIColor?, backgroundColor: UIColor?)](./deleteoptions/init%28ishidden,reservedlayoutwidth,tintcolor,backgroundcolor%29.md)
  Creates a delete accessory options structure.
### Accessing configuration options
- [var isHidden: Bool](./deleteoptions/ishidden.md)
  A Boolean value that determines whether the cell hides the accessory.
- [var reservedLayoutWidth: UICellAccessory.LayoutDimension](./deleteoptions/reservedlayoutwidth.md)
  The layout width that the system reserves for the accessory, and then centers the accessory within.
- [var tintColor: UIColor?](./deleteoptions/tintcolor.md)
  The tint color to apply to the accessory.
- [var backgroundColor: UIColor?](./deleteoptions/backgroundcolor.md)
  The background color to apply to the accessory.

## See Also

### Creating a delete accessory
- [static func delete(displayed: UICellAccessory.DisplayedState, options: UICellAccessory.DeleteOptions, actionHandler: UICellAccessory.ActionHandler?) -> UICellAccessory](./delete%28displayed,options,actionhandler%29.md)
  Creates a delete system accessory with the specified display state, configuration options, and optional action handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicellaccessory-swift.struct/deleteoptions)*