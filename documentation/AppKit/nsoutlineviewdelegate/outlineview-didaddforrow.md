# outlineView(_:didAdd:forRow:)

**Framework**: AppKit  
**Kind**: method

Implemented to know when a new row view is added to the table.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
optional func outlineView(_ outlineView: NSOutlineView, didAdd rowView: NSTableRowView, forRow row: Int)
```

#### Discussion

This delegate method is for NSView-based outline views. At this point, you can choose to add in extra views or modify any properties on `rowView`.

## Parameters

- `outlineView`: The outline view that sent the message.
- `rowView`: The new row view.
- `row`: The row to which the view was added.

## See Also

- [func outlineView(NSOutlineView, didRemove: NSTableRowView, forRow: Int)](nsoutlineviewdelegate/outlineview(_:didremove:forrow:).md)
  Implemented to know when a row view is removed from the table
- [func outlineView(NSOutlineView, rowViewForItem: Any) -> NSTableRowView?](nsoutlineviewdelegate/outlineview(_:rowviewforitem:).md)
  implement this method to return a custom `NSTableRowView` for a particular item.
- [func outlineView(NSOutlineView, viewFor: NSTableColumn?, item: Any) -> NSView?](nsoutlineviewdelegate/outlineview(_:viewfor:item:).md)
  Implemented to return the view used to display the specified item and column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/outlineview(_:didadd:forrow:))*