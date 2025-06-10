# UICellAccessory.MultiselectOptions

**Framework**: UIKit  
**Kind**: struct

Configuration options for a multiselect accessory.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
struct MultiselectOptions
```

## Topics

### Creating configuration options
- [init(isHidden: Bool?, reservedLayoutWidth: UICellAccessory.LayoutDimension?, tintColor: UIColor?, backgroundColor: UIColor?)](uicellaccessory-swift.struct/multiselectoptions/init(ishidden:reservedlayoutwidth:tintcolor:backgroundcolor:).md)
  Creates a multiselect accessory options structure.
### Accessing configuration options
- [var isHidden: Bool](uicellaccessory-swift.struct/multiselectoptions/ishidden.md)
  A Boolean value that determines whether the cell hides the accessory.
- [var reservedLayoutWidth: UICellAccessory.LayoutDimension](uicellaccessory-swift.struct/multiselectoptions/reservedlayoutwidth.md)
  The layout width that the system reserves for the accessory, and then centers the accessory within.
- [var tintColor: UIColor?](uicellaccessory-swift.struct/multiselectoptions/tintcolor.md)
  The tint color to apply to the accessory.
- [var backgroundColor: UIColor?](uicellaccessory-swift.struct/multiselectoptions/backgroundcolor.md)
  The background color to apply to the accessory.

## See Also

- [static func multiselect(displayed: UICellAccessory.DisplayedState, options: UICellAccessory.MultiselectOptions) -> UICellAccessory](uicellaccessory-swift.struct/multiselect(displayed:options:).md)
  Creates a multiselect system accessory with the specified display state and configuration options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicellaccessory-swift.struct/multiselectoptions)*