# tableView(_:draggingSession:willBeginAt:forRowIndexes:)

**Framework**: AppKit  
**Kind**: method

Implement this method to determine when a dragging session will begin.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
optional func tableView(_ tableView: NSTableView, draggingSession session: NSDraggingSession, willBeginAt screenPoint: NSPoint, forRowIndexes rowIndexes: IndexSet)
```

#### Discussion

Implement this method to know when the dragging session is about to begin and to potentially modify the dragging session.

The dragged item order will directly match the pasteboard writer array used to begin the dragging session with the `NSView` method [`beginDraggingSession(with:event:source:)`](nsview/begindraggingsession(with:event:source:).md). Hence, the order is deterministic, and can be used in [`tableView(_:acceptDrop:row:dropOperation:)`](nstableviewdatasource/tableview(_:acceptdrop:row:dropoperation:).md) when enumerating the [`NSDraggingInfo`](nsdragginginfo.md) pasteboard classes.

## Parameters

- `tableView`: The table view.
- `session`: The dragging session.
- `screenPoint`: The initial drag location in screen coordinates.
- `rowIndexes`: The indexes of the rows to be dragged, excluding rows that were not dragged due to   returning  .

## See Also

- [Supporting Table View Drag and Drop Through File Promises](supporting-table-view-drag-and-drop-through-file-promises.md)
  Share data between macOS apps during drag and drop by using an item provider.
- [func tableView(NSTableView, acceptDrop: any NSDraggingInfo, row: Int, dropOperation: NSTableView.DropOperation) -> Bool](nstableviewdatasource/tableview(_:acceptdrop:row:dropoperation:).md)
  Called by `aTableView` when the mouse button is released over a table view that previously decided to allow a drop.
- [func tableView(NSTableView, namesOfPromisedFilesDroppedAtDestination: URL, forDraggedRowsWith: IndexSet) -> [String]](nstableviewdatasource/tableview(_:namesofpromisedfilesdroppedatdestination:fordraggedrowswith:).md)
  Returns an array of filenames that represent the `indexSet` rows for a drag to `dropDestination`.
- [func tableView(NSTableView, validateDrop: any NSDraggingInfo, proposedRow: Int, proposedDropOperation: NSTableView.DropOperation) -> NSDragOperation](nstableviewdatasource/tableview(_:validatedrop:proposedrow:proposeddropoperation:).md)
  Used by `aTableView` to determine a valid drop target.
- [func tableView(NSTableView, writeRowsWith: IndexSet, to: NSPasteboard) -> Bool](nstableviewdatasource/tableview(_:writerowswith:to:).md)
  Returns a Boolean value that indicates whether a drag operation is allowed.
- [func tableView(NSTableView, updateDraggingItemsForDrag: any NSDraggingInfo)](nstableviewdatasource/tableview(_:updatedraggingitemsfordrag:).md)
  Implement this method to allow the table to update dragging items as they are dragged over a view.
- [func tableView(NSTableView, draggingSession: NSDraggingSession, endedAt: NSPoint, operation: NSDragOperation)](nstableviewdatasource/tableview(_:draggingsession:endedat:operation:).md)
  Implement this method to determine when a dragging session has ended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableviewdatasource/tableview(_:draggingsession:willbeginat:forrowindexes:))*