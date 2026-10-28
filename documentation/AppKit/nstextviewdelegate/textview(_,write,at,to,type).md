# textView(_:write:at:to:type:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns whether data of the specified type for the given cell could be written to the specified pasteboard.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
optional func textView(_ view: NSTextView, write cell: any NSTextAttachmentCellProtocol, at charIndex: Int, to pboard: NSPasteboard, type: NSPasteboard.PasteboardType) -> Bool
```

```objc
- (BOOL) textView:(NSTextView *) view writeCell:(id<NSTextAttachmentCell>) cell atIndex:(NSUInteger) charIndex toPasteboard:(NSPasteboard *) pboard type:(NSPasteboardType) type;
```

## Return Value

[`true`](../../Swift/true.md) if the write succeeded, [`false`](../../Swift/false.md) otherwise.

## Discussion

The receiver should attempt to write the `cell` to `pboard` with the given `type`, and return success or failure.

## Parameters

- `view`: The text view sending the message.
- `cell`: The cell whose contents should be written to the pasteboard.
- `charIndex`: The index at which the cell was accessed.
- `pboard`: The pasteboard to which the cell’s contents should be written.
- `type`: The type of data that should be written.

## See Also

### Managing the Pasteboard
- [func textView(NSTextView, writablePasteboardTypesFor: any NSTextAttachmentCellProtocol, at: Int) -> [NSPasteboard.PasteboardType]](./textview%28_,writablepasteboardtypesfor,at%29.md)
  Returns the writable pasteboard types for a given cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextviewdelegate/textview(_:write:at:to:type:))*