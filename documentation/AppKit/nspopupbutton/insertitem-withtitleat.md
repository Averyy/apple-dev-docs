# insertItem(withTitle:at:)

**Framework**: AppKit  
**Kind**: method

Inserts an item at the specified position in the menu.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func insertItem(withTitle title: String, at index: Int)
```

#### Discussion

If you want to move an item, it’s better to invoke [`removeItem(withTitle:)`](nspopupbutton/removeitem(withtitle:).md) explicitly and then send this method. After adding the item, this method uses the [`synchronizeTitleAndSelectedItem()`](nspopupbutton/synchronizetitleandselecteditem().md) method to make sure the item displayed matches the currently selected item.

Since this method searches for duplicate items, it should not be used if you are adding an item to an already populated menu with more than a few hundred items. Add items directly to the receiver’s menu instead.

## Parameters

- `title`: The title of the new item. If an item with the same title already exists in the menu, the existing item is removed and the new one is added
- `index`: The zero-based index at which to insert the item. Specifying 0 inserts the item at the top of the menu.

## See Also

- [func indexOfItem(withTitle: String) -> Int](nspopupbutton/indexofitem(withtitle:).md)
  Returns the index of the item with the specified title.
- [func addItem(withTitle: String)](nspopupbutton/additem(withtitle:).md)
  Adds an item with the specified title to the end of the menu.
- [func addItems(withTitles: [String])](nspopupbutton/additems(withtitles:).md)
  Adds multiple items to the end of the menu.
- [func removeAllItems()](nspopupbutton/removeallitems.md)
  Removes all items in the receiver’s item menu.
- [func removeItem(withTitle: String)](nspopupbutton/removeitem(withtitle:).md)
  Removes the item with the specified title from the menu.
- [func removeItem(at: Int)](nspopupbutton/removeitem(at:).md)
  Removes the item at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbutton/insertitem(withtitle:at:))*