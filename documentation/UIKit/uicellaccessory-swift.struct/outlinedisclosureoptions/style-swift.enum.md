# UICellAccessory.OutlineDisclosureOptions.Style

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Constants that describe the style of the outline disclosure accessory.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS

## Declaration

```swift
enum Style
```

## Topics

### Constants
- [UICellAccessory.OutlineDisclosureOptions.Style.automatic](./style-swift.enum/automatic.md)
  The system automatically determines the style depending on whether the cell’s configuration is as a section header.
- [UICellAccessory.OutlineDisclosureOptions.Style.cell](./style-swift.enum/cell.md)
  The style to use for a selectable cell with nested children.
- [UICellAccessory.OutlineDisclosureOptions.Style.header](./style-swift.enum/header.md)
  The style to use for a section header.

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)

## See Also

### Accessing configuration options
- [var isHidden: Bool](./ishidden.md)
  A Boolean value that determines whether the cell hides the accessory.
- [var reservedLayoutWidth: UICellAccessory.LayoutDimension](./reservedlayoutwidth.md)
  The layout width that the system reserves for the accessory, and then centers the accessory within.
- [var tintColor: UIColor?](./tintcolor.md)
  The tint color to apply to the accessory.
- [var style: UICellAccessory.OutlineDisclosureOptions.Style](./style-swift.property.md)
  The style of the outline disclosure accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicellaccessory-swift.struct/outlinedisclosureoptions/style-swift.enum)*