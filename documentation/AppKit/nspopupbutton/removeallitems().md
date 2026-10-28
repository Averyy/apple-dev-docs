# removeAllItems()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Removes all items in the receiver’s item menu.

**Availability**:
- macOS

## Declaration

```swift
func removeAllItems()
```

```objc
- (void) removeAllItems;
```

## Discussion

After removing the items, this method uses the [`synchronizeTitleAndSelectedItem()`](./synchronizetitleandselecteditem%28%29.md) method to refresh the menu.

## See Also

### Related Documentation
- [var numberOfItems: Int](./numberofitems.md)
  The number of items in the menu.
### Inserting and deleting items
- [func addItem(withTitle: String)](./additem%28withtitle%29.md)
  Adds an item with the specified title to the end of the menu.
- [func addItems(withTitles: [String])](./additems%28withtitles%29.md)
  Adds multiple items to the end of the menu.
- [func insertItem(withTitle: String, at: Int)](./insertitem%28withtitle,at%29.md)
  Inserts an item at the specified position in the menu.
- [func removeItem(withTitle: String)](./removeitem%28withtitle%29.md)
  Removes the item with the specified title from the menu.
- [func removeItem(at: Int)](./removeitem%28at%29.md)
  Removes the item at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbutton/removeallitems())*