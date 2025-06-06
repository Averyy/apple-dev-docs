# selectItem(withTitle:)

**Framework**: AppKit  
**Kind**: method

Selects the item with the specified title.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func selectItem(withTitle title: String)
```

## Parameters

- `title`: The title of the item to select. If you specify an empty string, or a string that does not match the title of a menu item, this method deselects the currently selected item.

## See Also

- [func indexOfItem(withTitle: String) -> Int](nspopupbutton/indexofitem(withtitle:).md)
  Returns the index of the item with the specified title.
- [func addItem(withTitle: String)](nspopupbutton/additem(withtitle:).md)
  Adds an item with the specified title to the end of the menu.
- [func setTitle(String)](nspopupbutton/settitle(_:).md)
  Sets the string displayed in the receiver when the user isn’t pressing the mouse button.
- [func select(NSMenuItem?)](nspopupbutton/select(_:).md)
  Selects the specified menu item.
- [func selectItem(at: Int)](nspopupbutton/selectitem(at:).md)
  Selects the item in the menu at the specified index.
- [func selectItem(withTag: Int) -> Bool](nspopupbutton/selectitem(withtag:).md)
  Selects the menu item with the specified tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbutton/selectitem(withtitle:))*