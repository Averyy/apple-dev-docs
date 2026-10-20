# tableView(_:acceptDrop:row:dropOperation:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Called by `aTableView` when the mouse button is released over a table view that previously decided to allow a drop.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
optional func tableView(_ tableView: NSTableView, acceptDrop info: any NSDraggingInfo, row: Int, dropOperation: NSTableView.DropOperation) -> Bool
```

```objc
- (BOOL) tableView:(NSTableView *) tableView acceptDrop:(id<NSDraggingInfo>) info row:(NSInteger) row dropOperation:(NSTableViewDropOperation) dropOperation;
```

#### Return Value

[`true`](../../Swift/true.md) if the drop operation was successful, otherwise [`false`](../../Swift/false.md).

#### Discussion

The data source should incorporate the data from the dragging pasteboard in the implementation of this method. You can use the [`draggingPasteboard`](../nsdragginginfo/draggingpasteboard.md) method to get the data for the drop operation from `info`.

To accept a drop on the second row, `row` would be 2 and `operation` would be `NSTableViewDropOn`. To accept a drop below the last row, `row` would be `[aTableView numberOfRows]` and `operation` would be `NSTableViewDropAbove`.

## Parameters

- `tableView`: The table view that sent the message.
- `info`: An object that contains more information about this dragging operation.
- `row`: The index of the proposed target row.
- `dropOperation`: The type of dragging operation.

## See Also

### Drag and Drop
- [Supporting Table View Drag and Drop Through File Promises](../supporting-table-view-drag-and-drop-through-file-promises.md)
  Share data between macOS apps during drag and drop by using an item provider.
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
- [func tableView(NSTableView, writeRowsWith: IndexSet, to: NSPasteboard) -> Bool](./tableview%28_,writerowswith,to%29.md)
  Returns a Boolean value that indicates whether a drag operation is allowed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableviewdatasource/tableview(_:acceptdrop:row:dropoperation:))*