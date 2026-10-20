# clicked(onLink:at:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Causes the text view to act as if the user clicked on some text with the given link as the value of a link attribute associated with the text.

**Availability**:
- macOS

## Declaration

```swift
func clicked(onLink link: Any, at charIndex: Int)
```

```objc
- (void) clickedOnLink:(id) link atIndex:(NSUInteger) charIndex;
```

#### Discussion

If, for instance, you have a special attachment cell that can follow links, you can use this method to ask the text view to follow a link once you decide it should. In addition, this method is invoked by the text view during mouse tracking if the user clicks a link.

The `charIndex` parameter is a character index somewhere in the range of the link attribute. If the user actually physically clicked the link, then it should be the character that was originally clicked. In some cases a link may be opened indirectly or programmatically, in which case a character index somewhere in the range of the link attribute is supplied.

This method sends the [`textView(_:clickedOnLink:at:)`](../nstextviewdelegate/textview%28_,clickedonlink,at%29.md) delegate message if the delegate implements it, so that the delegate can handle the click.

## Parameters

- `link`: The link that was clicked; the value of [`link`](../../Foundation/nsattributedstring/key/link.md).
- `charIndex`: The character index where the click occurred, indexed within the text storage.

## See Also

### Related Documentation
- [func textView(NSTextView, clickedOnLink: Any, at: Int) -> Bool](../nstextviewdelegate/textview%28_,clickedonlink,at%29.md)
  Sent after the user clicks a link.
### Clicking and pasting
- [func pasteAsPlainText(Any?)](./pasteasplaintext%28_%29.md)
  Inserts the contents of the pasteboard into the receiver’s text as plain text.
- [func pasteAsRichText(Any?)](./pasteasrichtext%28_%29.md)
  This action method inserts the contents of the pasteboard into the receiver’s text as rich text, maintaining its attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/clicked(onlink:at:))*