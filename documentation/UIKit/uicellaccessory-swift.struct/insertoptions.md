# UICellAccessory.InsertOptions

**Framework**: UIKit  
**Kind**: struct

Configuration options for an insert accessory.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
struct InsertOptions
```

## Topics

### Creating configuration options
- [init(isHidden: Bool?, reservedLayoutWidth: UICellAccessory.LayoutDimension?, tintColor: UIColor?, backgroundColor: UIColor?)](uicellaccessory-swift.struct/insertoptions/init(ishidden:reservedlayoutwidth:tintcolor:backgroundcolor:).md)
  Creates an insert accessory options structure.
### Accessing configuration options
- [var isHidden: Bool](uicellaccessory-swift.struct/insertoptions/ishidden.md)
  A Boolean value that determines whether the cell hides the accessory.
- [var reservedLayoutWidth: UICellAccessory.LayoutDimension](uicellaccessory-swift.struct/insertoptions/reservedlayoutwidth.md)
  The layout width that the system reserves for the accessory, and then centers the accessory within.
- [var tintColor: UIColor?](uicellaccessory-swift.struct/insertoptions/tintcolor.md)
  The tint color to apply to the accessory.
- [var backgroundColor: UIColor?](uicellaccessory-swift.struct/insertoptions/backgroundcolor.md)
  The background color to apply to the accessory.

## See Also

- [static func insert(displayed: UICellAccessory.DisplayedState, options: UICellAccessory.InsertOptions, actionHandler: UICellAccessory.ActionHandler?) -> UICellAccessory](uicellaccessory-swift.struct/insert(displayed:options:actionhandler:).md)
  Creates an insert system accessory with the specified display state, configuration options, and optional action handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicellaccessory-swift.struct/insertoptions)*