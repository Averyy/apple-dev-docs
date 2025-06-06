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

## Parameters

- `index`: The zero-based index indicating which item to remove. Specifying   removes the item at the top of the menu. The index must be valid and non-negative.

## See Also

- [func addItem(withTitle: String)](nspopupbuttoncell/additem(withtitle:).md)
  Adds an item with the specified title to the end of the menu.
- [func addItems(withTitles: [String])](nspopupbuttoncell/additems(withtitles:).md)
  Adds multiple items to the end of the menu.
- [func insertItem(withTitle: String, at: Int)](nspopupbuttoncell/insertitem(withtitle:at:).md)
  Inserts an item at the specified position in the menu.
- [func removeItem(withTitle: String)](nspopupbuttoncell/removeitem(withtitle:).md)
  Removes the item with the specified title from the menu.
- [func removeAllItems()](nspopupbuttoncell/removeallitems.md)
  Removes all items in the receiver’s item menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/removeitem(at:))*