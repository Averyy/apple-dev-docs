# outlineView(_:rowViewForItem:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

implement this method to return a custom `NSTableRowView` for a particular item.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
optional func outlineView(_ outlineView: NSOutlineView, rowViewForItem item: Any) -> NSTableRowView?
```

```objc
- (NSTableRowView *) outlineView:(NSOutlineView *) outlineView rowViewForItem:(id) item;
```

## Return Value

An instance or subclass of `NSTableRowView`. If `nil` is returned, a `NSTableRowView` instance is created and used.

## Discussion

This method, if implemented, is only invoked for NSView-based outline views.

## Parameters

- `outlineView`: The outline view that sent the message.
- `item`: The item displayed by the returned table row view.

## See Also

### Working with NSView-Based Outline Views
- [func outlineView(NSOutlineView, didAdd: NSTableRowView, forRow: Int)](./outlineview%28_,didadd,forrow%29.md)
  Implemented to know when a new row view is added to the table.
- [func outlineView(NSOutlineView, didRemove: NSTableRowView, forRow: Int)](./outlineview%28_,didremove,forrow%29.md)
  Implemented to know when a row view is removed from the table
- [func outlineView(NSOutlineView, viewFor: NSTableColumn?, item: Any) -> NSView?](./outlineview%28_,viewfor,item%29.md)
  Implemented to return the view used to display the specified item and column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/outlineview(_:rowviewforitem:))*