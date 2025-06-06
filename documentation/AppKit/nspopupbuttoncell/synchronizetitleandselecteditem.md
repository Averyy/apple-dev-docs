# synchronizeTitleAndSelectedItem()

**Framework**: AppKit  
**Kind**: method

Synchronizes the pop-up button’s displayed item with the currently selected menu item.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func synchronizeTitleAndSelectedItem()
```

#### Discussion

If no item is currently selected, this method synchronizes the pop-up buttons displayed item with the first menu item. If the pop-up button cell does not get its displayed item from a menu item, this method does nothing.

For pull-down menus, this method sets the displayed item to the title first menu item.

If the pop-up button’s menu does not contain any menu items, this method sets the pop-up button’s displayed item to `nil`, resulting in nothing being displayed in the control.

## See Also

- [func select(NSMenuItem?)](nspopupbuttoncell/select(_:).md)
  Selects the specified menu item.
- [func selectItem(at: Int)](nspopupbuttoncell/selectitem(at:).md)
  Selects the item in the menu at the specified index.
- [func selectItem(withTag: Int) -> Bool](nspopupbuttoncell/selectitem(withtag:).md)
  Selects the menu item with the specified tag.
- [func selectItem(withTitle: String)](nspopupbuttoncell/selectitem(withtitle:).md)
  Selects the item with the specified title.
- [func setTitle(String?)](nspopupbuttoncell/settitle(_:).md)
  Sets the string displayed in the receiver when the user isn’t pressing the mouse button.
- [var selectedItem: NSMenuItem?](nspopupbuttoncell/selecteditem.md)
  The menu item last selected by the user.
- [var indexOfSelectedItem: Int](nspopupbuttoncell/indexofselecteditem.md)
  The index of the item last selected by the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/synchronizetitleandselecteditem())*