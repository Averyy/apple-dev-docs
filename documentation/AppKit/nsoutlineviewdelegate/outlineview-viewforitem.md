# outlineView(_:viewFor:item:)

**Framework**: AppKit  
**Kind**: method

Implemented to return the view used to display the specified item and column.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
optional func outlineView(_ outlineView: NSOutlineView, viewFor tableColumn: NSTableColumn?, item: Any) -> NSView?
```

#### Return Value

The view to display the specified column and row. Returning `nil` is acceptable, in which case a view is not shown at that location.

#### Discussion

This method is required if you wish to use `NSView` objects instead of `NSCell` objects for the cells within an outline view. Cells and views cannot be mixed within the same outline view.

It is recommended that the implementation of this method first call the `NSTableView` method [`makeView(withIdentifier:owner:)`](nstableview/makeview(withidentifier:owner:).md) passing, respectively, the `tableColumn` parameter’s identifier and `self` as the owner to attempt to reuse a view that is no longer visible. The frame of the view returned by this method is not important, and is automatically set by the outline view.

The view’s properties should be properly set up before returning the result.

When using Cocoa bindings, this method is optional if at least one identifier has been associated with the table view at design time. If this method is not implemented, the outline view automatically calls [`makeView(withIdentifier:owner:)`](nstableview/makeview(withidentifier:owner:).md) with the `tableColumn` parameter’s identifier and the outline view’s delegate as parameters, to attempt to reuse a previous view or automatically unarchive a prototype associated with the table view.

The [`autoresizingMask`](nsview/autoresizingmask-swift.property.md) of the returned view is automatically set to [`height`](nsview/autoresizingmask-swift.struct/height.md) to resize properly on row height changes.

## Parameters

- `outlineView`: The outline view that sent the message.
- `tableColumn`: The table column, or   if the row is a group row.
- `item`: The item displayed by the returned view.

## See Also

- [func outlineView(NSOutlineView, didAdd: NSTableRowView, forRow: Int)](nsoutlineviewdelegate/outlineview(_:didadd:forrow:).md)
  Implemented to know when a new row view is added to the table.
- [func outlineView(NSOutlineView, didRemove: NSTableRowView, forRow: Int)](nsoutlineviewdelegate/outlineview(_:didremove:forrow:).md)
  Implemented to know when a row view is removed from the table
- [func outlineView(NSOutlineView, rowViewForItem: Any) -> NSTableRowView?](nsoutlineviewdelegate/outlineview(_:rowviewforitem:).md)
  implement this method to return a custom `NSTableRowView` for a particular item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/outlineview(_:viewfor:item:))*