# textView(_:clickedOn:in:at:)

**Framework**: AppKit  
**Kind**: method

Sent when the user clicks a cell.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func textView(_ textView: NSTextView, clickedOn cell: any NSTextAttachmentCellProtocol, in cellFrame: NSRect, at charIndex: Int)
```

#### Discussion

The delegate can use this message as its cue to perform an action or select the attachment cell’s character. `aTextView` is the first text view in a series shared by a layout manager, not necessarily the one that draws `cell`.

The delegate may subsequently receive a [`textView(_:doubleClickedOn:in:at:)`](nstextviewdelegate/textview(_:doubleclickedon:in:at:).md) message if the user continues to perform a double click.

## Parameters

- `textView`: The text view sending the message.
- `cell`: The cell clicked by the user.
- `cellFrame`: The frame of the clicked cell.
- `charIndex`: The character index of the clicked cell.

## See Also

- [func textView(NSTextView, doubleClickedOn: any NSTextAttachmentCellProtocol, in: NSRect, at: Int)](nstextviewdelegate/textview(_:doubleclickedon:in:at:).md)
  Sent when the user double-clicks a cell.
- [func textView(NSTextView, clickedOnLink: Any, at: Int) -> Bool](nstextviewdelegate/textview(_:clickedonlink:at:).md)
  Sent after the user clicks a link.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextviewdelegate/textview(_:clickedon:in:at:))*