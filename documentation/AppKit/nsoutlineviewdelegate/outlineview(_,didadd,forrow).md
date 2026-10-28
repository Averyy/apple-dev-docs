# outlineView(_:didAdd:forRow:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Implemented to know when a new row view is added to the table.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
optional func outlineView(_ outlineView: NSOutlineView, didAdd rowView: NSTableRowView, forRow row: Int)
```

```objc
- (void) outlineView:(NSOutlineView *) outlineView didAddRowView:(NSTableRowView *) rowView forRow:(NSInteger) row;
```

## Discussion

This delegate method is for NSView-based outline views. At this point, you can choose to add in extra views or modify any properties on `rowView`.

## Parameters

- `outlineView`: The outline view that sent the message.
- `rowView`: The new row view.
- `row`: The row to which the view was added.

## See Also

### Working with NSView-Based Outline Views
- [func outlineView(NSOutlineView, didRemove: NSTableRowView, forRow: Int)](./outlineview%28_,didremove,forrow%29.md)
  Implemented to know when a row view is removed from the table
- [func outlineView(NSOutlineView, rowViewForItem: Any) -> NSTableRowView?](./outlineview%28_,rowviewforitem%29.md)
  implement this method to return a custom `NSTableRowView` for a particular item.
- [func outlineView(NSOutlineView, viewFor: NSTableColumn?, item: Any) -> NSView?](./outlineview%28_,viewfor,item%29.md)
  Implemented to return the view used to display the specified item and column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/outlineview(_:didadd:forrow:))*