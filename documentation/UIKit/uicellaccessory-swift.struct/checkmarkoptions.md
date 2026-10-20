# UICellAccessory.CheckmarkOptions

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

Configuration options for a checkmark accessory.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS

## Declaration

```swift
struct CheckmarkOptions
```

## Topics

### Creating configuration options
- [init(isHidden: Bool?, reservedLayoutWidth: UICellAccessory.LayoutDimension?, tintColor: UIColor?)](./checkmarkoptions/init%28ishidden,reservedlayoutwidth,tintcolor%29.md)
  Creates a checkmark accessory options structure.
### Accessing configuration options
- [var isHidden: Bool](./checkmarkoptions/ishidden.md)
  A Boolean value that determines whether the cell hides the accessory.
- [var reservedLayoutWidth: UICellAccessory.LayoutDimension](./checkmarkoptions/reservedlayoutwidth.md)
  The layout width that the system reserves for the accessory, and then centers the accessory within.
- [var tintColor: UIColor?](./checkmarkoptions/tintcolor.md)
  The tint color to apply to the accessory.

## See Also

### Creating a checkmark accessory
- [static func checkmark(displayed: UICellAccessory.DisplayedState, options: UICellAccessory.CheckmarkOptions) -> UICellAccessory](./checkmark%28displayed,options%29.md)
  Creates a checkmark system accessory with the specified display state and configuration options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicellaccessory-swift.struct/checkmarkoptions)*