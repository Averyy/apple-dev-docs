# didAdd(_:forRow:)

**Framework**: AppKit  
**Kind**: method

Invoked when a row view is added to the table.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
func didAdd(_ rowView: NSTableRowView, forRow row: Int)
```

#### Discussion

The subclass can implement this method to be alerted when `rowView` has been added to the table. At this point, the subclass can choose to add in extra views, or modify any properties of `rowView`. Subclasses must be sure to call super.

> **Note**:  This method is only applicable to [`NSView`](nsview.md)-based table views.

 This method is only applicable to [`NSView`](nsview.md)-based table views.

## Parameters

- `rowView`: The row view.
- `row`: The row index.

## See Also

- [func didRemove(NSTableRowView, forRow: Int)](nstableview/didremove(_:forrow:).md)
  Invoked when a row view is removed from the table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/didadd(_:forrow:))*