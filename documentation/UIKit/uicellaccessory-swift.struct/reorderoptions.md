# UICellAccessory.ReorderOptions

**Framework**: UIKit  
**Kind**: struct

Configuration options for a reorder accessory.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
struct ReorderOptions
```

## Topics

### Creating configuration options
- [init(isHidden: Bool?, reservedLayoutWidth: UICellAccessory.LayoutDimension?, tintColor: UIColor?, showsVerticalSeparator: Bool?)](uicellaccessory-swift.struct/reorderoptions/init(ishidden:reservedlayoutwidth:tintcolor:showsverticalseparator:).md)
  Creates a reorder accessory options structure.
### Accessing configuration options
- [var isHidden: Bool](uicellaccessory-swift.struct/reorderoptions/ishidden.md)
  A Boolean value that determines whether the cell hides the accessory.
- [var reservedLayoutWidth: UICellAccessory.LayoutDimension](uicellaccessory-swift.struct/reorderoptions/reservedlayoutwidth.md)
  The layout width that the system reserves for the accessory, and then centers the accessory within.
- [var tintColor: UIColor?](uicellaccessory-swift.struct/reorderoptions/tintcolor.md)
  The tint color to apply to the accessory.
- [var showsVerticalSeparator: Bool](uicellaccessory-swift.struct/reorderoptions/showsverticalseparator.md)
  A Boolean value that determines whether a vertical separator displays before the accessory when it appears after another accessory.

## See Also

- [static func reorder(displayed: UICellAccessory.DisplayedState, options: UICellAccessory.ReorderOptions) -> UICellAccessory](uicellaccessory-swift.struct/reorder(displayed:options:).md)
  Creates a reorder system accessory with the specified display state and configuration options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicellaccessory-swift.struct/reorderoptions)*