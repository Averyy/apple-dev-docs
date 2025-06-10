# outlineView(_:heightOfRowByItem:)

**Framework**: AppKit  
**Kind**: method

Returns the height in points of the row containing `item`.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
optional func outlineView(_ outlineView: NSOutlineView, heightOfRowByItem item: Any) -> CGFloat
```

#### Return Value

The height of the row.

#### Discussion

Values returned by this method should not include intercell spacing and must be greater than `0`.

Implement this method to support an outline view with varying row heights.

For large tables in particular, you should make sure that this method is efficient. `NSOutlineView` may cache the values this method returns, so if you would like to change a row’s height make sure to invalidate the row height by calling [`noteHeightOfRows(withIndexesChanged:)`](nstableview/noteheightofrows(withindexeschanged:).md). `NSOutlineView` automatically invalidates its entire row height cache in [`reloadData()`](nstableview/reloaddata().md) and [`noteNumberOfRowsChanged()`](nstableview/notenumberofrowschanged().md).

If you call [`view(atColumn:row:makeIfNecessary:)`](nstableview/view(atcolumn:row:makeifnecessary:).md) or [`rowView(atRow:makeIfNecessary:)`](nstableview/rowview(atrow:makeifnecessary:).md) within your implementation of this method, an exception is thrown.

> ❗ **Important**:  To avoid the possibility of a hang due to unexpected recursion, don’t call geometry-calculating methods such as [`bounds`](nsview/bounds.md), [`rect(ofColumn:)`](nstableview/rect(ofcolumn:).md), or any `NSTableView` method that calls [`tile()`](nstableview/tile().md) within your implementation of this method.

## Parameters

- `outlineView`: The outline view that sent the message.
- `item`: The row item.

## See Also

- [func outlineView(NSOutlineView, sizeToFitWidthOfColumn: Int) -> CGFloat](nsoutlineviewdelegate/outlineview(_:sizetofitwidthofcolumn:).md)
  Invoked to allow the delegate to provide custom sizing behavior when a column’s resize divider is double clicked.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/outlineview(_:heightofrowbyitem:))*