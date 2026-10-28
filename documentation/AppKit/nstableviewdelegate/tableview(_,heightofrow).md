# tableView(_:heightOfRow:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate for the height of the specified row.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
optional func tableView(_ tableView: NSTableView, heightOfRow row: Int) -> CGFloat
```

```objc
- (CGFloat) tableView:(NSTableView *) tableView heightOfRow:(NSInteger) row;
```

## Return Value

The height of the row. The height doesn’t include intercell spacing and must be greater than zero.

## Discussion

Implement this method if your table supports varying row heights.

Although table views may cache the returned values, you should ensure that this method is efficient. When you change a row’s height you must invalidate the existing row height by calling [`noteHeightOfRows(withIndexesChanged:)`](../nstableview/noteheightofrows%28withindexeschanged%29.md).  [`NSTableView`](../nstableview.md) automatically invalidates its entire row height cache in response to calls to [`reloadData()`](../nstableview/reloaddata%28%29.md) or [`noteNumberOfRowsChanged()`](../nstableview/notenumberofrowschanged%28%29.md).

If you call [`view(atColumn:row:makeIfNecessary:)`](../nstableview/view%28atcolumn,row,makeifnecessary%29.md) or [`rowView(atRow:makeIfNecessary:)`](../nstableview/rowview%28atrow,makeifnecessary%29.md) within your implementation of this method, the table view throws an exception.

> ❗ **Important**:  To avoid the possibility of a hang due to unexpected recursion, don’t call geometry-calculating methods such as [`bounds`](../nsview/bounds.md),  [`rect(ofColumn:)`](../nstableview/rect%28ofcolumn%29.md), or any [`NSTableView`](../nstableview.md) method that calls [`tile()`](../nstableview/tile%28%29.md) within your implementation of this method, such as [`intercellSpacing`](../nstableview/intercellspacing.md). To confirm your code isn’t inadvertently causing any calls to [`tile()`](../nstableview/tile%28%29.md), set a breakpoint on [`tile()`](../nstableview/tile%28%29.md) in Xcode.

## Parameters

- `tableView`: The table view that sent the message.
- `row`: The row index.

## See Also

### Setting row and column size
- [func tableView(NSTableView, sizeToFitWidthOfColumn: Int) -> CGFloat](./tableview%28_,sizetofitwidthofcolumn%29.md)
  Asks the delegate to provide custom sizing behavior when a column’s resize divider is double clicked.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableviewdelegate/tableview(_:heightofrow:))*