# tableView(_:validateDrop:proposedRow:proposedDropOperation:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Used by `aTableView` to determine a valid drop target.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
optional func tableView(_ tableView: NSTableView, validateDrop info: any NSDraggingInfo, proposedRow row: Int, proposedDropOperation dropOperation: NSTableView.DropOperation) -> NSDragOperation
```

```objc
- (NSDragOperation) tableView:(NSTableView *) tableView validateDrop:(id<NSDraggingInfo>) info proposedRow:(NSInteger) row proposedDropOperation:(NSTableViewDropOperation) dropOperation;
```

## Return Value

The dragging operation the data source will perform.

## Discussion

The data source may retarget a drop by calling [`setDropRow(_:dropOperation:)`](../nstableview/setdroprow%28_,dropoperation%29.md) and returning something other than `NSDragOperationNone`. A data source might retarget for various reasons, such as to provide better visual feedback when inserting into a sorted position.

To propose a drop on the second row, `row` would be 2 and `operation` would be `NSTableViewDropOn`. To propose a drop below the last row, `row` would be `[aTableView numberOfRows]` and `operation` would be `NSTableViewDropAbove`.

## Parameters

- `tableView`: The table view that sent the message.
- `info`: An object that contains more information about this dragging operation.
- `row`: The index of the proposed target row.
- `dropOperation`: The type of dragging operation proposed.

## See Also

### Drag and Drop
- [Supporting Table View Drag and Drop Through File Promises](../supporting-table-view-drag-and-drop-through-file-promises.md)
  Share data between macOS apps during drag and drop by using an item provider.
- [func tableView(NSTableView, acceptDrop: any NSDraggingInfo, row: Int, dropOperation: NSTableView.DropOperation) -> Bool](./tableview%28_,acceptdrop,row,dropoperation%29.md)
  Called by `aTableView` when the mouse button is released over a table view that previously decided to allow a drop.
- [func tableView(NSTableView, draggingSession: NSDraggingSession, willBeginAt: NSPoint, forRowIndexes: IndexSet)](./tableview%28_,draggingsession,willbeginat,forrowindexes%29.md)
  Implement this method to determine when a dragging session will begin.
- [func tableView(NSTableView, updateDraggingItemsForDrag: any NSDraggingInfo)](./tableview%28_,updatedraggingitemsfordrag%29.md)
  Implement this method to allow the table to update dragging items as they are dragged over a view.
- [func tableView(NSTableView, draggingSession: NSDraggingSession, endedAt: NSPoint, operation: NSDragOperation)](./tableview%28_,draggingsession,endedat,operation%29.md)
  Implement this method to determine when a dragging session has ended.
- [func tableView(NSTableView, namesOfPromisedFilesDroppedAtDestination: URL, forDraggedRowsWith: IndexSet) -> [String]](./tableview%28_,namesofpromisedfilesdroppedatdestination,fordraggedrowswith%29.md)
  Returns an array of filenames that represent the `indexSet` rows for a drag to `dropDestination`.
- [func tableView(NSTableView, writeRowsWith: IndexSet, to: NSPasteboard) -> Bool](./tableview%28_,writerowswith,to%29.md)
  Returns a Boolean value that indicates whether a drag operation is allowed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableviewdatasource/tableview(_:validatedrop:proposedrow:proposeddropoperation:))*