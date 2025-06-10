# isHidden

**Framework**: UIKit  
**Kind**: property

A Boolean value that determines whether the cell hides the accessory.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
var isHidden: Bool
```

#### Discussion

A hidden accessory takes up space in the layout, but it isn’t visible and doesn’t provide any behaviors.

Use this property to achieve a consistent layout across cells when some cells show this type of accessory and others don’t.

## See Also

- [var reservedLayoutWidth: UICellAccessory.LayoutDimension](uicellaccessory-swift.struct/popupmenuoptions/reservedlayoutwidth.md)
  The layout width that the system reserves for the accessory, and then centers the accessory within.
- [var tintColor: UIColor?](uicellaccessory-swift.struct/popupmenuoptions/tintcolor.md)
  The tint color to apply to the accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicellaccessory-swift.struct/popupmenuoptions/ishidden)*