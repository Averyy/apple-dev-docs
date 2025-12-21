# tableView(_:acceptDrop:row:dropOperation:)

**Framework**: AppKit  
**Kind**: method

Called by `aTableView` when the mouse button is released over a table view that previously decided to allow a drop.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func tableView(_ tableView: NSTableView, acceptDrop info: any NSDraggingInfo, row: Int, dropOperation: NSTableView.DropOperation) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the drop operation was successful, otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

The data source should incorporate the data from the dragging pasteboard in the implementation of this method. You can use the [`draggingPasteboard`](nsdragginginfo/draggingpasteboard.md) method to get the data for the drop operation from `info`.

To accept a drop on the second row, `row` would be 2 and `operation` would be `NSTableViewDropOn`. To accept a drop below the last row, `row` would be `[aTableView numberOfRows]` and `operation` would be `NSTableViewDropAbove`.

## Parameters

- `tableView`: The table view that sent the message.
- `info`: An object that contains more information about this dragging operation.
- `row`: The index of the proposed target row.
- `dropOperation`: The type of dragging operation.

## See Also

- [Supporting Table View Drag and Drop Through File Promises](supporting-table-view-drag-and-drop-through-file-promises.md)
  Share data between macOS apps during drag and drop by using an item provider.
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
- [func tableView(NSTableView, draggingSession: NSDraggingSession, endedAt: NSPoint, operation: NSDragOperation)](nstableviewdatasource/tableview(_:draggingsession:endedat:operation:).md)
  Implement this method to determine when a dragging session has ended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableviewdatasource/tableview(_:acceptdrop:row:dropoperation:))*