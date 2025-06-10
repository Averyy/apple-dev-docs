# UICellAccessory.DetailOptions

**Framework**: UIKit  
**Kind**: struct

Configuration options for a detail accessory.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst ?+
- tvOS 15.4+
- visionOS ?+

## Declaration

```swift
struct DetailOptions
```

## Topics

### Creating configuration options
- [init(isHidden: Bool?, reservedLayoutWidth: UICellAccessory.LayoutDimension?, tintColor: UIColor?)](uicellaccessory-swift.struct/detailoptions/init(ishidden:reservedlayoutwidth:tintcolor:).md)
  Creates a detail accessory options structure.
### Accessing configuration options
- [var isHidden: Bool](uicellaccessory-swift.struct/detailoptions/ishidden.md)
  A Boolean value that determines whether the cell hides the accessory.
- [var reservedLayoutWidth: UICellAccessory.LayoutDimension](uicellaccessory-swift.struct/detailoptions/reservedlayoutwidth.md)
  The layout width that the system reserves for the accessory, and then centers the accessory within.
- [var tintColor: UIColor?](uicellaccessory-swift.struct/detailoptions/tintcolor.md)
  The tint color to apply to the accessory.

## See Also

- [static func detail(displayed: UICellAccessory.DisplayedState, options: UICellAccessory.DetailOptions, actionHandler: UICellAccessory.ActionHandler?) -> UICellAccessory](uicellaccessory-swift.struct/detail(displayed:options:actionhandler:).md)
  Creates a detail system accessory with the specified display state, configuration options, and optional action handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicellaccessory-swift.struct/detailoptions)*