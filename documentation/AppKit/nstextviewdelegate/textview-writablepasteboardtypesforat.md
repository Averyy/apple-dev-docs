# textView(_:writablePasteboardTypesFor:at:)

**Framework**: AppKit  
**Kind**: method

Returns the writable pasteboard types for a given cell.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func textView(_ view: NSTextView, writablePasteboardTypesFor cell: any NSTextAttachmentCellProtocol, at charIndex: Int) -> [NSPasteboard.PasteboardType]
```

#### Return Value

An array of types that can be written to the pasteboard for `cell`.

#### Discussion

This method is invoked after the user clicks `cell` at the specified `charIndex` location in `aTextView`. If the [`textView(_:draggedCell:in:event:at:)`](nstextviewdelegate/textview(_:draggedcell:in:event:at:).md) is not used, this method and [`textView(_:write:at:to:type:)`](nstextviewdelegate/textview(_:write:at:to:type:).md) allow `aTextView` to take care of attachment dragging and pasting, with the delegate responsible only for writing the attachment to the pasteboard.

## Parameters

- `view`: The text view sending the message.
- `cell`: The cell in question.
- `charIndex`: The character index in the text view that was clicked.

## See Also

- [func textView(NSTextView, write: any NSTextAttachmentCellProtocol, at: Int, to: NSPasteboard, type: NSPasteboard.PasteboardType) -> Bool](nstextviewdelegate/textview(_:write:at:to:type:).md)
  Returns whether data of the specified type for the given cell could be written to the specified pasteboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextviewdelegate/textview(_:writablepasteboardtypesfor:at:))*