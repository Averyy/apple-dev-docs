# UICellAccessory.DisclosureIndicatorOptions

**Framework**: UIKit  
**Kind**: struct

Configuration options for a disclosure indicator.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
struct DisclosureIndicatorOptions
```

## Topics

### Creating configuration options
- [init(isHidden: Bool?, reservedLayoutWidth: UICellAccessory.LayoutDimension?, tintColor: UIColor?)](uicellaccessory-swift.struct/disclosureindicatoroptions/init(ishidden:reservedlayoutwidth:tintcolor:).md)
  Creates a disclosure indicator options structure.
### Accessing configuration options
- [var isHidden: Bool](uicellaccessory-swift.struct/disclosureindicatoroptions/ishidden.md)
  A Boolean value that determines whether the cell hides the accessory.
- [var reservedLayoutWidth: UICellAccessory.LayoutDimension](uicellaccessory-swift.struct/disclosureindicatoroptions/reservedlayoutwidth.md)
  The layout width that the system reserves for the accessory, and then centers the accessory within.
- [var tintColor: UIColor?](uicellaccessory-swift.struct/disclosureindicatoroptions/tintcolor.md)
  The tint color to apply to the accessory.

## See Also

- [static func disclosureIndicator(displayed: UICellAccessory.DisplayedState, options: UICellAccessory.DisclosureIndicatorOptions) -> UICellAccessory](uicellaccessory-swift.struct/disclosureindicator(displayed:options:).md)
  Creates a disclosure indicator system accessory with the specified display state and configuration options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicellaccessory-swift.struct/disclosureindicatoroptions)*