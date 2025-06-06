# addItem(withTitle:)

**Framework**: AppKit  
**Kind**: method

Adds an item with the specified title to the end of the menu.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func addItem(withTitle title: String)
```

#### Discussion

If you want to move an item, it’s better to invoke [`removeItem(withTitle:)`](nspopupbutton/removeitem(withtitle:).md) explicitly and then send this method. After adding the item, this method calls the [`synchronizeTitleAndSelectedItem()`](nspopupbutton/synchronizetitleandselecteditem().md) method to make sure the item being displayed matches the currently selected item.

Since this method searches for duplicate items, it should not be used if you are adding an item to an already populated menu with more than a few hundred items. Add items directly to the receiver’s menu instead.

## Parameters

- `title`: The title of the menu-item entry. If an item with the same title already exists in the menu, the existing item is removed and the new one is added.

## See Also

- [func setTitle(String)](nspopupbutton/settitle(_:).md)
  Sets the string displayed in the receiver when the user isn’t pressing the mouse button.
- [func addItems(withTitles: [String])](nspopupbutton/additems(withtitles:).md)
  Adds multiple items to the end of the menu.
- [func insertItem(withTitle: String, at: Int)](nspopupbutton/insertitem(withtitle:at:).md)
  Inserts an item at the specified position in the menu.
- [func removeAllItems()](nspopupbutton/removeallitems.md)
  Removes all items in the receiver’s item menu.
- [func removeItem(withTitle: String)](nspopupbutton/removeitem(withtitle:).md)
  Removes the item with the specified title from the menu.
- [func removeItem(at: Int)](nspopupbutton/removeitem(at:).md)
  Removes the item at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbutton/additem(withtitle:))*