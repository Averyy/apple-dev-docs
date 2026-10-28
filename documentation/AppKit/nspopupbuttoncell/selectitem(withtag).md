# selectItem(withTag:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Selects the menu item with the specified tag.

**Availability**:
- macOS

## Declaration

```swift
func selectItem(withTag tag: Int) -> Bool
```

```objc
- (BOOL) selectItemWithTag:(NSInteger) tag;
```

## Return Value

[`true`](../../Swift/true.md) if the item was successfully selected; otherwise, [`false`](../../Swift/false.md).

## Discussion

If no item with the specified tag is found, this method returns [`false`](../../Swift/false.md) and leaves the menu state unchanged.

You typically assign tags to menu items from Interface Builder, but you can also assign them programmatically using the setTag: method of [`NSMenuItem`](../nsmenuitem.md).

## Parameters

- `tag`: The tag of the item you want to select.

## See Also

### Dealing with selection
- [func select(NSMenuItem?)](./select%28_%29.md)
  Selects the specified menu item.
- [func selectItem(at: Int)](./selectitem%28at%29.md)
  Selects the item in the menu at the specified index.
- [func selectItem(withTitle: String)](./selectitem%28withtitle%29.md)
  Selects the item with the specified title.
- [func setTitle(String?)](./settitle%28_%29.md)
  Sets the string displayed in the receiver when the user isn’t pressing the mouse button.
- [var selectedItem: NSMenuItem?](./selecteditem.md)
  The menu item last selected by the user.
- [var indexOfSelectedItem: Int](./indexofselecteditem.md)
  The index of the item last selected by the user.
- [func synchronizeTitleAndSelectedItem()](./synchronizetitleandselecteditem%28%29.md)
  Synchronizes the pop-up button’s displayed item with the currently selected menu item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/selectitem(withtag:))*