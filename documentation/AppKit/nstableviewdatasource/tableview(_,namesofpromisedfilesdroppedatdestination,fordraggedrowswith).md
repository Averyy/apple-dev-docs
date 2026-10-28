# tableView(_:namesOfPromisedFilesDroppedAtDestination:forDraggedRowsWith:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns an array of filenames that represent the `indexSet` rows for a drag to `dropDestination`.

**Availability**:
- macOS 10.0+ - Deprecated in 10.13

> **Deprecated**: Use NSFilePromiseReceiver objects instead

## Declaration

```swift
optional func tableView(_ tableView: NSTableView, namesOfPromisedFilesDroppedAtDestination dropDestination: URL, forDraggedRowsWith indexSet: IndexSet) -> [String]
```

```objc
- (NSArray<NSString *> *) tableView:(NSTableView *) tableView namesOfPromisedFilesDroppedAtDestination:(NSURL *) dropDestination forDraggedRowsWithIndexes:(NSIndexSet *) indexSet;
```

## Return Value

An array of filenames (not full paths) for the created files that the receiver promises to create.

## Discussion

This method is called when a destination has accepted a promise drag.

For more information on file promise dragging, see documentation on the NSDraggingSource protocol and [`namesOfPromisedFilesDropped(atDestination:)`](../nsdragginginfo/namesofpromisedfilesdropped%28atdestination%29.md).

## Parameters

- `tableView`: The table view that sent the message.
- `dropDestination`: The drop location where the files are created.
- `indexSet`: The indexes of the items being dragged.

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
- [func tableView(NSTableView, writeRowsWith: IndexSet, to: NSPasteboard) -> Bool](./tableview%28_,writerowswith,to%29.md)
  Returns a Boolean value that indicates whether a drag operation is allowed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableviewdatasource/tableview(_:namesofpromisedfilesdroppedatdestination:fordraggedrowswith:))*