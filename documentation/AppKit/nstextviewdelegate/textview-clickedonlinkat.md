# textView(_:clickedOnLink:at:)

**Framework**: AppKit  
**Kind**: method

Sent after the user clicks a link.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func textView(_ textView: NSTextView, clickedOnLink link: Any, at charIndex: Int) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the click was handled; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false) to allow the next responder to handle it.

#### Discussion

The delegate can use this method to handle the click on the link. It is invoked by [`clicked(onLink:at:)`](nstextview/clicked(onlink:at:).md).

The `charIndex` parameter is a character index somewhere in the range of the link attribute. If the user actually physically clicked the link, then it should be the character that was originally clicked. In some cases a link may be opened indirectly or programmatically, in which case a character index somewhere in the range of the link attribute is supplied.

## Parameters

- `textView`: The text view sending the message.
- `link`: The link that was clicked; the value of  .
- `charIndex`: The character index where the click occurred, indexed within the text storage.

## See Also

- [func clicked(onLink: Any, at: Int)](nstextview/clicked(onlink:at:).md)
  Causes the text view to act as if the user clicked on some text with the given link as the value of a link attribute associated with the text.
- [func textView(NSTextView, clickedOn: any NSTextAttachmentCellProtocol, in: NSRect, at: Int)](nstextviewdelegate/textview(_:clickedon:in:at:).md)
  Sent when the user clicks a cell.
- [func textView(NSTextView, doubleClickedOn: any NSTextAttachmentCellProtocol, in: NSRect, at: Int)](nstextviewdelegate/textview(_:doubleclickedon:in:at:).md)
  Sent when the user double-clicks a cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextviewdelegate/textview(_:clickedonlink:at:))*