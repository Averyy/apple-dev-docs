# textView(_:urlForContentsOf:at:)

**Framework**: AppKit  
**Kind**: method

Returns a URL representing the document contents for a text attachment.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
optional func textView(_ textView: NSTextView, urlForContentsOf textAttachment: NSTextAttachment, at charIndex: Int) -> URL?
```

#### Return Value

The absolute URL for the document contents represented by `textAttachment`.

#### Discussion

The returned `NSURL` object is used by the text view to provide default behaviors involving text attachments such as Quick Look and double-clicking. For example, the `NSTextView` method [`quickLookPreviewableItems(inRanges:)`](nstextview/quicklookpreviewableitems(inranges:).md) uses this method for mapping text attachments to their corresponding document URLs, and `NSTextView` invokes the `NSWorkspace` method [`open(_:)`](nsworkspace/open(_:).md) with the URL returned from this method when the delegate has no [`textView(_:doubleClickedOn:in:at:)`](nstextviewdelegate/textview(_:doubleclickedon:in:at:).md) implementation.

## Parameters

- `textView`: The text view sending the message.
- `textAttachment`: The text attachment object containing an   object that holds the contents of the attached file.
- `charIndex`: The character index of the text attachment.

## See Also

- [func textView(NSTextView, doubleClickedOn: any NSTextAttachmentCellProtocol, in: NSRect, at: Int)](nstextviewdelegate/textview(_:doubleclickedon:in:at:).md)
  Sent when the user double-clicks a cell.
- [func quickLookPreviewableItems(inRanges: [NSValue]) -> [any QLPreviewItem]](nstextview/quicklookpreviewableitems(inranges:).md)
  Returns an array of URLs for items that can be displayed by QuickLook in the specified ranges.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextviewdelegate/textview(_:urlforcontentsof:at:))*