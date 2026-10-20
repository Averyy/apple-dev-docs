# outlineView(_:heightOfRowByItem:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the height in points of the row containing `item`.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
optional func outlineView(_ outlineView: NSOutlineView, heightOfRowByItem item: Any) -> CGFloat
```

```objc
- (CGFloat) outlineView:(NSOutlineView *) outlineView heightOfRowByItem:(id) item;
```

#### Return Value

The height of the row.

#### Discussion

Values returned by this method should not include intercell spacing and must be greater than `0`.

Implement this method to support an outline view with varying row heights.

For large tables in particular, you should make sure that this method is efficient. `NSOutlineView` may cache the values this method returns, so if you would like to change a row’s height make sure to invalidate the row height by calling [`noteHeightOfRows(withIndexesChanged:)`](../nstableview/noteheightofrows%28withindexeschanged%29.md). `NSOutlineView` automatically invalidates its entire row height cache in [`reloadData()`](../nstableview/reloaddata%28%29.md) and [`noteNumberOfRowsChanged()`](../nstableview/notenumberofrowschanged%28%29.md).

If you call [`view(atColumn:row:makeIfNecessary:)`](../nstableview/view%28atcolumn,row,makeifnecessary%29.md) or [`rowView(atRow:makeIfNecessary:)`](../nstableview/rowview%28atrow,makeifnecessary%29.md) within your implementation of this method, an exception is thrown.

> ❗ **Important**:  To avoid the possibility of a hang due to unexpected recursion, don’t call geometry-calculating methods such as [`bounds`](../nsview/bounds.md), [`rect(ofColumn:)`](../nstableview/rect%28ofcolumn%29.md), or any `NSTableView` method that calls [`tile()`](../nstableview/tile%28%29.md) within your implementation of this method.

## Parameters

- `outlineView`: The outline view that sent the message.
- `item`: The row item.

## See Also

### Customizing Column and Row Sizes
- [func outlineView(NSOutlineView, sizeToFitWidthOfColumn: Int) -> CGFloat](./outlineview%28_,sizetofitwidthofcolumn%29.md)
  Invoked to allow the delegate to provide custom sizing behavior when a column’s resize divider is double clicked.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/outlineview(_:heightofrowbyitem:))*