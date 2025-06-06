# subitems

**Framework**: AppKit  
**Kind**: property

The subitems of the grouped toolbar item.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.5+

## Declaration

```swift
@MainActor
var subitems: [NSToolbarItem] { get set }
```

#### Discussion

By default, an [`NSToolbarItemGroup`](nstoolbaritemgroup.md) instance has an empty array of subitems.

## See Also

- [Toolbar Programming Topics for Cocoa](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Toolbars/Toolbars.html#//apple_ref/doc/uid/10000109i)
- [var selectedIndex: Int](nstoolbaritemgroup/selectedindex.md)
  The index value for the most recently selected subitem of a grouped toolbar item.
- [func isSelected(at: Int) -> Bool](nstoolbaritemgroup/isselected(at:).md)
  Indicates whether a specified index is currently selected.
- [func setSelected(Bool, at: Int)](nstoolbaritemgroup/setselected(_:at:).md)
  Sets the selected state of a subitem in a grouped toolbar item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbaritemgroup/subitems)*