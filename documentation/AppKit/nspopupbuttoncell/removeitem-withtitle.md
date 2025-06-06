# removeItem(withTitle:)

**Framework**: AppKit  
**Kind**: method

Removes the item with the specified title from the menu.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func removeItem(withTitle title: String)
```

## Parameters

- `title`: The title of the item you want to remove. If no menu item exists with the specified title, this method triggers an assertion.

## See Also

- [func addItem(withTitle: String)](nspopupbuttoncell/additem(withtitle:).md)
  Adds an item with the specified title to the end of the menu.
- [func addItems(withTitles: [String])](nspopupbuttoncell/additems(withtitles:).md)
  Adds multiple items to the end of the menu.
- [func insertItem(withTitle: String, at: Int)](nspopupbuttoncell/insertitem(withtitle:at:).md)
  Inserts an item at the specified position in the menu.
- [func removeItem(at: Int)](nspopupbuttoncell/removeitem(at:).md)
  Removes the item at the specified index.
- [func removeAllItems()](nspopupbuttoncell/removeallitems.md)
  Removes all items in the receiver’s item menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/removeitem(withtitle:))*