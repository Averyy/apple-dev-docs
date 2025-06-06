# selectItem(withTag:)

**Framework**: AppKit  
**Kind**: method

Selects the menu item with the specified tag.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func selectItem(withTag tag: Int) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the item was successfully selected; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

If no item with the specified tag is found, this method returns [`false`](https://developer.apple.com/documentation/swift/false) and leaves the menu state unchanged.

You typically assign tags to menu items from Interface Builder, but you can also assign them programmatically using the setTag: method of [`NSMenuItem`](nsmenuitem.md).

## Parameters

- `tag`: The tag of the item you want to select.

## See Also

- [func select(NSMenuItem?)](nspopupbuttoncell/select(_:).md)
  Selects the specified menu item.
- [func selectItem(at: Int)](nspopupbuttoncell/selectitem(at:).md)
  Selects the item in the menu at the specified index.
- [func selectItem(withTitle: String)](nspopupbuttoncell/selectitem(withtitle:).md)
  Selects the item with the specified title.
- [func setTitle(String?)](nspopupbuttoncell/settitle(_:).md)
  Sets the string displayed in the receiver when the user isn’t pressing the mouse button.
- [var selectedItem: NSMenuItem?](nspopupbuttoncell/selecteditem.md)
  The menu item last selected by the user.
- [var indexOfSelectedItem: Int](nspopupbuttoncell/indexofselecteditem.md)
  The index of the item last selected by the user.
- [func synchronizeTitleAndSelectedItem()](nspopupbuttoncell/synchronizetitleandselecteditem.md)
  Synchronizes the pop-up button’s displayed item with the currently selected menu item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/selectitem(withtag:))*