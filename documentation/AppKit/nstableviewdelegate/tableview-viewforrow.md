# tableView(_:viewFor:row:)

**Framework**: AppKit  
**Kind**: method

Asks the delegate for a view to display the specified row and column.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
optional func tableView(_ tableView: NSTableView, viewFor tableColumn: NSTableColumn?, row: Int) -> NSView?
```

#### Return Value

The view to display the specified column and row. If you return `nil`, a view will not be shown at that location.

#### Discussion

This method is required if you want to use [`NSView`](nsview.md) objects instead of [`NSCell`](nscell.md) objects for the cells within a table view. Cells and views can’t be mixed within the same table view.

It’s recommended that the implementation of this method first call the [`NSTableView`](nstableview.md) method [`makeView(withIdentifier:owner:)`](nstableview/makeview(withidentifier:owner:).md) passing, respectively, the `tableColumn` parameter’s identifier and `self` as the owner to attempt to reuse a view that is no longer visible or automatically unarchive an associated prototype view for that identifier. The `frame` of the view returned by this method is not important, and it will be automatically set by the table.

The view’s properties should be properly set up before returning the result.

When using Cocoa bindings, this method is optional if at least one identifier has been associated with the table view at design time. (Note that a view’s identifier must be the same as the identifier of its column. An easy way to achieve this is to use the Automatic identifier setting in Interface Builder.) If this method isn’t implemented, the table will automatically call the [`NSTableView`](nstableview.md) method [`makeView(withIdentifier:owner:)`](nstableview/makeview(withidentifier:owner:).md) with the `tableColumn` parameter’s identifier and the table view’s `delegate` as parameters, to attempt to reuse a previous view, or automatically unarchive a prototype associated with the table view. If this method is implemented, you can set up properties that aren’t using bindings.

The autoresizing mask of the returned view will automatically be set to [`height`](nsview/autoresizingmask-swift.struct/height.md) to resize properly on row height changes.

## Parameters

- `tableView`: The table view that sent the message.
- `tableColumn`: The table column. (If the row is a group row,   is  .)
- `row`: The row index.

## See Also

- [Table View Programming Guide for Mac](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/TableView/Introduction/Introduction.html#//apple_ref/doc/uid/10000026i)
- [Drag and Drop Programming Topics](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DragandDrop/DragandDrop.html#//apple_ref/doc/uid/10000069i)
- [func tableView(NSTableView, rowViewForRow: Int) -> NSTableRowView?](nstableviewdelegate/tableview(_:rowviewforrow:).md)
  Asks the delegate for a view to display the specified row.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableviewdelegate/tableview(_:viewfor:row:))*