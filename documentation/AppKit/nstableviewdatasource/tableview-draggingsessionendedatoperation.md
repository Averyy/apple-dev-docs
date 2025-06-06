# tableView(_:draggingSession:endedAt:operation:)

**Framework**: AppKit  
**Kind**: method

Implement this method to determine when a dragging session has ended.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
optional func tableView(_ tableView: NSTableView, draggingSession session: NSDraggingSession, endedAt screenPoint: NSPoint, operation: NSDragOperation)
```

#### Discussion

This delegate method can be used to determine when the dragging source operation ended at a specific location, such as the trash, by checking for an operation of [`delete`](nsdragoperation/delete.md).

## Parameters

- `tableView`: The table view.
- `session`: The dragging session.
- `screenPoint`: The ending drag location in screen coordinates.
- `operation`: The drag operation. See   for supported values.

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
- [func tableView(NSTableView, draggingSession: NSDraggingSession, willBeginAt: NSPoint, forRowIndexes: IndexSet)](nstableviewdatasource/tableview(_:draggingsession:willbeginat:forrowindexes:).md)
  Implement this method to determine when a dragging session will begin.
- [func tableView(NSTableView, updateDraggingItemsForDrag: any NSDraggingInfo)](nstableviewdatasource/tableview(_:updatedraggingitemsfordrag:).md)
  Implement this method to allow the table to update dragging items as they are dragged over a view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableviewdatasource/tableview(_:draggingsession:endedat:operation:))*