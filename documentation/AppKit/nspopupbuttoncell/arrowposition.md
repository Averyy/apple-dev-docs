# arrowPosition

**Framework**: AppKit  
**Kind**: property

The position of the arrow displayed on the button.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var arrowPosition: NSPopUpButton.ArrowPosition { get set }
```

#### Discussion

When the value of this property is [`NSPopUpButton.ArrowPosition.noArrow`](nspopupbutton/arrowposition/noarrow.md), the control displays no arrow. [`NSPopUpButton.ArrowPosition.arrowAtCenter`](nspopupbutton/arrowposition/arrowatcenter.md) displays the arrow centered horizontally within the cell and  [`NSPopUpButton.ArrowPosition.arrowAtBottom`](nspopupbutton/arrowposition/arrowatbottom.md) displays the arrow at the edge of the cell. This property is used with [`preferredEdge`](nspopupbuttoncell/preferrededge.md) to determine the exact location and orientation of the arrow.

This property applies to only bezel style and borderless pop-up buttons.

## See Also

- [var menu: NSMenu?](nspopupbuttoncell/menu.md)
  The pop-up button’s associated menu.
- [var pullsDown: Bool](nspopupbuttoncell/pullsdown.md)
  A Boolean value that indicates the behavior of the button’s menu.
- [var autoenablesItems: Bool](nspopupbuttoncell/autoenablesitems.md)
  A Boolean value that indicates if the button automatically enables and disables its items every time a user event occurs.
- [var preferredEdge: NSRectEdge](nspopupbuttoncell/preferrededge.md)
  The edge of the cell from which the menu should pop out when screen conditions are restrictive.
- [var usesItemFromMenu: Bool](nspopupbuttoncell/usesitemfrommenu.md)
  A Boolean value that indicates if the control uses an item from the menu for its own title.
- [var altersStateOfSelectedItem: Bool](nspopupbuttoncell/altersstateofselecteditem.md)
  A Boolean value that indicates if the pop-up button links the state of the selected menu item to the current selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/arrowposition)*