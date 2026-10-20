# tableView(_:heightOfRow:)

**Framework**: AppKit  
**Kind**: method

Asks the delegate for the height of the specified row.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
optional func tableView(_ tableView: NSTableView, heightOfRow row: Int) -> CGFloat
```

#### Return Value

The height of the row. The height doesn’t include intercell spacing and must be greater than zero.

#### Discussion

Implement this method if your table supports varying row heights.

Although table views may cache the returned values, you should ensure that this method is efficient. When you change a row’s height you must invalidate the existing row height by calling [`noteHeightOfRows(withIndexesChanged:)`](nstableview/noteheightofrows(withindexeschanged:).md).  [`NSTableView`](nstableview.md) automatically invalidates its entire row height cache in response to calls to [`reloadData()`](nstableview/reloaddata().md) or [`noteNumberOfRowsChanged()`](nstableview/notenumberofrowschanged().md).

If you call [`view(atColumn:row:makeIfNecessary:)`](nstableview/view(atcolumn:row:makeifnecessary:).md) or [`rowView(atRow:makeIfNecessary:)`](nstableview/rowview(atrow:makeifnecessary:).md) within your implementation of this method, the table view throws an exception.

> ❗ **Important**:  To avoid the possibility of a hang due to unexpected recursion, don’t call geometry-calculating methods such as [`bounds`](nsview/bounds.md),  [`rect(ofColumn:)`](nstableview/rect(ofcolumn:).md), or any [`NSTableView`](nstableview.md) method that calls [`tile()`](nstableview/tile().md) within your implementation of this method, such as [`intercellSpacing`](nstableview/intercellspacing.md). To confirm your code isn’t inadvertently causing any calls to [`tile()`](nstableview/tile().md), set a breakpoint on [`tile()`](nstableview/tile().md) in Xcode.

## Parameters

- `tableView`: The table view that sent the message.
- `row`: The row index.

## See Also

- [func tableView(NSTableView, sizeToFitWidthOfColumn: Int) -> CGFloat](nstableviewdelegate/tableview(_:sizetofitwidthofcolumn:).md)
  Asks the delegate to provide custom sizing behavior when a column’s resize divider is double clicked.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableviewdelegate/tableview(_:heightofrow:))*