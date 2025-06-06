# removeItem(at:)

**Framework**: AppKit  
**Kind**: method

Removes the item at the specified index.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func removeItem(at index: Int)
```

#### Discussion

After removing the item, this method uses the [`synchronizeTitleAndSelectedItem()`](nspopupbutton/synchronizetitleandselecteditem().md) method to make sure the title displayed matches the currently selected item.

## Parameters

- `index`: The zero-based index indicating which item to remove. Specifying 0 removes the item at the top of the menu.

## See Also

- [func addItem(withTitle: String)](nspopupbutton/additem(withtitle:).md)
  Adds an item with the specified title to the end of the menu.
- [func addItems(withTitles: [String])](nspopupbutton/additems(withtitles:).md)
  Adds multiple items to the end of the menu.
- [func insertItem(withTitle: String, at: Int)](nspopupbutton/insertitem(withtitle:at:).md)
  Inserts an item at the specified position in the menu.
- [func removeAllItems()](nspopupbutton/removeallitems.md)
  Removes all items in the receiver’s item menu.
- [func removeItem(withTitle: String)](nspopupbutton/removeitem(withtitle:).md)
  Removes the item with the specified title from the menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbutton/removeitem(at:))*