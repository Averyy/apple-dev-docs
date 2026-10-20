# UICellAccessory.ReorderOptions

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

Configuration options for a reorder accessory.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS

## Declaration

```swift
struct ReorderOptions
```

## Topics

### Creating configuration options
- [init(isHidden: Bool?, reservedLayoutWidth: UICellAccessory.LayoutDimension?, tintColor: UIColor?, showsVerticalSeparator: Bool?)](./reorderoptions/init%28ishidden,reservedlayoutwidth,tintcolor,showsverticalseparator%29.md)
  Creates a reorder accessory options structure.
### Accessing configuration options
- [var isHidden: Bool](./reorderoptions/ishidden.md)
  A Boolean value that determines whether the cell hides the accessory.
- [var reservedLayoutWidth: UICellAccessory.LayoutDimension](./reorderoptions/reservedlayoutwidth.md)
  The layout width that the system reserves for the accessory, and then centers the accessory within.
- [var tintColor: UIColor?](./reorderoptions/tintcolor.md)
  The tint color to apply to the accessory.
- [var showsVerticalSeparator: Bool](./reorderoptions/showsverticalseparator.md)
  A Boolean value that determines whether a vertical separator displays before the accessory when it appears after another accessory.

## See Also

### Creating a reorder accessory
- [static func reorder(displayed: UICellAccessory.DisplayedState, options: UICellAccessory.ReorderOptions) -> UICellAccessory](./reorder%28displayed,options%29.md)
  Creates a reorder system accessory with the specified display state and configuration options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicellaccessory-swift.struct/reorderoptions)*