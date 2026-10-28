# pullsDown

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates the behavior of the button’s menu.

**Availability**:
- macOS

## Declaration

```swift
var pullsDown: Bool { get set }
```

```objc
@property BOOL pullsDown;
```

## Discussion

When the value of this property is [`true`](../../Swift/true.md), the menu behaves like a pull-down menu; when the value is [`false`](../../Swift/false.md), it behaves like a pop-up menu. If you use this property to change the menu type from a pop-up menu to a pull-down menu, and the cell alters the state of its selected items, the state of the currently selected item is set to [`NSOffState`](../nsoffstate.md) before the menu type is changed.

## See Also

### Related Documentation
- [func synchronizeTitleAndSelectedItem()](./synchronizetitleandselecteditem%28%29.md)
  Synchronizes the pop-up button’s displayed item with the currently selected menu item.
### Accessing menu attributes
- [var menu: NSMenu?](./menu.md)
  The pop-up button’s associated menu.
- [var autoenablesItems: Bool](./autoenablesitems.md)
  A Boolean value that indicates if the button automatically enables and disables its items every time a user event occurs.
- [var preferredEdge: NSRectEdge](./preferrededge.md)
  The edge of the cell from which the menu should pop out when screen conditions are restrictive.
- [var usesItemFromMenu: Bool](./usesitemfrommenu.md)
  A Boolean value that indicates if the control uses an item from the menu for its own title.
- [var altersStateOfSelectedItem: Bool](./altersstateofselecteditem.md)
  A Boolean value that indicates if the pop-up button links the state of the selected menu item to the current selection.
- [var arrowPosition: NSPopUpButton.ArrowPosition](./arrowposition.md)
  The position of the arrow displayed on the button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/pullsdown)*