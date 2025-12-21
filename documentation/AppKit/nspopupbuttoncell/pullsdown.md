# pullsDown

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates the behavior of the button’s menu.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var pullsDown: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), the menu behaves like a pull-down menu; when the value is [`false`](https://developer.apple.com/documentation/Swift/false), it behaves like a pop-up menu. If you use this property to change the menu type from a pop-up menu to a pull-down menu, and the cell alters the state of its selected items, the state of the currently selected item is set to [`NSOffState`](nsoffstate.md) before the menu type is changed.

## See Also

- [func synchronizeTitleAndSelectedItem()](nspopupbuttoncell/synchronizetitleandselecteditem.md)
  Synchronizes the pop-up button’s displayed item with the currently selected menu item.
- [var menu: NSMenu?](nspopupbuttoncell/menu.md)
  The pop-up button’s associated menu.
- [var autoenablesItems: Bool](nspopupbuttoncell/autoenablesitems.md)
  A Boolean value that indicates if the button automatically enables and disables its items every time a user event occurs.
- [var preferredEdge: NSRectEdge](nspopupbuttoncell/preferrededge.md)
  The edge of the cell from which the menu should pop out when screen conditions are restrictive.
- [var usesItemFromMenu: Bool](nspopupbuttoncell/usesitemfrommenu.md)
  A Boolean value that indicates if the control uses an item from the menu for its own title.
- [var altersStateOfSelectedItem: Bool](nspopupbuttoncell/altersstateofselecteditem.md)
  A Boolean value that indicates if the pop-up button links the state of the selected menu item to the current selection.
- [var arrowPosition: NSPopUpButton.ArrowPosition](nspopupbuttoncell/arrowposition.md)
  The position of the arrow displayed on the button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/pullsdown)*