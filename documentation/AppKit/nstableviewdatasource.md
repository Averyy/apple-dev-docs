# NSTableViewDataSource

**Framework**: AppKit  
**Kind**: protocol

A set of methods that a table view uses to provide data to a table view and to allow the editing of the table view’s data source object.

**Availability**:
- macOS ?+

## Declaration

```swift
protocol NSTableViewDataSource : NSObjectProtocol
```

#### Overview

Some of the methods in this protocol, such as [`tableView(_:objectValueFor:row:)`](nstableviewdatasource/tableview(_:objectvaluefor:row:).md) and [`numberOfRows(in:)`](nstableviewdatasource/numberofrows(in:).md) along with other methods that return data, are called frequently, so they must be efficient.

> **Note**:  View-based table views must not use the [`tableView(_:setObjectValue:for:row:)`](nstableviewdatasource/tableview(_:setobjectvalue:for:row:).md) method for setting values. Instead the views must explicitly set the values for the fields, or use Cocoa bindings. Likewise, use target/action for editing. See [`Table View Programming Guide for Mac`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/TableView/Introduction/Introduction.html#//apple_ref/doc/uid/10000026i) for more information on populating view-based and cell-based table views.

 View-based table views must not use the [`tableView(_:setObjectValue:for:row:)`](nstableviewdatasource/tableview(_:setobjectvalue:for:row:).md) method for setting values. Instead the views must explicitly set the values for the fields, or use Cocoa bindings. Likewise, use target/action for editing. See [`Table View Programming Guide for Mac`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/TableView/Introduction/Introduction.html#//apple_ref/doc/uid/10000026i) for more information on populating view-based and cell-based table views.

If you’re not using Cocoa bindings to provide data to the table view, the following methods are required:

- [`numberOfRows(in:)`](nstableviewdatasource/numberofrows(in:).md)
- [`tableView(_:objectValueFor:row:)`](nstableviewdatasource/tableview(_:objectvaluefor:row:).md)
- [`tableView(_:setObjectValue:for:row:)`](nstableviewdatasource/tableview(_:setobjectvalue:for:row:).md) (cell-based tables only)

To learn more about Cocoa bindings, see [`Cocoa Bindings Programming Topics`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaBindings/CocoaBindings.html#//apple_ref/doc/uid/10000167i).

## Topics

### Getting Values
- [func numberOfRows(in: NSTableView) -> Int](nstableviewdatasource/numberofrows(in:).md)
  Returns the number of records managed for `aTableView` by the data source object.
- [func tableView(NSTableView, objectValueFor: NSTableColumn?, row: Int) -> Any?](nstableviewdatasource/tableview(_:objectvaluefor:row:).md)
  Called by the table view to return the data object associated with the specified row and column.
### Setting Values
- [func tableView(NSTableView, setObjectValue: Any?, for: NSTableColumn?, row: Int)](nstableviewdatasource/tableview(_:setobjectvalue:for:row:).md)
  Sets the data object for an item in the specified row and column.
### Implementing Pasteboard Support
- [func tableView(NSTableView, pasteboardWriterForRow: Int) -> (any NSPasteboardWriting)?](nstableviewdatasource/tableview(_:pasteboardwriterforrow:).md)
  Called to allow the table to support multiple item dragging.
### Drag and Drop
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
- [func tableView(NSTableView, draggingSession: NSDraggingSession, endedAt: NSPoint, operation: NSDragOperation)](nstableviewdatasource/tableview(_:draggingsession:endedat:operation:).md)
  Implement this method to determine when a dragging session has ended.
### Sorting
- [func tableView(NSTableView, sortDescriptorsDidChange: [NSSortDescriptor])](nstableviewdatasource/tableview(_:sortdescriptorsdidchange:).md)
  Called by `aTableView` to indicate that sorting may need to be done.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [NSTableViewDiffableDataSource](nstableviewdiffabledatasource-c5gl.md)
- [NSTableViewDiffableDataSourceReference](nstableviewdiffabledatasourcereference.md)

## See Also

- [protocol NSTableViewDelegate](nstableviewdelegate.md)
  A set of optional methods you implement in a table view delegate to customize the behavior of the table view.
- [class NSTableViewDiffableDataSource](nstableviewdiffabledatasource-c5gl.md)
  The object you use to manage data and provide items for a table view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableviewdatasource)*