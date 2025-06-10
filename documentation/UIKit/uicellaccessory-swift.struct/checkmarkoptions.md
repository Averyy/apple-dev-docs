# UICellAccessory.CheckmarkOptions

**Framework**: UIKit  
**Kind**: struct

Configuration options for a checkmark accessory.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
struct CheckmarkOptions
```

## Topics

### Creating configuration options
- [init(isHidden: Bool?, reservedLayoutWidth: UICellAccessory.LayoutDimension?, tintColor: UIColor?)](uicellaccessory-swift.struct/checkmarkoptions/init(ishidden:reservedlayoutwidth:tintcolor:).md)
  Creates a checkmark accessory options structure.
### Accessing configuration options
- [var isHidden: Bool](uicellaccessory-swift.struct/checkmarkoptions/ishidden.md)
  A Boolean value that determines whether the cell hides the accessory.
- [var reservedLayoutWidth: UICellAccessory.LayoutDimension](uicellaccessory-swift.struct/checkmarkoptions/reservedlayoutwidth.md)
  The layout width that the system reserves for the accessory, and then centers the accessory within.
- [var tintColor: UIColor?](uicellaccessory-swift.struct/checkmarkoptions/tintcolor.md)
  The tint color to apply to the accessory.

## See Also

- [static func checkmark(displayed: UICellAccessory.DisplayedState, options: UICellAccessory.CheckmarkOptions) -> UICellAccessory](uicellaccessory-swift.struct/checkmark(displayed:options:).md)
  Creates a checkmark system accessory with the specified display state and configuration options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicellaccessory-swift.struct/checkmarkoptions)*