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

#### Discussion

By default, selecting or deselecting a menu item changes its state. To disassociate the current selection from the state of menu items, set the [`altersStateOfSelectedItem`](./altersstateofselecteditem.md) property to [`false`](../../Swift/false.md).

## Parameters

- `title`: The title of the item to select. If you specify an empty string, or a string that does not match the title of a menu item, this method deselects the currently selected item.

## See Also

### Related Documentation
- [var altersStateOfSelectedItem: Bool](./altersstateofselecteditem.md)
  A Boolean value that indicates if the pop-up button links the state of the selected menu item to the current selection.
### Dealing with selection
- [func select(NSMenuItem?)](./select%28_%29.md)
  Selects the specified menu item.
- [func selectItem(at: Int)](./selectitem%28at%29.md)
  Selects the item in the menu at the specified index.
- [func selectItem(withTag: Int) -> Bool](./selectitem%28withtag%29.md)
  Selects the menu item with the specified tag.
- [func setTitle(String?)](./settitle%28_%29.md)
  Sets the string displayed in the receiver when the user isn’t pressing the mouse button.
- [var selectedItem: NSMenuItem?](./selecteditem.md)
  The menu item last selected by the user.
- [var indexOfSelectedItem: Int](./indexofselecteditem.md)
  The index of the item last selected by the user.
- [func synchronizeTitleAndSelectedItem()](./synchronizetitleandselecteditem%28%29.md)
  Synchronizes the pop-up button’s displayed item with the currently selected menu item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/selectitem(withtitle:))*