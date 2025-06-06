# selectItem(withTitle:)

**Framework**: AppKit  
**Kind**: method

Selects the item with the specified title.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func selectItem(withTitle title: String)
```

#### Discussion

By default, selecting or deselecting a menu item changes its state. To disassociate the current selection from the state of menu items, set the [`altersStateOfSelectedItem`](nspopupbuttoncell/altersstateofselecteditem.md) property to [`false`](https://developer.apple.com/documentation/swift/false).

## Parameters

- `title`: The title of the item to select. If you specify an empty string, or a string that does not match the title of a menu item, this method deselects the currently selected item.

## See Also

- [var altersStateOfSelectedItem: Bool](nspopupbuttoncell/altersstateofselecteditem.md)
  A Boolean value that indicates if the pop-up button links the state of the selected menu item to the current selection.
- [func select(NSMenuItem?)](nspopupbuttoncell/select(_:).md)
  Selects the specified menu item.
- [func selectItem(at: Int)](nspopupbuttoncell/selectitem(at:).md)
  Selects the item in the menu at the specified index.
- [func selectItem(withTag: Int) -> Bool](nspopupbuttoncell/selectitem(withtag:).md)
  Selects the menu item with the specified tag.
- [func setTitle(String?)](nspopupbuttoncell/settitle(_:).md)
  Sets the string displayed in the receiver when the user isn’t pressing the mouse button.
- [var selectedItem: NSMenuItem?](nspopupbuttoncell/selecteditem.md)
  The menu item last selected by the user.
- [var indexOfSelectedItem: Int](nspopupbuttoncell/indexofselecteditem.md)
  The index of the item last selected by the user.
- [func synchronizeTitleAndSelectedItem()](nspopupbuttoncell/synchronizetitleandselecteditem.md)
  Synchronizes the pop-up button’s displayed item with the currently selected menu item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/selectitem(withtitle:))*