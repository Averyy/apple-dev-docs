# usesItemFromMenu

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates if the control uses an item from the menu for its own title.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var usesItemFromMenu: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), a pull-down menu uses the title of the first menu item, and a pop-up menu uses the title of the currently selected menu (if no menu item is selected, the pop-up button displays no item and is drawn empty). When the value is [`false`](https://developer.apple.com/documentation/Swift/false), the menu item set with [`menuItem`](nsmenuitemcell/menuitem.md) (`NSMenuItem`) is always displayed. The default value is [`true`](https://developer.apple.com/documentation/Swift/true).

## See Also

- [var menu: NSMenu?](nspopupbuttoncell/menu.md)
  The pop-up button’s associated menu.
- [var pullsDown: Bool](nspopupbuttoncell/pullsdown.md)
  A Boolean value that indicates the behavior of the button’s menu.
- [var autoenablesItems: Bool](nspopupbuttoncell/autoenablesitems.md)
  A Boolean value that indicates if the button automatically enables and disables its items every time a user event occurs.
- [var preferredEdge: NSRectEdge](nspopupbuttoncell/preferrededge.md)
  The edge of the cell from which the menu should pop out when screen conditions are restrictive.
- [var altersStateOfSelectedItem: Bool](nspopupbuttoncell/altersstateofselecteditem.md)
  A Boolean value that indicates if the pop-up button links the state of the selected menu item to the current selection.
- [var arrowPosition: NSPopUpButton.ArrowPosition](nspopupbuttoncell/arrowposition.md)
  The position of the arrow displayed on the button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/usesitemfrommenu)*