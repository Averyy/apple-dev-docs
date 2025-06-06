# isSelected(at:)

**Framework**: AppKit  
**Kind**: method

Indicates whether a specified index is currently selected.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+

## Declaration

```swift
@MainActor
func isSelected(at index: Int) -> Bool
```

#### Return Value

A Boolean value indicating whether the specified index is currently selected.

#### Discussion

Use this method when you specify the [`NSToolbarItemGroup.SelectionMode.selectAny`](nstoolbaritemgroup/selectionmode-swift.enum/selectany.md) selection mode for the grouped toolbar item to determine which subitems are currently selected.

## Parameters

- `index`: The index of the subitems in a grouped toolbar item.

## See Also

- [var subitems: [NSToolbarItem]](nstoolbaritemgroup/subitems.md)
  The subitems of the grouped toolbar item.
- [var selectedIndex: Int](nstoolbaritemgroup/selectedindex.md)
  The index value for the most recently selected subitem of a grouped toolbar item.
- [func setSelected(Bool, at: Int)](nstoolbaritemgroup/setselected(_:at:).md)
  Sets the selected state of a subitem in a grouped toolbar item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbaritemgroup/isselected(at:))*