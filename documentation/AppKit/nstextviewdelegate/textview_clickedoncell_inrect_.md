# textView:clickedOnCell:inRect:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sent when the user clicks a cell.

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

> **Deprecated**: Use textView:clickedOnCell:inRect:atIndex: instead.

## Declaration

```objc
- (void) textView:(NSTextView *) textView clickedOnCell:(id<NSTextAttachmentCell>) cell inRect:(NSRect) cellFrame;
```

#### Discussion

This message is only sent if textView:clickedOnCell:inRect:atIndex: is not implemented. Implement this method in order to track the mouse after a mouse click on a cell.

## Parameters

- `textView`: The text view sending the message.
- `cell`: The cell clicked by the user.
- `cellFrame`: The frame of the clicked cell.

## See Also

### Deprecated
- [- textView:clickedOnLink:](./textview_clickedonlink_.md)
  Sent after the user clicks on a link.
- [- textView:draggedCell:inRect:event:](./textview_draggedcell_inrect_event_.md)
  Sent when the user attempts to drag a cell.
- [- textView:doubleClickedOnCell:inRect:](./textview_doubleclickedoncell_inrect_.md)
  Sent when the user double-clicks a cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextviewdelegate/textview:clickedoncell:inrect:)*