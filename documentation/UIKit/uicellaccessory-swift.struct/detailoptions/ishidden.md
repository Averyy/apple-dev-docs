# isHidden

**Framework**: UIKit  
**Kind**: property

A Boolean value that determines whether the cell hides the accessory.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst ?+
- tvOS 15.4+
- visionOS ?+

## Declaration

```swift
var isHidden: Bool
```

#### Discussion

A hidden accessory takes up space in the layout, but it isn’t visible and doesn’t provide any behaviors.

Use this property to achieve a consistent layout across cells when some cells show this type of accessory and others don’t.

## See Also

- [var reservedLayoutWidth: UICellAccessory.LayoutDimension](uicellaccessory-swift.struct/detailoptions/reservedlayoutwidth.md)
  The layout width that the system reserves for the accessory, and then centers the accessory within.
- [var tintColor: UIColor?](uicellaccessory-swift.struct/detailoptions/tintcolor.md)
  The tint color to apply to the accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicellaccessory-swift.struct/detailoptions/ishidden)*