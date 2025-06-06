# tableView(_:namesOfPromisedFilesDroppedAtDestination:forDraggedRowsWith:)

**Framework**: AppKit  
**Kind**: method

Returns an array of filenames that represent the `indexSet` rows for a drag to `dropDestination`.

**Availability**:
- macOS 10.0+

## Declaration

```swift
optional func tableView(_ tableView: NSTableView, namesOfPromisedFilesDroppedAtDestination dropDestination: URL, forDraggedRowsWith indexSet: IndexSet) -> [String]
```

#### Return Value

An array of filenames (not full paths) for the created files that the receiver promises to create.

#### Discussion

This method is called when a destination has accepted a promise drag.

For more information on file promise dragging, see documentation on the NSDraggingSource protocol and [`namesOfPromisedFilesDropped(atDestination:)`](nsdragginginfo/namesofpromisedfilesdropped(atdestination:).md).

## Parameters

- `tableView`: The table view that sent the message.
- `dropDestination`: The drop location where the files are created.
- `indexSet`: The indexes of the items being dragged.

## See Also

- [Supporting Table View Drag and Drop Through File Promises](supporting-table-view-drag-and-drop-through-file-promises.md)
  Share data between macOS apps during drag and drop by using an item provider.
- [func tableView(NSTableView, acceptDrop: any NSDraggingInfo, row: Int, dropOperation: NSTableView.DropOperation) -> Bool](nstableviewdatasource/tableview(_:acceptdrop:row:dropoperation:).md)
  Called by `aTableView` when the mouse button is released over a table view that previously decided to allow a drop.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableviewdatasource/tableview(_:namesofpromisedfilesdroppedatdestination:fordraggedrowswith:))*