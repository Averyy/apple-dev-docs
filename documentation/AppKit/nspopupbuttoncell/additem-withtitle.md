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

The menu item uses the pop-up button’s default action and target, but you can change these using the setAction: and setTarget: methods of the corresponding [`NSMenuItem`](nsmenuitem.md) object.

Because this method searches for duplicate items, it should not be used if you are adding an item to an already populated menu with more than a few hundred items. In a situation like this, add items directly to the button’s menu instead.

## Parameters

- `title`: The title of the new menu item. If an item with the same title already exists in the menu, the existing item is removed and the new one is added.

## See Also

- [func addItems(withTitles: [String])](nspopupbuttoncell/additems(withtitles:).md)
  Adds multiple items to the end of the menu.
- [func insertItem(withTitle: String, at: Int)](nspopupbuttoncell/insertitem(withtitle:at:).md)
  Inserts an item at the specified position in the menu.
- [func removeItem(withTitle: String)](nspopupbuttoncell/removeitem(withtitle:).md)
  Removes the item with the specified title from the menu.
- [func removeItem(at: Int)](nspopupbuttoncell/removeitem(at:).md)
  Removes the item at the specified index.
- [func removeAllItems()](nspopupbuttoncell/removeallitems.md)
  Removes all items in the receiver’s item menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/additem(withtitle:))*