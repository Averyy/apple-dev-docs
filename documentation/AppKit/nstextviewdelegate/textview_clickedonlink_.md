# textView:clickedOnLink:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sent after the user clicks on a link.

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

> **Deprecated**: Use textView:clickedOnLink:atIndex: instead.

## Declaration

```objc
- (BOOL) textView:(NSTextView *) textView clickedOnLink:(id) link;
```

#### Discussion

This message is only sent if textView:clickedOnLink:atIndex: is not implemented.

## Parameters

- `textView`: The text view sending the message.
- `link`: The link that was clicked.

## See Also

### Related Documentation
- [func textView(NSTextView, clickedOnLink: Any, at: Int) -> Bool](./textview%28_,clickedonlink,at%29.md)
  Sent after the user clicks a link.
- [func clicked(onLink: Any, at: Int)](../nstextview/clicked%28onlink,at%29.md)
  Causes the text view to act as if the user clicked on some text with the given link as the value of a link attribute associated with the text.
### Deprecated
- [- textView:draggedCell:inRect:event:](./textview_draggedcell_inrect_event_.md)
  Sent when the user attempts to drag a cell.
- [- textView:clickedOnCell:inRect:](./textview_clickedoncell_inrect_.md)
  Sent when the user clicks a cell.
- [- textView:doubleClickedOnCell:inRect:](./textview_doubleclickedoncell_inrect_.md)
  Sent when the user double-clicks a cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextviewdelegate/textview:clickedonlink:)*