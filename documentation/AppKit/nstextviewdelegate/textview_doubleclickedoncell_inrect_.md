# textView:doubleClickedOnCell:inRect:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sent when the user double-clicks a cell.

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

> **Deprecated**: Use textView:doubleClickedOnCell:inRect:atIndex: instead.

## Declaration

```objc
- (void) textView:(NSTextView *) textView doubleClickedOnCell:(id<NSTextAttachmentCell>) cell inRect:(NSRect) cellFrame;
```

## Discussion

This message is only sent if [`textView(_:doubleClickedOn:in:at:)`](./textview%28_,doubleclickedon,in,at%29.md) is not implemented. Implement this method in order to track the mouse after a mouse double-click on a cell.

## Parameters

- `textView`: The text view sending the message.
- `cell`: The cell double-clicked by the user.
- `cellFrame`: The frame of the double-clicked cell.

## See Also

### Related Documentation
- [func textView(NSTextView, doubleClickedOn: any NSTextAttachmentCellProtocol, in: NSRect, at: Int)](./textview%28_,doubleclickedon,in,at%29.md)
  Sent when the user double-clicks a cell.
### Deprecated
- [- textView:clickedOnLink:](./textview_clickedonlink_.md)
  Sent after the user clicks on a link.
- [- textView:draggedCell:inRect:event:](./textview_draggedcell_inrect_event_.md)
  Sent when the user attempts to drag a cell.
- [- textView:clickedOnCell:inRect:](./textview_clickedoncell_inrect_.md)
  Sent when the user clicks a cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextviewdelegate/textview:doubleclickedoncell:inrect:)*