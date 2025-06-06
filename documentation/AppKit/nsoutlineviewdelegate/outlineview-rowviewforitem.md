# outlineView(_:rowViewForItem:)

**Framework**: AppKit  
**Kind**: method

implement this method to return a custom `NSTableRowView` for a particular item.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
optional func outlineView(_ outlineView: NSOutlineView, rowViewForItem item: Any) -> NSTableRowView?
```

#### Return Value

An instance or subclass of `NSTableRowView`. If `nil` is returned, a `NSTableRowView` instance is created and used.

#### Discussion

This method, if implemented, is only invoked for NSView-based outline views.

## Parameters

- `outlineView`: The outline view that sent the message.
- `item`: The item displayed by the returned table row view.

## See Also

- [func outlineView(NSOutlineView, didAdd: NSTableRowView, forRow: Int)](nsoutlineviewdelegate/outlineview(_:didadd:forrow:).md)
  Implemented to know when a new row view is added to the table.
- [func outlineView(NSOutlineView, didRemove: NSTableRowView, forRow: Int)](nsoutlineviewdelegate/outlineview(_:didremove:forrow:).md)
  Implemented to know when a row view is removed from the table
- [func outlineView(NSOutlineView, viewFor: NSTableColumn?, item: Any) -> NSView?](nsoutlineviewdelegate/outlineview(_:viewfor:item:).md)
  Implemented to return the view used to display the specified item and column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/outlineview(_:rowviewforitem:))*