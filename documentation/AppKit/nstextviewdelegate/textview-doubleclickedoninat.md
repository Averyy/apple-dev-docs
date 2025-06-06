# textView(_:doubleClickedOn:in:at:)

**Framework**: AppKit  
**Kind**: method

Sent when the user double-clicks a cell.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func textView(_ textView: NSTextView, doubleClickedOn cell: any NSTextAttachmentCellProtocol, in cellFrame: NSRect, at charIndex: Int)
```

#### Discussion

The delegate can use this message as its cue to perform an action, such as opening the file represented by the attachment. `aTextView` is the first text view in a series shared by a layout manager, not necessarily the one that draws `cell`.

## Parameters

- `textView`: The text view sending the message.
- `cell`: The cell double-clicked by the user.
- `cellFrame`: The frame of the double-clicked cell.
- `charIndex`: The character index of the double-clicked cell.

## See Also

- [func textView(NSTextView, clickedOn: any NSTextAttachmentCellProtocol, in: NSRect, at: Int)](nstextviewdelegate/textview(_:clickedon:in:at:).md)
  Sent when the user clicks a cell.
- [func textView(NSTextView, clickedOnLink: Any, at: Int) -> Bool](nstextviewdelegate/textview(_:clickedonlink:at:).md)
  Sent after the user clicks a link.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextviewdelegate/textview(_:doubleclickedon:in:at:))*