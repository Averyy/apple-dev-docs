# outlineView(_:didRemove:forRow:)

**Framework**: AppKit  
**Kind**: method

Implemented to know when a row view is removed from the table

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
optional func outlineView(_ outlineView: NSOutlineView, didRemove rowView: NSTableRowView, forRow row: Int)
```

#### Discussion

The removed `rowView` may be reused by the table, so any additionally inserted views should be removed at this point.

## Parameters

- `outlineView`: The outline view that sent the message.
- `rowView`: The row view that was removed.
- `row`: The number of the row that was removed due to being moved offscreen, or   if the row was removed from the table so it is no longer valid.

## See Also

- [func outlineView(NSOutlineView, didAdd: NSTableRowView, forRow: Int)](nsoutlineviewdelegate/outlineview(_:didadd:forrow:).md)
  Implemented to know when a new row view is added to the table.
- [func outlineView(NSOutlineView, rowViewForItem: Any) -> NSTableRowView?](nsoutlineviewdelegate/outlineview(_:rowviewforitem:).md)
  implement this method to return a custom `NSTableRowView` for a particular item.
- [func outlineView(NSOutlineView, viewFor: NSTableColumn?, item: Any) -> NSView?](nsoutlineviewdelegate/outlineview(_:viewfor:item:).md)
  Implemented to return the view used to display the specified item and column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/outlineview(_:didremove:forrow:))*