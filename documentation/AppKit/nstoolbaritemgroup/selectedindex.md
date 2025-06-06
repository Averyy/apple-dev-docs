# selectedIndex

**Framework**: AppKit  
**Kind**: property

The index value for the most recently selected subitem of a grouped toolbar item.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+

## Declaration

```swift
@MainActor
var selectedIndex: Int { get set }
```

#### Discussion

When using the [`NSToolbarItemGroup.SelectionMode.selectAny`](nstoolbaritemgroup/selectionmode-swift.enum/selectany.md) or [`NSToolbarItemGroup.SelectionMode.momentary`](nstoolbaritemgroup/selectionmode-swift.enum/momentary.md) selection mode, don’t assume that this value represents the selected subitem. This method returns the index of the most recently selected subitem.

To determine if a specific subitem of a grouped toolbar item is selected, use the [`isSelected(at:)`](nstoolbaritemgroup/isselected(at:).md) method.

## See Also

- [var subitems: [NSToolbarItem]](nstoolbaritemgroup/subitems.md)
  The subitems of the grouped toolbar item.
- [func isSelected(at: Int) -> Bool](nstoolbaritemgroup/isselected(at:).md)
  Indicates whether a specified index is currently selected.
- [func setSelected(Bool, at: Int)](nstoolbaritemgroup/setselected(_:at:).md)
  Sets the selected state of a subitem in a grouped toolbar item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbaritemgroup/selectedindex)*