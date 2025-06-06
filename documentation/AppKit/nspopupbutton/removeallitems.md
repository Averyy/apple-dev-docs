# removeAllItems()

**Framework**: AppKit  
**Kind**: method

Removes all items in the receiver’s item menu.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func removeAllItems()
```

#### Discussion

After removing the items, this method uses the [`synchronizeTitleAndSelectedItem()`](nspopupbutton/synchronizetitleandselecteditem().md) method to refresh the menu.

## See Also

- [var numberOfItems: Int](nspopupbutton/numberofitems.md)
  The number of items in the menu.
- [func addItem(withTitle: String)](nspopupbutton/additem(withtitle:).md)
  Adds an item with the specified title to the end of the menu.
- [func addItems(withTitles: [String])](nspopupbutton/additems(withtitles:).md)
  Adds multiple items to the end of the menu.
- [func insertItem(withTitle: String, at: Int)](nspopupbutton/insertitem(withtitle:at:).md)
  Inserts an item at the specified position in the menu.
- [func removeItem(withTitle: String)](nspopupbutton/removeitem(withtitle:).md)
  Removes the item with the specified title from the menu.
- [func removeItem(at: Int)](nspopupbutton/removeitem(at:).md)
  Removes the item at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbutton/removeallitems())*