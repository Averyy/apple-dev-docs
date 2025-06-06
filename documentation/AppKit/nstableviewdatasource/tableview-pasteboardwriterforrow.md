# tableView(_:pasteboardWriterForRow:)

**Framework**: AppKit  
**Kind**: method

Called to allow the table to support multiple item dragging.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
optional func tableView(_ tableView: NSTableView, pasteboardWriterForRow row: Int) -> (any NSPasteboardWriting)?
```

#### Return Value

Returns an instance of [`NSPasteboardItem`](nspasteboarditem.md) or a custom object that implements the [`NSPasteboardWriting`](nspasteboardwriting.md) protocol. Returning `nil` excludes the row from being dragged.

#### Discussion

This method is required for multi-image dragging.

If this method is implemented, then [`tableView(_:writeRowsWith:to:)`](nstableviewdatasource/tableview(_:writerowswith:to:).md) will not be called.

## Parameters

- `tableView`: The table view.
- `row`: The row.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableviewdatasource/tableview(_:pasteboardwriterforrow:))*