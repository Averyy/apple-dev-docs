# UICellAccessory.DetailOptions

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

Configuration options for a detail accessory.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- tvOS 15.4+
- visionOS

## Declaration

```swift
struct DetailOptions
```

## Topics

### Creating configuration options
- [init(isHidden: Bool?, reservedLayoutWidth: UICellAccessory.LayoutDimension?, tintColor: UIColor?)](./detailoptions/init%28ishidden,reservedlayoutwidth,tintcolor%29.md)
  Creates a detail accessory options structure.
### Accessing configuration options
- [var isHidden: Bool](./detailoptions/ishidden.md)
  A Boolean value that determines whether the cell hides the accessory.
- [var reservedLayoutWidth: UICellAccessory.LayoutDimension](./detailoptions/reservedlayoutwidth.md)
  The layout width that the system reserves for the accessory, and then centers the accessory within.
- [var tintColor: UIColor?](./detailoptions/tintcolor.md)
  The tint color to apply to the accessory.

## See Also

### Creating a detail accessory
- [static func detail(displayed: UICellAccessory.DisplayedState, options: UICellAccessory.DetailOptions, actionHandler: UICellAccessory.ActionHandler?) -> UICellAccessory](./detail%28displayed,options,actionhandler%29.md)
  Creates a detail system accessory with the specified display state, configuration options, and optional action handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicellaccessory-swift.struct/detailoptions)*