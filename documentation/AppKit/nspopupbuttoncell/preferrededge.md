# preferredEdge

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The edge of the cell from which the menu should pop out when screen conditions are restrictive.

**Availability**:
- macOS

## Declaration

```swift
var preferredEdge: NSRectEdge { get set }
```

```objc
@property NSRectEdge preferredEdge;
```

## Discussion

At display time, if attaching the menu to the preferred edge would cause part of the menu to be obscured, the pop-up button may use a different edge. If no preferred edge is set, the pop-up button uses the bottom edge by default, which is [`NSMaxYEdge`](../../Foundation/nsrectedge/nsmaxyedge.md) for flipped views or [`NSMinYEdge`](../../Foundation/nsrectedge/nsminyedge.md) for unflipped views. Additional values for this property include [`NSMinXEdge`](../../Foundation/nsrectedge/nsminxedge.md) and [`NSMaxXEdge`](../../Foundation/nsrectedge/nsmaxxedge.md).

The exact location of the arrow is determined by examining the value of this property and [`arrowPosition`](./arrowposition.md).

- If the arrow position is [`NSPopUpButton.ArrowPosition.arrowAtCenter`](../nspopupbutton/arrowposition/arrowatcenter.md), the arrow stays in the center of the button and the value of this property determines which edge the arrow points to: `NSMinXEdge` points to the left, `NSMaxYEdge` points to the top, `NSMaxXEdge` points to the right, and `NSMinYEdge` points to the bottom.
- If the arrow position is [`NSPopUpButton.ArrowPosition.arrowAtBottom`](../nspopupbutton/arrowposition/arrowatbottom.md), the value of this property determines which edge at which the arrow is placed: `NSMinXEdge` places the arrow at the center of the left side, pointing to the left, `NSMinYEdge` places the arrow at bottom right corner, pointing up, `NSMaxXEdge` places the arrow at the center of the right side, pointing to the right, and `NSMaxYEdge` places the arrow at the bottom right corner, pointing down.

## See Also

### Accessing menu attributes
- [var menu: NSMenu?](./menu.md)
  The pop-up button’s associated menu.
- [var pullsDown: Bool](./pullsdown.md)
  A Boolean value that indicates the behavior of the button’s menu.
- [var autoenablesItems: Bool](./autoenablesitems.md)
  A Boolean value that indicates if the button automatically enables and disables its items every time a user event occurs.
- [var usesItemFromMenu: Bool](./usesitemfrommenu.md)
  A Boolean value that indicates if the control uses an item from the menu for its own title.
- [var altersStateOfSelectedItem: Bool](./altersstateofselecteditem.md)
  A Boolean value that indicates if the pop-up button links the state of the selected menu item to the current selection.
- [var arrowPosition: NSPopUpButton.ArrowPosition](./arrowposition.md)
  The position of the arrow displayed on the button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/preferrededge)*