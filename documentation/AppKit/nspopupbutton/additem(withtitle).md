# addItem(withTitle:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Adds an item with the specified title to the end of the menu.

**Availability**:
- macOS

## Declaration

```swift
func addItem(withTitle title: String)
```

```objc
- (void) addItemWithTitle:(NSString *) title;
```

#### Discussion

If you want to move an item, it’s better to invoke [`removeItem(withTitle:)`](./removeitem%28withtitle%29.md) explicitly and then send this method. After adding the item, this method calls the [`synchronizeTitleAndSelectedItem()`](./synchronizetitleandselecteditem%28%29.md) method to make sure the item being displayed matches the currently selected item.

Since this method searches for duplicate items, it should not be used if you are adding an item to an already populated menu with more than a few hundred items. Add items directly to the receiver’s menu instead.

## Parameters

- `title`: The title of the menu-item entry. If an item with the same title already exists in the menu, the existing item is removed and the new one is added.

## See Also

### Related Documentation
- [func setTitle(String)](./settitle%28_%29.md)
  Sets the string displayed in the receiver when the user isn’t pressing the mouse button.
### Inserting and deleting items
- [func addItems(withTitles: [String])](./additems%28withtitles%29.md)
  Adds multiple items to the end of the menu.
- [func insertItem(withTitle: String, at: Int)](./insertitem%28withtitle,at%29.md)
  Inserts an item at the specified position in the menu.
- [func removeAllItems()](./removeallitems%28%29.md)
  Removes all items in the receiver’s item menu.
- [func removeItem(withTitle: String)](./removeitem%28withtitle%29.md)
  Removes the item with the specified title from the menu.
- [func removeItem(at: Int)](./removeitem%28at%29.md)
  Removes the item at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbutton/additem(withtitle:))*