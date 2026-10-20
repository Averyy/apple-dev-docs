# tableView(_:updateDraggingItemsForDrag:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Implement this method to allow the table to update dragging items as they are dragged over a view.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
optional func tableView(_ tableView: NSTableView, updateDraggingItemsForDrag draggingInfo: any NSDraggingInfo)
```

```objc
- (void) tableView:(NSTableView *) tableView updateDraggingItemsForDrag:(id<NSDraggingInfo>) draggingInfo;
```

#### Discussion

Required for multi-image dragging. Typically this will involve invoking [`enumerateDraggingItems(options:for:classes:searchOptions:using:)`](../nsdragginginfo/enumeratedraggingitems%28options,for,classes,searchoptions,using%29.md) on the `draggingInfo` parameter value and setting the `draggingItem` object’s [`imageComponentsProvider`](../nsdraggingitem/imagecomponentsprovider.md) to a proper image based on the content.

For view-based table views, you can use the `NSTableCellView` method [`draggingImageComponents`](../nstablecellview/draggingimagecomponents.md). For cell-based tables, use the `NSCell` method [`draggingImageComponents(withFrame:in:)`](../nscell/draggingimagecomponents%28withframe,in%29.md).

## Parameters

- `tableView`: The table view.
- `draggingInfo`: The dragging information.

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
- [func tableView(NSTableView, draggingSession: NSDraggingSession, endedAt: NSPoint, operation: NSDragOperation)](./tableview%28_,draggingsession,endedat,operation%29.md)
  Implement this method to determine when a dragging session has ended.
- [func tableView(NSTableView, namesOfPromisedFilesDroppedAtDestination: URL, forDraggedRowsWith: IndexSet) -> [String]](./tableview%28_,namesofpromisedfilesdroppedatdestination,fordraggedrowswith%29.md)
  Returns an array of filenames that represent the `indexSet` rows for a drag to `dropDestination`.
- [func tableView(NSTableView, writeRowsWith: IndexSet, to: NSPasteboard) -> Bool](./tableview%28_,writerowswith,to%29.md)
  Returns a Boolean value that indicates whether a drag operation is allowed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableviewdatasource/tableview(_:updatedraggingitemsfordrag:))*