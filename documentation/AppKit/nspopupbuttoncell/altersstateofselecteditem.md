# altersStateOfSelectedItem

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates if the pop-up button links the state of the selected menu item to the current selection.

**Availability**:
- macOS

## Declaration

```swift
var altersStateOfSelectedItem: Bool { get set }
```

```objc
@property BOOL altersStateOfSelectedItem;
```

## Discussion

When the value of this property is [`true`](../../Swift/true.md) (which is the default value), the state of the selected item is set to [`NSOnState`](../nsonstate.md). When the value of this property is [`false`](../../Swift/false.md), the items in the menu are left alone. When you change the value of this property, the state of the currently selected item is updated appropriately.

Note that this property affects only pop-up buttons (it is ignored for pull-down menus).

## See Also

### Related Documentation
- [func selectItem(at: Int)](./selectitem%28at%29.md)
  Selects the item in the menu at the specified index.
- [func select(NSMenuItem?)](./select%28_%29.md)
  Selects the specified menu item.
- [var selectedItem: NSMenuItem?](./selecteditem.md)
  The menu item last selected by the user.
- [func selectItem(withTitle: String)](./selectitem%28withtitle%29.md)
  Selects the item with the specified title.
### Accessing menu attributes
- [var menu: NSMenu?](./menu.md)
  The pop-up button’s associated menu.
- [var pullsDown: Bool](./pullsdown.md)
  A Boolean value that indicates the behavior of the button’s menu.
- [var autoenablesItems: Bool](./autoenablesitems.md)
  A Boolean value that indicates if the button automatically enables and disables its items every time a user event occurs.
- [var preferredEdge: NSRectEdge](./preferrededge.md)
  The edge of the cell from which the menu should pop out when screen conditions are restrictive.
- [var usesItemFromMenu: Bool](./usesitemfrommenu.md)
  A Boolean value that indicates if the control uses an item from the menu for its own title.
- [var arrowPosition: NSPopUpButton.ArrowPosition](./arrowposition.md)
  The position of the arrow displayed on the button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/altersstateofselecteditem)*