# objectValue

**Framework**: AppKit  
**Kind**: property

The object that represents the cell data.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
var objectValue: Any? { get set }
```

#### Discussion

The `objectValue` is automatically set by the table when using bindings or is the object returned by the [`NSTableViewDataSource`](nstableviewdatasource.md) protocol method [`tableView(_:objectValueFor:row:)`](nstableviewdatasource/tableview(_:objectvaluefor:row:).md).

## See Also

- [func tableView(NSTableView, objectValueFor: NSTableColumn?, row: Int) -> Any?](nstableviewdatasource/tableview(_:objectvaluefor:row:).md)
  Called by the table view to return the data object associated with the specified row and column.
- [Drag and Drop Programming Topics](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DragandDrop/DragandDrop.html#//apple_ref/doc/uid/10000069i)
- [Table View Programming Guide for Mac](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/TableView/Introduction/Introduction.html#//apple_ref/doc/uid/10000026i)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstablecellview/objectvalue)*