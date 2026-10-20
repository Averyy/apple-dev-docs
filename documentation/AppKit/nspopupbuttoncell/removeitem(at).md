# removeItem(at:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Removes the item at the specified index.

**Availability**:
- macOS

## Declaration

```swift
func removeItem(at index: Int)
```

```objc
- (void) removeItemAtIndex:(NSInteger) index;
```

## Parameters

- `index`: The zero-based index indicating which item to remove. Specifying `0` removes the item at the top of the menu. The index must be valid and non-negative.

## See Also

### Adding and removing items
- [func addItem(withTitle: String)](./additem%28withtitle%29.md)
  Adds an item with the specified title to the end of the menu.
- [func addItems(withTitles: [String])](./additems%28withtitles%29.md)
  Adds multiple items to the end of the menu.
- [func insertItem(withTitle: String, at: Int)](./insertitem%28withtitle,at%29.md)
  Inserts an item at the specified position in the menu.
- [func removeItem(withTitle: String)](./removeitem%28withtitle%29.md)
  Removes the item with the specified title from the menu.
- [func removeAllItems()](./removeallitems%28%29.md)
  Removes all items in the receiver’s item menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/removeitem(at:))*