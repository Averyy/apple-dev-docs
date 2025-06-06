# addItems(withTitles:)

**Framework**: AppKit  
**Kind**: method

Adds multiple items to the end of the menu.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func addItems(withTitles itemTitles: [String])
```

#### Discussion

The new menu items use the pop-up button’s default action and target, but you can change these using the setAction: and setTarget: methods of the corresponding [`NSMenuItem`](nsmenuitem.md) object.

If you want to move an item, it’s better to invoke [`removeItem(withTitle:)`](nspopupbuttoncell/removeitem(withtitle:).md) explicitly and then call this method. After adding the items, this method uses the [`synchronizeTitleAndSelectedItem()`](nspopupbuttoncell/synchronizetitleandselecteditem().md) method to make sure the item being displayed matches the currently selected item.

Because this method searches for duplicate items, it should not be used if you are adding items to an already populated menu with more than a few hundred items. In a situation like this, add items directly to the receiver’s menu instead.

## Parameters

- `itemTitles`: An array of   objects containing the titles of the items you want to add. Each string in the array should be unique. If an item with the same title already exists in the menu, the existing item is removed and the new one is added.

## See Also

- [func addItem(withTitle: String)](nspopupbuttoncell/additem(withtitle:).md)
  Adds an item with the specified title to the end of the menu.
- [func insertItem(withTitle: String, at: Int)](nspopupbuttoncell/insertitem(withtitle:at:).md)
  Inserts an item at the specified position in the menu.
- [func removeItem(withTitle: String)](nspopupbuttoncell/removeitem(withtitle:).md)
  Removes the item with the specified title from the menu.
- [func removeItem(at: Int)](nspopupbuttoncell/removeitem(at:).md)
  Removes the item at the specified index.
- [func removeAllItems()](nspopupbuttoncell/removeallitems.md)
  Removes all items in the receiver’s item menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/additems(withtitles:))*