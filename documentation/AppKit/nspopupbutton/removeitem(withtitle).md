# removeItem(withTitle:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Removes the item with the specified title from the menu.

**Availability**:
- macOS

## Declaration

```swift
func removeItem(withTitle title: String)
```

```objc
- (void) removeItemWithTitle:(NSString *) title;
```

## Discussion

This method removes the first item it finds with the specified name. This method then uses [`synchronizeTitleAndSelectedItem()`](./synchronizetitleandselecteditem%28%29.md) to refresh the menu.

## Parameters

- `title`: The title of the item you want to remove. If no menu item exists with the specified title, this method triggers an assertion.

## See Also

### Inserting and deleting items
- [func addItem(withTitle: String)](./additem%28withtitle%29.md)
  Adds an item with the specified title to the end of the menu.
- [func addItems(withTitles: [String])](./additems%28withtitles%29.md)
  Adds multiple items to the end of the menu.
- [func insertItem(withTitle: String, at: Int)](./insertitem%28withtitle,at%29.md)
  Inserts an item at the specified position in the menu.
- [func removeAllItems()](./removeallitems%28%29.md)
  Removes all items in the receiver’s item menu.
- [func removeItem(at: Int)](./removeitem%28at%29.md)
  Removes the item at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbutton/removeitem(withtitle:))*