# didRemove(_:forRow:)

**Framework**: AppKit  
**Kind**: method

Invoked when a row view is removed from the table.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
func didRemove(_ rowView: NSTableRowView, forRow row: Int)
```

#### Discussion

The subclass can implement this method to be alerted when `rowView` has been removed from the table. The removed `rowView` may be reused by the table, so any additionally inserted views should be removed at this point. Subclasses must be sure to call `super`.

> **Note**:  This method is only applicable to [`NSView`](nsview.md)-based table views.

## Parameters

- `rowView`: The row view.
- `row`: The row index. The index is   for rows that are being deleted from the table, and no longer have a valid row; otherwise it is the valid row that is being removed due to it being moved off screen.

## See Also

- [func didAdd(NSTableRowView, forRow: Int)](nstableview/didadd(_:forrow:).md)
  Invoked when a row view is added to the table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/didremove(_:forrow:))*