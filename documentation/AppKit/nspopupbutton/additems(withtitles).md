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

If you want to move an item, it’s better to invoke [`removeItem(withTitle:)`](./removeitem%28withtitle%29.md) explicitly and then send this method. After adding the items, this method uses the [`synchronizeTitleAndSelectedItem()`](./synchronizetitleandselecteditem%28%29.md) method to make sure the item being displayed matches the currently selected item.

Since this method searches for duplicate items, it should not be used if you are adding items to an already populated menu with more than a few hundred items. Add items directly to the receiver’s menu instead.

## Parameters

- `itemTitles`: An array of `NSString` objects containing the titles of the items you want to add. Each string in the array should be unique. If an item with the same title already exists in the menu, the existing item is removed and the new one is added.

## See Also

### Inserting and deleting items
- [func addItem(withTitle: String)](./additem%28withtitle%29.md)
  Adds an item with the specified title to the end of the menu.
- [func insertItem(withTitle: String, at: Int)](./insertitem%28withtitle,at%29.md)
  Inserts an item at the specified position in the menu.
- [func removeAllItems()](./removeallitems%28%29.md)
  Removes all items in the receiver’s item menu.
- [func removeItem(withTitle: String)](./removeitem%28withtitle%29.md)
  Removes the item with the specified title from the menu.
- [func removeItem(at: Int)](./removeitem%28at%29.md)
  Removes the item at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbutton/additems(withtitles:))*