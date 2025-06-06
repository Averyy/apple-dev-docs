# setTitle(_:)

**Framework**: AppKit  
**Kind**: method

Sets the string displayed in the receiver when the user isn’t pressing the mouse button.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func setTitle(_ string: String?)
```

#### Discussion

For pull-down menus that get their titles from a menu item, this method simply sets the pop-up button cell’s menu item to the first item in the menu. For pop-up menus, if a menu item whose title matches `aString` exists, this method makes that menu item the current selection; otherwise, it creates a new menu item with the title `aString`, adds it to the pop-up menu, and selects it.

## Parameters

- `string`: The string to display.

## See Also

- [init(textCell: String, pullsDown: Bool)](nspopupbuttoncell/init(textcell:pullsdown:).md)
  Returns an `NSPopUpButtonCell` object initialized with the specified title.
- [func select(NSMenuItem?)](nspopupbuttoncell/select(_:).md)
  Selects the specified menu item.
- [func selectItem(at: Int)](nspopupbuttoncell/selectitem(at:).md)
  Selects the item in the menu at the specified index.
- [func selectItem(withTag: Int) -> Bool](nspopupbuttoncell/selectitem(withtag:).md)
  Selects the menu item with the specified tag.
- [func selectItem(withTitle: String)](nspopupbuttoncell/selectitem(withtitle:).md)
  Selects the item with the specified title.
- [var selectedItem: NSMenuItem?](nspopupbuttoncell/selecteditem.md)
  The menu item last selected by the user.
- [var indexOfSelectedItem: Int](nspopupbuttoncell/indexofselecteditem.md)
  The index of the item last selected by the user.
- [func synchronizeTitleAndSelectedItem()](nspopupbuttoncell/synchronizetitleandselecteditem.md)
  Synchronizes the pop-up button’s displayed item with the currently selected menu item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/settitle(_:))*