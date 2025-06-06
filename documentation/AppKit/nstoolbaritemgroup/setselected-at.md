# setSelected(_:at:)

**Framework**: AppKit  
**Kind**: method

Sets the selected state of a subitem in a grouped toolbar item.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+

## Declaration

```swift
@MainActor
func setSelected(_ selected: Bool, at index: Int)
```

## Parameters

- `selected`: If  , indicates whether to select a subitem,   otherwise.
- `index`: The index location of the subitem.

## See Also

- [var subitems: [NSToolbarItem]](nstoolbaritemgroup/subitems.md)
  The subitems of the grouped toolbar item.
- [var selectedIndex: Int](nstoolbaritemgroup/selectedindex.md)
  The index value for the most recently selected subitem of a grouped toolbar item.
- [func isSelected(at: Int) -> Bool](nstoolbaritemgroup/isselected(at:).md)
  Indicates whether a specified index is currently selected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbaritemgroup/setselected(_:at:))*