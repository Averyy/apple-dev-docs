# textView(_:urlForContentsOf:at:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns a URL representing the document contents for a text attachment.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
optional func textView(_ textView: NSTextView, urlForContentsOf textAttachment: NSTextAttachment, at charIndex: Int) -> URL?
```

```objc
- (NSURL *) textView:(NSTextView *) textView URLForContentsOfTextAttachment:(NSTextAttachment *) textAttachment atIndex:(NSUInteger) charIndex;
```

#### Return Value

The absolute URL for the document contents represented by `textAttachment`.

#### Discussion

The returned `NSURL` object is used by the text view to provide default behaviors involving text attachments such as Quick Look and double-clicking. For example, the `NSTextView` method [`quickLookPreviewableItems(inRanges:)`](../nstextview/quicklookpreviewableitems%28inranges%29.md) uses this method for mapping text attachments to their corresponding document URLs, and `NSTextView` invokes the `NSWorkspace` method [`open(_:)`](../nsworkspace/open%28_%29.md) with the URL returned from this method when the delegate has no [`textView(_:doubleClickedOn:in:at:)`](./textview%28_,doubleclickedon,in,at%29.md) implementation.

## Parameters

- `textView`: The text view sending the message.
- `textAttachment`: The text attachment object containing an `NSFileWrapper` object that holds the contents of the attached file.
- `charIndex`: The character index of the text attachment.

## See Also

### Related Documentation
- [func textView(NSTextView, doubleClickedOn: any NSTextAttachmentCellProtocol, in: NSRect, at: Int)](./textview%28_,doubleclickedon,in,at%29.md)
  Sent when the user double-clicks a cell.
- [func quickLookPreviewableItems(inRanges: [NSValue]) -> [any QLPreviewItem]](../nstextview/quicklookpreviewableitems%28inranges%29.md)
  Returns an array of URLs for items that can be displayed by QuickLook in the specified ranges.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextviewdelegate/textview(_:urlforcontentsof:at:))*