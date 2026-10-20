# tableView(_:writeRowsWith:to:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates whether a drag operation is allowed.

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: Use -tableView:pasteboardWriterForRow: instead

## Declaration

```swift
optional func tableView(_ tableView: NSTableView, writeRowsWith rowIndexes: IndexSet, to pboard: NSPasteboard) -> Bool
```

```objc
- (BOOL) tableView:(NSTableView *) tableView writeRowsWithIndexes:(NSIndexSet *) rowIndexes toPasteboard:(NSPasteboard *) pboard;
```

#### Return Value

`YES` if the drag operation is allowed, `NO` otherwise.

#### Discussion

Called by `aTableView` after it has been determined that a drag should begin, but before the drag has been started.

To refuse the drag, return [`false`](../../Swift/false.md). To start a drag, return [`true`](../../Swift/true.md) and place the drag data onto `pboard` (data, owner, and so on). The drag image and other drag-related information will be set up and provided by the table view once this call returns with [`true`](../../Swift/true.md).

## Parameters

- `tableView`: The table view that sent the message.
- `rowIndexes`: An index set of row numbers that will be participating in the drag.
- `pboard`: The pasteboard to which to write the drag data.

## See Also

### Drag and Drop
- [Supporting Table View Drag and Drop Through File Promises](../supporting-table-view-drag-and-drop-through-file-promises.md)
  Share data between macOS apps during drag and drop by using an item provider.
- [func tableView(NSTableView, acceptDrop: any NSDraggingInfo, row: Int, dropOperation: NSTableView.DropOperation) -> Bool](./tableview%28_,acceptdrop,row,dropoperation%29.md)
  Called by `aTableView` when the mouse button is released over a table view that previously decided to allow a drop.
- [func tableView(NSTableView, validateDrop: any NSDraggingInfo, proposedRow: Int, proposedDropOperation: NSTableView.DropOperation) -> NSDragOperation](./tableview%28_,validatedrop,proposedrow,proposeddropoperation%29.md)
  Used by `aTableView` to determine a valid drop target.
- [func tableView(NSTableView, draggingSession: NSDraggingSession, willBeginAt: NSPoint, forRowIndexes: IndexSet)](./tableview%28_,draggingsession,willbeginat,forrowindexes%29.md)
  Implement this method to determine when a dragging session will begin.
- [func tableView(NSTableView, updateDraggingItemsForDrag: any NSDraggingInfo)](./tableview%28_,updatedraggingitemsfordrag%29.md)
  Implement this method to allow the table to update dragging items as they are dragged over a view.
- [func tableView(NSTableView, draggingSession: NSDraggingSession, endedAt: NSPoint, operation: NSDragOperation)](./tableview%28_,draggingsession,endedat,operation%29.md)
  Implement this method to determine when a dragging session has ended.
- [func tableView(NSTableView, namesOfPromisedFilesDroppedAtDestination: URL, forDraggedRowsWith: IndexSet) -> [String]](./tableview%28_,namesofpromisedfilesdroppedatdestination,fordraggedrowswith%29.md)
  Returns an array of filenames that represent the `indexSet` rows for a drag to `dropDestination`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableviewdatasource/tableview(_:writerowswith:to:))*