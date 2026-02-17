# objectValue

**Framework**: AppKit  
**Kind**: property

The object that represents the cell data.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var objectValue: Any? { get set }
```

#### Discussion

The `objectValue` is automatically set by the table when using bindings or is the object returned by the [`NSTableViewDataSource`](nstableviewdatasource.md) protocol method [`tableView(_:objectValueFor:row:)`](nstableviewdatasource/tableview(_:objectvaluefor:row:).md).

## See Also

- [func tableView(NSTableView, objectValueFor: NSTableColumn?, row: Int) -> Any?](nstableviewdatasource/tableview(_:objectvaluefor:row:).md)
  Called by the table view to return the data object associated with the specified row and column.
- [Drag and Drop](drag-and-drop.md)
  Support the direct manipulation of your app’s content using drag and drop.
- [Table View](table-view.md)
  Display custom data in rows and columns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstablecellview/objectvalue)*