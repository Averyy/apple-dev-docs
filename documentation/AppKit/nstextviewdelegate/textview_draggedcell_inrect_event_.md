# textView:draggedCell:inRect:event:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sent when the user attempts to drag a cell.

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

> **Deprecated**: Use textView:draggedCell:inRect:event:atIndex: instead.

## Declaration

```objc
- (void) textView:(NSTextView *) view draggedCell:(id<NSTextAttachmentCell>) cell inRect:(NSRect) rect event:(NSEvent *) event;
```

## Discussion

This method has been deprecated in favor of [`textView(_:draggedCell:in:event:at:)`](./textview%28_,draggedcell,in,event,at%29.md).

## Parameters

- `view`: The text view sending the message.
- `cell`: The cell being dragged.
- `rect`: The rectangle from which the cell was dragged.
- `event`: The mouse-down event that preceded the mouse-dragged event.

## See Also

### Related Documentation
- [- dragImage:at:offset:event:pasteboard:source:slideBack:](../nsview/dragimage_at_offset_event_pasteboard_source_slideback_.md)
  Initiates a dragging operation from the view, allowing the user to drag arbitrary data with a specified icon into any application that has window or view objects that accept dragged data.
- [func dragFile(String, from: NSRect, slideBack: Bool, event: NSEvent) -> Bool](../nsview/dragfile%28_,from,slideback,event%29.md)
  Initiates a dragging operation from the view, allowing the user to drag a file icon to any application that has window or view objects that accept files.
### Deprecated
- [- textView:clickedOnLink:](./textview_clickedonlink_.md)
  Sent after the user clicks on a link.
- [- textView:clickedOnCell:inRect:](./textview_clickedoncell_inrect_.md)
  Sent when the user clicks a cell.
- [- textView:doubleClickedOnCell:inRect:](./textview_doubleclickedoncell_inrect_.md)
  Sent when the user double-clicks a cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextviewdelegate/textview:draggedcell:inrect:event:)*