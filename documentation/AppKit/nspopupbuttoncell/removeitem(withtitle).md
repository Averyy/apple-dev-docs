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

## Parameters

- `title`: The title of the item you want to remove. If no menu item exists with the specified title, this method triggers an assertion.

## See Also

### Adding and removing items
- [func addItem(withTitle: String)](./additem%28withtitle%29.md)
  Adds an item with the specified title to the end of the menu.
- [func addItems(withTitles: [String])](./additems%28withtitles%29.md)
  Adds multiple items to the end of the menu.
- [func insertItem(withTitle: String, at: Int)](./insertitem%28withtitle,at%29.md)
  Inserts an item at the specified position in the menu.
- [func removeItem(at: Int)](./removeitem%28at%29.md)
  Removes the item at the specified index.
- [func removeAllItems()](./removeallitems%28%29.md)
  Removes all items in the receiver’s item menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/removeitem(withtitle:))*