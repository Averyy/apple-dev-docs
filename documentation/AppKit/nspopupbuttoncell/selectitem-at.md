# selectItem(at:)

**Framework**: AppKit  
**Kind**: method

Selects the item in the menu at the specified index.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func selectItem(at index: Int)
```

#### Discussion

By default, selecting or deselecting a menu item from a pop-up menu changes its state. Selecting a menu item from a pull-down menu does not automatically alter the state of the item. To disassociate the current selection from the state of menu items, set the [`altersStateOfSelectedItem`](nspopupbuttoncell/altersstateofselecteditem.md) property to [`false`](https://developer.apple.com/documentation/Swift/false).

Subclassers can override this method to catch all select calls.

## Parameters

- `index`: The index of the item you want to select, or   you want to deselect all menu items.

## See Also

- [var altersStateOfSelectedItem: Bool](nspopupbuttoncell/altersstateofselecteditem.md)
  A Boolean value that indicates if the pop-up button links the state of the selected menu item to the current selection.
- [func select(NSMenuItem?)](nspopupbuttoncell/select(_:).md)
  Selects the specified menu item.
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
- [func synchronizeTitleAndSelectedItem()](nspopupbuttoncell/synchronizetitleandselecteditem.md)
  Synchronizes the pop-up button’s displayed item with the currently selected menu item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/selectitem(at:))*