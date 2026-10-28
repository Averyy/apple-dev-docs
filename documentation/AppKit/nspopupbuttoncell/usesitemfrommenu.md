# usesItemFromMenu

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates if the control uses an item from the menu for its own title.

**Availability**:
- macOS

## Declaration

```swift
var usesItemFromMenu: Bool { get set }
```

```objc
@property BOOL usesItemFromMenu;
```

## Discussion

When the value of this property is [`true`](../../Swift/true.md), a pull-down menu uses the title of the first menu item, and a pop-up menu uses the title of the currently selected menu (if no menu item is selected, the pop-up button displays no item and is drawn empty). When the value is [`false`](../../Swift/false.md), the menu item set with [`menuItem`](../nsmenuitemcell/menuitem.md) (`NSMenuItem`) is always displayed. The default value is [`true`](../../Swift/true.md).

## See Also

### Accessing menu attributes
- [var menu: NSMenu?](./menu.md)
  The pop-up button’s associated menu.
- [var pullsDown: Bool](./pullsdown.md)
  A Boolean value that indicates the behavior of the button’s menu.
- [var autoenablesItems: Bool](./autoenablesitems.md)
  A Boolean value that indicates if the button automatically enables and disables its items every time a user event occurs.
- [var preferredEdge: NSRectEdge](./preferrededge.md)
  The edge of the cell from which the menu should pop out when screen conditions are restrictive.
- [var altersStateOfSelectedItem: Bool](./altersstateofselecteditem.md)
  A Boolean value that indicates if the pop-up button links the state of the selected menu item to the current selection.
- [var arrowPosition: NSPopUpButton.ArrowPosition](./arrowposition.md)
  The position of the arrow displayed on the button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/usesitemfrommenu)*