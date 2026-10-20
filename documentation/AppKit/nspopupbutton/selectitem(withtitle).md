# selectItem(withTitle:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Selects the item with the specified title.

**Availability**:
- macOS

## Declaration

```swift
func selectItem(withTitle title: String)
```

```objc
- (void) selectItemWithTitle:(NSString *) title;
```

## Parameters

- `title`: The title of the item to select. If you specify an empty string, or a string that does not match the title of a menu item, this method deselects the currently selected item.

## See Also

### Related Documentation
- [func indexOfItem(withTitle: String) -> Int](./indexofitem%28withtitle%29.md)
  Returns the index of the item with the specified title.
- [func addItem(withTitle: String)](./additem%28withtitle%29.md)
  Adds an item with the specified title to the end of the menu.
- [func setTitle(String)](./settitle%28_%29.md)
  Sets the string displayed in the receiver when the user isn’t pressing the mouse button.
### Setting the current selection
- [func select(NSMenuItem?)](./select%28_%29.md)
  Selects the specified menu item.
- [func selectItem(at: Int)](./selectitem%28at%29.md)
  Selects the item in the menu at the specified index.
- [func selectItem(withTag: Int) -> Bool](./selectitem%28withtag%29.md)
  Selects the menu item with the specified tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbutton/selectitem(withtitle:))*