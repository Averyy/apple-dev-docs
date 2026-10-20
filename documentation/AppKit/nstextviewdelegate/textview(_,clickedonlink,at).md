# textView(_:clickedOnLink:at:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sent after the user clicks a link.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
optional func textView(_ textView: NSTextView, clickedOnLink link: Any, at charIndex: Int) -> Bool
```

```objc
- (BOOL) textView:(NSTextView *) textView clickedOnLink:(id) link atIndex:(NSUInteger) charIndex;
```

#### Return Value

[`true`](../../Swift/true.md) if the click was handled; otherwise, [`false`](../../Swift/false.md) to allow the next responder to handle it.

#### Discussion

The delegate can use this method to handle the click on the link. It is invoked by [`clicked(onLink:at:)`](../nstextview/clicked%28onlink,at%29.md).

The `charIndex` parameter is a character index somewhere in the range of the link attribute. If the user actually physically clicked the link, then it should be the character that was originally clicked. In some cases a link may be opened indirectly or programmatically, in which case a character index somewhere in the range of the link attribute is supplied.

## Parameters

- `textView`: The text view sending the message.
- `link`: The link that was clicked; the value of [`link`](../../Foundation/nsattributedstring/key/link.md).
- `charIndex`: The character index where the click occurred, indexed within the text storage.

## See Also

### Related Documentation
- [func clicked(onLink: Any, at: Int)](../nstextview/clicked%28onlink,at%29.md)
  Causes the text view to act as if the user clicked on some text with the given link as the value of a link attribute associated with the text.
### Clicking and Pasting
- [func textView(NSTextView, clickedOn: any NSTextAttachmentCellProtocol, in: NSRect, at: Int)](./textview%28_,clickedon,in,at%29.md)
  Sent when the user clicks a cell.
- [func textView(NSTextView, doubleClickedOn: any NSTextAttachmentCellProtocol, in: NSRect, at: Int)](./textview%28_,doubleclickedon,in,at%29.md)
  Sent when the user double-clicks a cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextviewdelegate/textview(_:clickedonlink:at:))*