# selectItem(at:)

**Framework**: AppKit  
**Kind**: method

Selects the item in the menu at the specified index.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func selectItem(at index: Int)
```

## Parameters

- `index`: The index of the item you want to select, or   you want to deselect all menu items.

## See Also

- [var indexOfSelectedItem: Int](nspopupbutton/indexofselecteditem.md)
  The index of the item that was last selected by the user.
- [func select(NSMenuItem?)](nspopupbutton/select(_:).md)
  Selects the specified menu item.
- [func selectItem(withTag: Int) -> Bool](nspopupbutton/selectitem(withtag:).md)
  Selects the menu item with the specified tag.
- [func selectItem(withTitle: String)](nspopupbutton/selectitem(withtitle:).md)
  Selects the item with the specified title.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbutton/selectitem(at:))*