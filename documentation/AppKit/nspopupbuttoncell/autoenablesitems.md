# autoenablesItems

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates if the button automatically enables and disables its items every time a user event occurs.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var autoenablesItems: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), the button automatically enables and disables items. The default value is [`true`](https://developer.apple.com/documentation/Swift/true). For more information about enabling and disabling menu items, see NSMenuValidation.

## See Also

- [var menu: NSMenu?](nspopupbuttoncell/menu.md)
  The pop-up button’s associated menu.
- [var pullsDown: Bool](nspopupbuttoncell/pullsdown.md)
  A Boolean value that indicates the behavior of the button’s menu.
- [var preferredEdge: NSRectEdge](nspopupbuttoncell/preferrededge.md)
  The edge of the cell from which the menu should pop out when screen conditions are restrictive.
- [var usesItemFromMenu: Bool](nspopupbuttoncell/usesitemfrommenu.md)
  A Boolean value that indicates if the control uses an item from the menu for its own title.
- [var altersStateOfSelectedItem: Bool](nspopupbuttoncell/altersstateofselecteditem.md)
  A Boolean value that indicates if the pop-up button links the state of the selected menu item to the current selection.
- [var arrowPosition: NSPopUpButton.ArrowPosition](nspopupbuttoncell/arrowposition.md)
  The position of the arrow displayed on the button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/autoenablesitems)*