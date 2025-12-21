# textView(_:write:at:to:type:)

**Framework**: AppKit  
**Kind**: method

Returns whether data of the specified type for the given cell could be written to the specified pasteboard.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func textView(_ view: NSTextView, write cell: any NSTextAttachmentCellProtocol, at charIndex: Int, to pboard: NSPasteboard, type: NSPasteboard.PasteboardType) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the write succeeded, [`false`](https://developer.apple.com/documentation/Swift/false) otherwise.

#### Discussion

The receiver should attempt to write the `cell` to `pboard` with the given `type`, and return success or failure.

## Parameters

- `view`: The text view sending the message.
- `cell`: The cell whose contents should be written to the pasteboard.
- `charIndex`: The index at which the cell was accessed.
- `pboard`: The pasteboard to which the cell’s contents should be written.
- `type`: The type of data that should be written.

## See Also

- [func textView(NSTextView, writablePasteboardTypesFor: any NSTextAttachmentCellProtocol, at: Int) -> [NSPasteboard.PasteboardType]](nstextviewdelegate/textview(_:writablepasteboardtypesfor:at:).md)
  Returns the writable pasteboard types for a given cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextviewdelegate/textview(_:write:at:to:type:))*