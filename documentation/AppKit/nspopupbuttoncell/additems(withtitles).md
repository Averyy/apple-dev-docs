# addItems(withTitles:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Adds multiple items to the end of the menu.

**Availability**:
- macOS

## Declaration

```swift
func addItems(withTitles itemTitles: [String])
```

```objc
- (void) addItemsWithTitles:(NSArray<NSString *> *) itemTitles;
```

#### Discussion

The new menu items use the pop-up button’s default action and target, but you can change these using the setAction: and setTarget: methods of the corresponding [`NSMenuItem`](../nsmenuitem.md) object.

If you want to move an item, it’s better to invoke [`removeItem(withTitle:)`](./removeitem%28withtitle%29.md) explicitly and then call this method. After adding the items, this method uses the [`synchronizeTitleAndSelectedItem()`](./synchronizetitleandselecteditem%28%29.md) method to make sure the item being displayed matches the currently selected item.

Because this method searches for duplicate items, it should not be used if you are adding items to an already populated menu with more than a few hundred items. In a situation like this, add items directly to the receiver’s menu instead.

## Parameters

- `itemTitles`: An array of [`NSString`](../../Foundation/nsstring.md) objects containing the titles of the items you want to add. Each string in the array should be unique. If an item with the same title already exists in the menu, the existing item is removed and the new one is added.

## See Also

### Adding and removing items
- [func addItem(withTitle: String)](./additem%28withtitle%29.md)
  Adds an item with the specified title to the end of the menu.
- [func insertItem(withTitle: String, at: Int)](./insertitem%28withtitle,at%29.md)
  Inserts an item at the specified position in the menu.
- [func removeItem(withTitle: String)](./removeitem%28withtitle%29.md)
  Removes the item with the specified title from the menu.
- [func removeItem(at: Int)](./removeitem%28at%29.md)
  Removes the item at the specified index.
- [func removeAllItems()](./removeallitems%28%29.md)
  Removes all items in the receiver’s item menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/additems(withtitles:))*