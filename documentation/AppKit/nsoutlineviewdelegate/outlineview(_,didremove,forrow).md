# outlineView(_:didRemove:forRow:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Implemented to know when a row view is removed from the table

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
optional func outlineView(_ outlineView: NSOutlineView, didRemove rowView: NSTableRowView, forRow row: Int)
```

```objc
- (void) outlineView:(NSOutlineView *) outlineView didRemoveRowView:(NSTableRowView *) rowView forRow:(NSInteger) row;
```

## Discussion

The removed `rowView` may be reused by the table, so any additionally inserted views should be removed at this point.

## Parameters

- `outlineView`: The outline view that sent the message.
- `rowView`: The row view that was removed.
- `row`: The number of the row that was removed due to being moved offscreen, or `-1` if the row was removed from the table so it is no longer valid.

## See Also

### Working with NSView-Based Outline Views
- [func outlineView(NSOutlineView, didAdd: NSTableRowView, forRow: Int)](./outlineview%28_,didadd,forrow%29.md)
  Implemented to know when a new row view is added to the table.
- [func outlineView(NSOutlineView, rowViewForItem: Any) -> NSTableRowView?](./outlineview%28_,rowviewforitem%29.md)
  implement this method to return a custom `NSTableRowView` for a particular item.
- [func outlineView(NSOutlineView, viewFor: NSTableColumn?, item: Any) -> NSView?](./outlineview%28_,viewfor,item%29.md)
  Implemented to return the view used to display the specified item and column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/outlineview(_:didremove:forrow:))*